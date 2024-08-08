# EnclosurePowersList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ac_status** | **str** |  | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dc_status** | **str** |  | [optional] 
**displayname** | **str** | Enclosure power Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**element_status_code** | **str** | Enclosure status code | [optional] 
**enclosure_device_id** | **int** |  | [optional] 
**enclosure_id** | **str** | Parent UID of the resource. &#x60;Filter&#x60; | [optional] 
**enclosure_name** | **str** | Name of the enclosure power. | [optional] 
**enclosure_power_id** | **int** | Numeric ID of the resource | [optional] 
**enclosure_type** | [**EnclosureTypeSingle**](EnclosureTypeSingle.md) |  | [optional] 
**fail_indicator** | **bool** |  | [optional] 
**fail_input** | **bool** |  | [optional] 
**fail_output** | **bool** |  | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**locate_enabled** | **bool** | Indicates if the locate beacon is enabled or not | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**model_read_only** | **bool** |  | [optional] 
**name** | **str** | Name of the resource. | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure power object | [optional] 
**safe_to_remove** | **bool** |  | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.enclosure_powers_list import EnclosurePowersList

# TODO update the JSON string below
json = "{}"
# create an instance of EnclosurePowersList from a JSON string
enclosure_powers_list_instance = EnclosurePowersList.from_json(json)
# print the JSON string representation of the object
print(EnclosurePowersList.to_json())

# convert the object into a dict
enclosure_powers_list_dict = enclosure_powers_list_instance.to_dict()
# create an instance of EnclosurePowersList from a dict
enclosure_powers_list_from_dict = EnclosurePowersList.from_dict(enclosure_powers_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


