# DeviceType4private


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reserved** | **float** |  | [optional] 
**reserved_v_vols** | **float** |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from dscc.models.device_type4private import DeviceType4private

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4private from a JSON string
device_type4private_instance = DeviceType4private.from_json(json)
# print the JSON string representation of the object
print(DeviceType4private.to_json())

# convert the object into a dict
device_type4private_dict = device_type4private_instance.to_dict()
# create an instance of DeviceType4private from a dict
device_type4private_from_dict = DeviceType4private.from_dict(device_type4private_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


