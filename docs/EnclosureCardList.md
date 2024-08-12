# EnclosureCardList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dc4data** | [**EcDc4data**](EcDc4data.md) |  | [optional] 
**dcsdata** | [**EcDcsdata**](EcDcsdata.md) |  | [optional] 
**displayname** | **str** | Enclosure Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**element_status_code** | **str** | Enclosure status code | [optional] 
**enclosure_card_id** | **int** | Numeric ID of the resource | [optional] 
**enclosure_device_id** | **int** |  | [optional] 
**enclosure_id** | **str** | Parent UID of the resource. &#x60;Filter&#x60; | [optional] 
**enclosure_name** | **str** | Name of the enclosure. &#x60;Filter, Sort&#x60; | [optional] 
**enclosure_type** | [**EnclosureTypeSingle**](EnclosureTypeSingle.md) |  | [optional] 
**fail_indicator** | **bool** |  | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**locate_enabled** | **bool** | Indicates if the locate beacon is enabled or not | [optional] 
**loop_a** | **bool** |  | [optional] 
**loop_b** | **bool** |  | [optional] 
**manufacturing** | [**Manufacturing**](Manufacturing.md) |  | [optional] 
**name** | **str** | Name of the resource. &#x60;Filter, Sort&#x60; | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure card object | [optional] 
**safe_to_remove** | **bool** |  | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.enclosure_card_list import EnclosureCardList

# TODO update the JSON string below
json = "{}"
# create an instance of EnclosureCardList from a JSON string
enclosure_card_list_instance = EnclosureCardList.from_json(json)
# print the JSON string representation of the object
print(EnclosureCardList.to_json())

# convert the object into a dict
enclosure_card_list_dict = enclosure_card_list_instance.to_dict()
# create an instance of EnclosureCardList from a dict
enclosure_card_list_from_dict = EnclosureCardList.from_dict(enclosure_card_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


