
param administratorLogin string = ''
@secure()
param administratorLoginPassword string
param location string = 'eastus'
param serverName string = ''
param psqlDatabaseName string = ''
param version string = '15'
param serverInstanceType string = 'Standard_B1ms'
param serverEdition string = 'Burstable'
param deployVNET bool = false

module network 'vnet.bicep' = if (deployVNET) {
  name: 'vnet'
  params: {
    location: location
    privateDnsZoneName: '${serverName}.private.postgres.database.azure.com'
  }
}

resource dbServer 'Microsoft.DBforPostgreSQL/flexibleServers@2021-06-01' = {
  name: serverName
  location: location
  sku: {
    name: serverInstanceType
    tier: serverEdition
  }
  properties: {
    createMode: 'Default'
    version: version
    administratorLogin: administratorLogin
    administratorLoginPassword: administratorLoginPassword
    storage: {
      storageSizeGB: 32
    }
    backup: {
      backupRetentionDays: 7
      geoRedundantBackup: 'Disabled'
    }
    network: (deployVNET) ? {
      delegatedSubnetResourceId: network.outputs.subnetPostgresId
      privateDnsZoneArmResourceId: network.outputs.privateDnsZoneArmResourceId
    } : {}
  }
}

resource configurations 'Microsoft.DBforPostgreSQL/flexibleServers/configurations@2022-12-01' = {
  name: 'azure.extensions'
  parent: dbServer
  properties: {
    value: 'vector'
    source: 'user-override'
  } 
}

resource vectorDB 'Microsoft.DBforPostgreSQL/flexibleServers/databases@2022-12-01' = {
  parent: dbServer
  name: psqlDatabaseName
  properties: {
    charset: 'UTF8'
    collation: 'en_US.UTF8'
  }
}
