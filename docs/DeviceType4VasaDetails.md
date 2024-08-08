# DeviceType4VasaDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**system_id** | **str** | SystemId of the storage system | [optional] 
**vasa** | [**DeviceType4Vasa**](DeviceType4Vasa.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_vasa_details import DeviceType4VasaDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VasaDetails from a JSON string
device_type4_vasa_details_instance = DeviceType4VasaDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VasaDetails.to_json())

# convert the object into a dict
device_type4_vasa_details_dict = device_type4_vasa_details_instance.to_dict()
# create an instance of DeviceType4VasaDetails from a dict
device_type4_vasa_details_from_dict = DeviceType4VasaDetails.from_dict(device_type4_vasa_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


