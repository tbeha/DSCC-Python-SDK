# DeviceType4cardType

Type of the PCI card this port is on

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from dscc.models.device_type4card_type import DeviceType4cardType

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4cardType from a JSON string
device_type4card_type_instance = DeviceType4cardType.from_json(json)
# print the JSON string representation of the object
print(DeviceType4cardType.to_json())

# convert the object into a dict
device_type4card_type_dict = device_type4card_type_instance.to_dict()
# create an instance of DeviceType4cardType from a dict
device_type4card_type_from_dict = DeviceType4cardType.from_dict(device_type4card_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


