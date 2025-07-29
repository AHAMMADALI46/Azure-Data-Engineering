param location string = resourceGroup().location
param storageAccountName string
param dataFactoryName string

resource storageAccount 'Microsoft.Storage/storageAccounts@2022-09-01' = {
  name: storageAccountName
  location: location
  sku: { name: 'Standard_LRS' }
  kind: 'StorageV2'
}

resource dataFactory 'Microsoft.DataFactory/factories@2018-06-01' = {
  name: dataFactoryName
  location: location
}

output storageAccountId string = storageAccount.id
output dataFactoryId string = dataFactory.id