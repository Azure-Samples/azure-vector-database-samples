@secure()
param administratorLoginPassword string
param location string
param clusterName string
param nodeCount int
param enableHa bool
param coordinatorVCores int = 4
param coordinatorStorageQuotaInMb int = 262144
param coordinatorServerEdition string = 'GeneralPurpose'
param enableShardsOnCoordinator bool = true
param nodeServerEdition string = 'MemoryOptimized'
param nodeVCores int = 4
param nodeStorageQuotaInMb int = 524288
param coordinatorEnablePublicIpAccess bool = true
param nodeEnablePublicIpAccess bool = false

//Optional Parameters
//param availabilityZone string = '1'
//param postgresqlVersion string = '16'
//param citusVersion string = '12.1'

resource postgresCluster 'Microsoft.DBforPostgreSQL/serverGroupsv2@2022-11-08' = {
  name: clusterName
  location: location
  tags: {}
  properties: {
    administratorLoginPassword: administratorLoginPassword
    coordinatorServerEdition: coordinatorServerEdition
    coordinatorVCores: coordinatorVCores
    coordinatorStorageQuotaInMb: coordinatorStorageQuotaInMb
    enableShardsOnCoordinator: enableShardsOnCoordinator
    nodeCount: nodeCount
    nodeServerEdition: nodeServerEdition
    nodeVCores: nodeVCores
    nodeStorageQuotaInMb: nodeStorageQuotaInMb
    enableHa: enableHa
    coordinatorEnablePublicIpAccess: coordinatorEnablePublicIpAccess
    nodeEnablePublicIpAccess: nodeEnablePublicIpAccess
    //citusVersion: citusVersion
    //postgresqlVersion: postgresqlVersion
    //preferredPrimaryZone: availabilityZone
  }
}
