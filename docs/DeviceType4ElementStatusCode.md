# DeviceType4ElementStatusCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Text in the default language | [optional] 
**key** | **str** | Key of the message in the i18n catalog | [optional] 

## Example

```python
from dscc.models.device_type4_element_status_code import DeviceType4ElementStatusCode

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ElementStatusCode from a JSON string
device_type4_element_status_code_instance = DeviceType4ElementStatusCode.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ElementStatusCode.to_json())

# convert the object into a dict
device_type4_element_status_code_dict = device_type4_element_status_code_instance.to_dict()
# create an instance of DeviceType4ElementStatusCode from a dict
device_type4_element_status_code_from_dict = DeviceType4ElementStatusCode.from_dict(device_type4_element_status_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


