# DeviceType4ProtectionPoliciesList

Response body for view protection policy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[DeviceType4ProtectionPoliciesListAssociatedLinksInner]**](DeviceType4ProtectionPoliciesListAssociatedLinksInner.md) | Associated Links | [optional] 
**items** | [**List[DeviceType4ProtectionPolicy]**](DeviceType4ProtectionPolicy.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestURI for Protection Policy for application set | [optional] 
**total** | **int** | Total number of protection policies for application set. | [optional] 

## Example

```python
from dscc.models.device_type4_protection_policies_list import DeviceType4ProtectionPoliciesList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ProtectionPoliciesList from a JSON string
device_type4_protection_policies_list_instance = DeviceType4ProtectionPoliciesList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ProtectionPoliciesList.to_json())

# convert the object into a dict
device_type4_protection_policies_list_dict = device_type4_protection_policies_list_instance.to_dict()
# create an instance of DeviceType4ProtectionPoliciesList from a dict
device_type4_protection_policies_list_from_dict = DeviceType4ProtectionPoliciesList.from_dict(device_type4_protection_policies_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


