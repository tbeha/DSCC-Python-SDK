# PrimeraSupportedProtectionTypes

Response body for supported protection types on an application set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**async_partners** | [**List[PrimeraReplicationPartner]**](PrimeraReplicationPartner.md) | List of potential replication partners that can be part of asynchronous protection policy | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**is_sld_supported** | **bool** | Shows if SLD is supported or not | [optional] 
**protection_types** | **List[str]** | List of protection policies types that can be configured on the application set Possible values: schedule, async, sync | [optional] 
**request_uri** | **str** | requestUri for supported protection types | [optional] 
**sync_partners** | [**List[PrimeraReplicationPartner]**](PrimeraReplicationPartner.md) | List of potential replication partners that can be part of synchronous protection policy | [optional] 

## Example

```python
from dscc.models.primera_supported_protection_types import PrimeraSupportedProtectionTypes

# TODO update the JSON string below
json = "{}"
# create an instance of PrimeraSupportedProtectionTypes from a JSON string
primera_supported_protection_types_instance = PrimeraSupportedProtectionTypes.from_json(json)
# print the JSON string representation of the object
print(PrimeraSupportedProtectionTypes.to_json())

# convert the object into a dict
primera_supported_protection_types_dict = primera_supported_protection_types_instance.to_dict()
# create an instance of PrimeraSupportedProtectionTypes from a dict
primera_supported_protection_types_from_dict = PrimeraSupportedProtectionTypes.from_dict(primera_supported_protection_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


