# VasaDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**system_id** | **str** | SystemId of the storage system | [optional] 
**vasa** | [**Vasa**](Vasa.md) |  | [optional] 

## Example

```python
from dscc.models.vasa_details import VasaDetails

# TODO update the JSON string below
json = "{}"
# create an instance of VasaDetails from a JSON string
vasa_details_instance = VasaDetails.from_json(json)
# print the JSON string representation of the object
print(VasaDetails.to_json())

# convert the object into a dict
vasa_details_dict = vasa_details_instance.to_dict()
# create an instance of VasaDetails from a dict
vasa_details_from_dict = VasaDetails.from_dict(vasa_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


