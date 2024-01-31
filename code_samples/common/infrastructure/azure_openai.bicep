param name string = 'openai-vector-search'
param location string = resourceGroup().location

@description('Specifies whether or not public endpoint access is allowed for this account..')
@allowed([
  'Enabled'
  'Disabled'
])
param publicNetworkAccess string = 'Enabled'

param sku object = {
  name: 'S0'
}

@description('Specifies the identity of the OpenAI resource.')
param identity object = {
  type: 'SystemAssigned'
}

// Resources
resource openai 'Microsoft.CognitiveServices/accounts@2022-12-01' = {
  name: name
  location: location
  sku: sku
  kind: 'OpenAI'
  identity: identity
  properties: {
    publicNetworkAccess: publicNetworkAccess
  }
}

resource model 'Microsoft.CognitiveServices/accounts/deployments@2023-05-01' = {
  name: 'text-embedding-ada-002'
  parent: openai
  properties: {
    model: {
      format: 'OpenAI'
      name: 'text-embedding-ada-002'
      version: '2'
    }
    raiPolicyName: ''
  }
}

// Outputs
// output id string = openai.id
// output name string = openai.name
