# NimbleShelfListItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **str** | ID of array the shelf belongs to. &#x60;Filter, Sort&#x60; | [optional] 
**array_name** | **str** | Name of array the shelf belongs to. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Identifier of the shelf. &#x60;Filter&#x60; | [optional] 
**model** | **str** | Model of the shelf or head unit. &#x60;Filter, Sort&#x60; | [optional] 
**serial** | **str** | The serial number of the chassis. &#x60;Filter, Sort&#x60; | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**chassis_sensors** | [**List[NimbleNsShelfSensor]**](NimbleNsShelfSensor.md) | List of chassis sensor readings. | [optional] 
**chassis_type** | **str** | Chassis type. Possible values: &#39;chassis_unknown&#39;, &#39;chassis_3u16&#39;, &#39;chassis_4u24&#39;, &#39;chassis_nmbl_2u12&#39;, &#39;chassis_nmbl_4u24&#39; | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**ctrlrs** | [**List[NimbleNsShelfCtrlr]**](NimbleNsShelfCtrlr.md) | List of ctrlr info. | [optional] 
**customer_id** | **str** | customerId | [optional] 
**disk_sets** | [**List[NimbleNsDiskSetAttr]**](NimbleNsDiskSetAttr.md) | Attributes for the disk sets in this shelf. | [optional] 
**fan_overall_status** | **str** | The overall status for the fans on both controllers. Possible values: &#39;OK&#39;, &#39;Alerted&#39;, &#39;Failed&#39;, &#39;Missing&#39;. | [optional] 
**generation** | **int** | generation | [optional] 
**model_ext** | **str** | Extended model of the shelf or head unit. | [optional] 
**psu_overall_status** | **str** | The overall status for the PSUs. Possible values: &#39;OK&#39;, &#39;Alerted&#39;, &#39;Failed&#39;, &#39;Missing&#39;. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**temp_overall_status** | **str** | The overall status for the temperature on both controllers. Possible values: &#39;OK&#39;, &#39;Alerted&#39;, &#39;Failed&#39;, &#39;Missing&#39;. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.nimble_shelf_list_items_inner import NimbleShelfListItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleShelfListItemsInner from a JSON string
nimble_shelf_list_items_inner_instance = NimbleShelfListItemsInner.from_json(json)
# print the JSON string representation of the object
print(NimbleShelfListItemsInner.to_json())

# convert the object into a dict
nimble_shelf_list_items_inner_dict = nimble_shelf_list_items_inner_instance.to_dict()
# create an instance of NimbleShelfListItemsInner from a dict
nimble_shelf_list_items_inner_from_dict = NimbleShelfListItemsInner.from_dict(nimble_shelf_list_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


