# DeviceType4ProtectionPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**policy** | [**DeviceType4ProtectionPolicyPolicy**](DeviceType4ProtectionPolicyPolicy.md) |  | [optional] 
**protection_policy_type** | **str** | Protection policy type: schedule, sync or async | [optional] 
**schedules** | [**DeviceType4ProtectionPolicySchedules**](DeviceType4ProtectionPolicySchedules.md) |  | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.device_type4_protection_policy import DeviceType4ProtectionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ProtectionPolicy from a JSON string
device_type4_protection_policy_instance = DeviceType4ProtectionPolicy.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ProtectionPolicy.to_json())

# convert the object into a dict
device_type4_protection_policy_dict = device_type4_protection_policy_instance.to_dict()
# create an instance of DeviceType4ProtectionPolicy from a dict
device_type4_protection_policy_from_dict = DeviceType4ProtectionPolicy.from_dict(device_type4_protection_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


