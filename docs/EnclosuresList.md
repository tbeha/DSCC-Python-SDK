# EnclosuresList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**chain_pos_loop_a** | **int** |  | [optional] 
**chain_pos_loop_b** | **int** |  | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dc4data** | [**Dc4data**](Dc4data.md) |  | [optional] 
**dcsdata** | [**EncDcsdata**](EncDcsdata.md) |  | [optional] 
**detailed_state** | **str** |  | [optional] 
**displayname** | **str** | Enclosure Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**enclosure_id** | **int** | Numeric ID of the resource | [optional] 
**enclosure_type** | [**EnclosureTypeSingle**](EnclosureTypeSingle.md) |  | [optional] 
**errors** | [**List[DeviceType4errorsInner]**](DeviceType4errorsInner.md) | Errors occurred in enclosure | [optional] 
**fail_indicator** | **bool** |  | [optional] 
**fail_requested** | **bool** |  | [optional] 
**form_factor** | **str** |  | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**locate_enabled** | **bool** | Indicates if the locate beacon is enabled or not | [optional] 
**location** | **str** | Location of the resource | [optional] 
**loop_split** | **bool** |  | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**name** | **str** | Name of the resource. &#x60;Filter, Sort&#x60; | [optional] 
**node_wwn** | **str** | WWn of the node resource | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure object | [optional] 
**state** | [**ENCSTATE**](ENCSTATE.md) |  | [optional] 
**sub_type** | **str** | Enclosure sub type | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 
**warn_indicator** | **bool** |  | [optional] 
**warn_requested** | **bool** |  | [optional] 

## Example

```python
from dscc.models.enclosures_list import EnclosuresList

# TODO update the JSON string below
json = "{}"
# create an instance of EnclosuresList from a JSON string
enclosures_list_instance = EnclosuresList.from_json(json)
# print the JSON string representation of the object
print(EnclosuresList.to_json())

# convert the object into a dict
enclosures_list_dict = enclosures_list_instance.to_dict()
# create an instance of EnclosuresList from a dict
enclosures_list_from_dict = EnclosuresList.from_dict(enclosures_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


