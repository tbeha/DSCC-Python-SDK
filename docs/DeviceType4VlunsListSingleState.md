# DeviceType4VlunsListSingleState

State of the resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detailed** | **List[Optional[str]]** | Array of the detailed states of the resource | [optional] 
**overall** | **str** | Overall state of the resource | [optional] 

## Example

```python
from dscc.models.device_type4_vluns_list_single_state import DeviceType4VlunsListSingleState

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VlunsListSingleState from a JSON string
device_type4_vluns_list_single_state_instance = DeviceType4VlunsListSingleState.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VlunsListSingleState.to_json())

# convert the object into a dict
device_type4_vluns_list_single_state_dict = device_type4_vluns_list_single_state_instance.to_dict()
# create an instance of DeviceType4VlunsListSingleState from a dict
device_type4_vluns_list_single_state_from_dict = DeviceType4VlunsListSingleState.from_dict(device_type4_vluns_list_single_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


