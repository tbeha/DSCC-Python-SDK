# DeviceType4StartParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_name** | **str** | Target name on which the protection has to be started. | [optional] 

## Example

```python
from dscc.models.device_type4_start_params import DeviceType4StartParams

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4StartParams from a JSON string
device_type4_start_params_instance = DeviceType4StartParams.from_json(json)
# print the JSON string representation of the object
print(DeviceType4StartParams.to_json())

# convert the object into a dict
device_type4_start_params_dict = device_type4_start_params_instance.to_dict()
# create an instance of DeviceType4StartParams from a dict
device_type4_start_params_from_dict = DeviceType4StartParams.from_dict(device_type4_start_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


