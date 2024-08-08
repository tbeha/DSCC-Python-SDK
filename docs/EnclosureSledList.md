# EnclosureSledList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dc4data** | [**EsDc4data**](EsDc4data.md) |  | [optional] 
**disk_count** | **int** | Number of disks present | [optional] 
**displayname** | **str** | Enclosure Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**element_status_code** | **str** | Enclosure status code | [optional] 
**enclosure_device_id** | **int** |  | [optional] 
**enclosure_id** | **str** | Parent UID of the resource. &#x60;Filter&#x60; | [optional] 
**enclosure_name** | **str** | Name of the enclosure | [optional] 
**enclosure_type** | [**EnclosureTypeSingle**](EnclosureTypeSingle.md) |  | [optional] 
**fail_indicator** | **bool** |  | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**locate_enabled** | **bool** | Indicates if the locate beacon is enabled or not | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**name** | **str** | Name of the resource. &#x60;Filter, Sort&#x60; | [optional] 
**ok_indicator** | **bool** |  | [optional] 
**port_bypass_a** | **bool** |  | [optional] 
**port_bypass_b** | **bool** |  | [optional] 
**power** | **bool** |  | [optional] 
**pred_fail_indicator** | **bool** |  | [optional] 
**protocol** | **str** |  | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure card object | [optional] 
**safe_to_remove** | **bool** |  | [optional] 
**sled_id** | **int** | Numeric ID of the resource | [optional] 
**state_loop_a** | [**State**](State.md) |  | [optional] 
**state_loop_b** | [**State**](State.md) |  | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**temperature** | **int** |  | [optional] 
**type** | **str** | type | [optional] 
**wwn** | **str** |  | [optional] 

## Example

```python
from dscc.models.enclosure_sled_list import EnclosureSledList

# TODO update the JSON string below
json = "{}"
# create an instance of EnclosureSledList from a JSON string
enclosure_sled_list_instance = EnclosureSledList.from_json(json)
# print the JSON string representation of the object
print(EnclosureSledList.to_json())

# convert the object into a dict
enclosure_sled_list_dict = enclosure_sled_list_instance.to_dict()
# create an instance of EnclosureSledList from a dict
enclosure_sled_list_from_dict = EnclosureSledList.from_dict(enclosure_sled_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


