# DeviceType4VasaUriInfo

List of VASA Service URLs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_valid** | **int** | Specifies whether VASA Service URL is valid or not | [optional] 
**uri** | **str** | VASA Service URL | [optional] 

## Example

```python
from dscc.models.device_type4_vasa_uri_info import DeviceType4VasaUriInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VasaUriInfo from a JSON string
device_type4_vasa_uri_info_instance = DeviceType4VasaUriInfo.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VasaUriInfo.to_json())

# convert the object into a dict
device_type4_vasa_uri_info_dict = device_type4_vasa_uri_info_instance.to_dict()
# create an instance of DeviceType4VasaUriInfo from a dict
device_type4_vasa_uri_info_from_dict = DeviceType4VasaUriInfo.from_dict(device_type4_vasa_uri_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


