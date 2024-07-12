param cosmosDbAccountName string = 'Replace the name of your Account - no capital letters'
param location string = 'replace location for example - West US'
param cosmosDbKind string = 'GlobalDocumentDB'
param cosmosDbOfferType string = 'Standard'
param cosmosDbCapabilities array = [
  {
    name: 'EnableServerless'
  }
]
param backupIntervalInMinutes int = 240
param backupRetentionIntervalInHours int = 8


resource cosmosDb 'Microsoft.DocumentDB/databaseAccounts@2021-04-15' = {
  name: cosmosDbAccountName
  location: location
  kind: cosmosDbKind
  properties: {
    databaseAccountOfferType: cosmosDbOfferType
    capabilities: cosmosDbCapabilities
    backupPolicy: {
      type: 'Periodic'
      periodicModeProperties: {
        backupIntervalInMinutes: backupIntervalInMinutes
        backupRetentionIntervalInHours: backupRetentionIntervalInHours
             }
    }
    consistencyPolicy: {
      defaultConsistencyLevel: 'Session'
      maxIntervalInSeconds: 5
      maxStalenessPrefix: 100
    }
    locations: [
      {
        locationName: location
        failoverPriority: 0
      }
    ]
    isVirtualNetworkFilterEnabled: false
    enableAutomaticFailover: false
    enableMultipleWriteLocations: false
    disableKeyBasedMetadataWriteAccess: false
    publicNetworkAccess: 'Enabled'
    enableFreeTier: false
    enableAnalyticalStorage: false
  
  }
}
