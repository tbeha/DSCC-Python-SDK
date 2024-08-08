# DeviceType4EditEnclosureInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | New Id of the enclosure | [optional] 
**location** | **str** | Location of the enclosure in the datacenter | [optional] 

## Example

```python
from dscc.models.device_type4_edit_enclosure_input import DeviceType4EditEnclosureInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EditEnclosureInput from a JSON string
device_type4_edit_enclosure_input_instance = DeviceType4EditEnclosureInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EditEnclosureInput.to_json())

# convert the object into a dict
device_type4_edit_enclosure_input_dict = device_type4_edit_enclosure_input_instance.to_dict()
# create an instance of DeviceType4EditEnclosureInput from a dict
device_type4_edit_enclosure_input_from_dict = DeviceType4EditEnclosureInput.from_dict(device_type4_edit_enclosure_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


