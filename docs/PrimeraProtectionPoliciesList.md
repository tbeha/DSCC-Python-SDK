# PrimeraProtectionPoliciesList

Response body for view protection policy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[DeviceType4ProtectionPoliciesListAssociatedLinksInner]**](DeviceType4ProtectionPoliciesListAssociatedLinksInner.md) | Associated Links | [optional] 
**items** | [**List[PrimeraProtectionPolicy]**](PrimeraProtectionPolicy.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestURI for Protection Policy for application set | [optional] 
**total** | **int** | Total number of protection policies for application set. | [optional] 

## Example

```python
from dscc.models.primera_protection_policies_list import PrimeraProtectionPoliciesList

# TODO update the JSON string below
json = "{}"
# create an instance of PrimeraProtectionPoliciesList from a JSON string
primera_protection_policies_list_instance = PrimeraProtectionPoliciesList.from_json(json)
# print the JSON string representation of the object
print(PrimeraProtectionPoliciesList.to_json())

# convert the object into a dict
primera_protection_policies_list_dict = primera_protection_policies_list_instance.to_dict()
# create an instance of PrimeraProtectionPoliciesList from a dict
primera_protection_policies_list_from_dict = PrimeraProtectionPoliciesList.from_dict(primera_protection_policies_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


