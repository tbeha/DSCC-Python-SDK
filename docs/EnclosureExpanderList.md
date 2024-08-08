# EnclosureExpanderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Name of the enclosure | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**element_status_code** | **str** | Enclosure status code | [optional] 
**enclosure_device_id** | **int** |  | [optional] 
**enclosure_expander_id** | **int** | Numeric ID of the resource | [optional] 
**enclosure_id** | **str** | Parent UID of the resource. &#x60;Filter&#x60; | [optional] 
**enclosure_name** | **str** | Name of the enclosure | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Enclosure Display name | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure expander object | [optional] 
**system_id** | **str** | systemId/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.enclosure_expander_list import EnclosureExpanderList

# TODO update the JSON string below
json = "{}"
# create an instance of EnclosureExpanderList from a JSON string
enclosure_expander_list_instance = EnclosureExpanderList.from_json(json)
# print the JSON string representation of the object
print(EnclosureExpanderList.to_json())

# convert the object into a dict
enclosure_expander_list_dict = enclosure_expander_list_instance.to_dict()
# create an instance of EnclosureExpanderList from a dict
enclosure_expander_list_from_dict = EnclosureExpanderList.from_dict(enclosure_expander_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


