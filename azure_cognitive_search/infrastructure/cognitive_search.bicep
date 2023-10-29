param name string = ''
param location string = resourceGroup().location
param tags object = {}
param sku string = 'standard'


param authOptions object = {}

module network 'vnet.bicep' = {
  name: 'vnet'
  params: {
    location: location
    privateDnsZoneName: '${name}.search.windows.net'
  }
}

resource search 'Microsoft.Search/searchServices@2022-09-01' = {
  name: name
  location: location
  tags: tags
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    authOptions: authOptions
    disableLocalAuth: false
    hostingMode: 'default'
    networkRuleSet: {
      ipRules: []
    }
    partitionCount: 1
    publicNetworkAccess: 'disabled'
    replicaCount: 1
  }
  sku: {
    name: sku
  }
}

resource cognitivePrivateEndpoint 'Microsoft.Network/privateEndpoints@2020-06-01' = {
  name: '${name}-cognitive'
  location: location
  properties: {
    subnet: {
      id: network.outputs.subnetsearchId
    }
    privateLinkServiceConnections: [
      {
        name: 'cognitive'
        properties: {
          privateLinkServiceId: search.id
          groupIds: [
            'searchService'
          ]
        }
      }
    ]
  }
}
