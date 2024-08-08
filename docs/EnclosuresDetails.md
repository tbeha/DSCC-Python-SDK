# EnclosuresDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**chain_pos_loop_a** | **int** |  | [optional] 
**chain_pos_loop_b** | **int** |  | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
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
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource. | [optional] 
**locate_enabled** | **bool** | Indicates if the locate beacon is enabled or not | [optional] 
**location** | **str** | Location of the resource | [optional] 
**loop_split** | **bool** |  | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**name** | **str** | Name of the resource. | [optional] 
**node_wwn** | **str** | WWn of the node resource | [optional] 
**request_uri** | **str** | resourceUri for detailed enclosure object | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure object | [optional] 
**state** | [**STATE**](STATE.md) |  | [optional] 
**sub_type** | **str** | Enclosure sub type | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 
**warn_indicator** | **bool** |  | [optional] 
**warn_requested** | **bool** |  | [optional] 

## Example

```python
from dscc.models.enclosures_details import EnclosuresDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EnclosuresDetails from a JSON string
enclosures_details_instance = EnclosuresDetails.from_json(json)
# print the JSON string representation of the object
print(EnclosuresDetails.to_json())

# convert the object into a dict
enclosures_details_dict = enclosures_details_instance.to_dict()
# create an instance of EnclosuresDetails from a dict
enclosures_details_from_dict = EnclosuresDetails.from_dict(enclosures_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


