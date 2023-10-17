param location string = resourceGroup().location
param redisCacheName string = ''
param redisPrivateEndpointName string = ''
param privateLinkServiceConnectionName string = ''
param redisCacheSKU string = 'Enterprise_E10'


module network 'vnet.bicep' = {
  name: 'vnet'
  params: {
    location: location
    privateDnsZoneName: '${redisCacheName}.redis.cache.windows.net'
  }
}

resource redisEnterprise 'Microsoft.Cache/redisEnterprise@2022-01-01' = {
  name: redisCacheName
  location: location
  sku: {
    name: redisCacheSKU
    capacity: 2
  }
}

resource redisdatabase 'Microsoft.Cache/redisEnterprise/databases@2022-01-01' = {
  name: 'default'
  parent: redisEnterprise
  properties: {
    evictionPolicy: 'NoEviction'
    clusteringPolicy: 'EnterpriseCluster'
    modules: [
      {
        name: 'RediSearch'
      }
      {
        name: 'RedisJSON'
      }
    ]
    port: 10000
  }
}

resource rediscacheprivateendpoint 'Microsoft.Network/privateEndpoints@2020-06-01' = {
  name: redisPrivateEndpointName
  location: location
  properties: {
    subnet: {
      id: network.outputs.subnetRedisId
    }
    privateLinkServiceConnections: [
      {
        name: privateLinkServiceConnectionName
        properties: {
          privateLinkServiceId: redisEnterprise.id
          groupIds: [
            'redisEnterprise'
          ]
        }
      }
    ]
  }
}

