# DeviceType4CfgListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key of the vasa configuration | [optional] 
**value** | **str** | Value of the vasa key configuration | [optional] 

## Example

```python
from dscc.models.device_type4_cfg_list_inner import DeviceType4CfgListInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4CfgListInner from a JSON string
device_type4_cfg_list_inner_instance = DeviceType4CfgListInner.from_json(json)
# print the JSON string representation of the object
print(DeviceType4CfgListInner.to_json())

# convert the object into a dict
device_type4_cfg_list_inner_dict = device_type4_cfg_list_inner_instance.to_dict()
# create an instance of DeviceType4CfgListInner from a dict
device_type4_cfg_list_inner_from_dict = DeviceType4CfgListInner.from_dict(device_type4_cfg_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


