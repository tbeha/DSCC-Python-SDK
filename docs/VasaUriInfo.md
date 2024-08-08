# VasaUriInfo

List of VASA Service URLs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_valid** | **int** | Specifies whether VASA Service URL is valid or not | [optional] 
**uri** | **str** | VASA Service URL | [optional] 

## Example

```python
from dscc.models.vasa_uri_info import VasaUriInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VasaUriInfo from a JSON string
vasa_uri_info_instance = VasaUriInfo.from_json(json)
# print the JSON string representation of the object
print(VasaUriInfo.to_json())

# convert the object into a dict
vasa_uri_info_dict = vasa_uri_info_instance.to_dict()
# create an instance of VasaUriInfo from a dict
vasa_uri_info_from_dict = VasaUriInfo.from_dict(vasa_uri_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


