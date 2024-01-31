@description('Azure Cosmos DB MongoDB vCore cluster name')
@maxLength(44)
param clusterName string

@description('Location for the cluster.')
param location string = resourceGroup().location

@description('Username for admin user')
param adminUsername string

@secure()
@description('Password for admin user')
@minLength(8)
@maxLength(128)
param adminPassword string

resource cluster 'Microsoft.DocumentDB/mongoClusters@2022-10-15-preview' = {
  name: clusterName
  location: location
  properties: {
    administratorLogin: adminUsername
    administratorLoginPassword: adminPassword
    nodeGroupSpecs: [
        {
            kind: 'Shard'
            nodeCount: 1
            sku: 'M30'
            diskSizeGB: 128
            enableHa: false
        }
    ]
  }
}

resource firewallRules 'Microsoft.DocumentDB/mongoClusters/firewallRules@2022-10-15-preview' = {
  parent: cluster
  name: 'AllowAllAzureServices'
  properties: {
    startIpAddress: '0.0.0.0'
    endIpAddress: '0.0.0.0'
  }
}
