@description('The name for the Azure virtual network to be created.')
param virtualNetworkName string = ''

@description('The name of the virtual network subnet to be used for Azure App Service regional virtual network integration.')
param subnetPostgresName string = ''

@description('Azure region for the virtual network.')
param location string = resourceGroup().location

@description('The virtual network IP space to use for the new virutal network.')
param vnetAddressPrefix string = '10.0.0.0/16'

@description('The Subnet IP space to use for the new subnet.')
param subnetAddressPrefix string = '10.0.1.0/24'

param privateDnsZoneName string = ''


resource virtualNetwork 'Microsoft.Network/virtualNetworks@2019-11-01' = {
  name: virtualNetworkName
  location: location
  properties: {
    addressSpace: {
      addressPrefixes: [
        vnetAddressPrefix
      ]
    }
    subnets: [
      {
        name: subnetPostgresName
        properties: {
          addressPrefix: subnetAddressPrefix
          delegations: [
            {
              name: 'delegation'
              properties: {
                serviceName: 'Microsoft.DBforPostgreSQL/flexibleServers'
              }
            }
          ] 
        }
      }
    ]
  }
  resource appServiceIntegrationSubnet 'subnets' existing = {
    name: subnetPostgresName
  }
}

resource privateDnsZones 'Microsoft.Network/privateDnsZones@2020-06-01' = {
  name: privateDnsZoneName
  location: 'global'
}

resource privateDnsZoneVNetLink 'Microsoft.Network/privateDnsZones/virtualNetworkLinks@2018-09-01' = {
  name: '${privateDnsZoneName}/vnetlink'
  location: 'global'
  properties: {
    registrationEnabled: true
    virtualNetwork: {
      id: virtualNetwork.id
    }
  }
}

output privateDnsZoneArmResourceId string = privateDnsZones.id

output virtualNetworkName string = virtualNetwork.name
output virtualNetworkId string = virtualNetwork.id
output subnetAppServiceIntId string = virtualNetwork::appServiceIntegrationSubnet.id
