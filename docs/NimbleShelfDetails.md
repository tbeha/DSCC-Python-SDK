# NimbleShelfDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from dscc.models.nimble_shelf_details import NimbleShelfDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleShelfDetails from a JSON string
nimble_shelf_details_instance = NimbleShelfDetails.from_json(json)
# print the JSON string representation of the object
print(NimbleShelfDetails.to_json())

# convert the object into a dict
nimble_shelf_details_dict = nimble_shelf_details_instance.to_dict()
# create an instance of NimbleShelfDetails from a dict
nimble_shelf_details_from_dict = NimbleShelfDetails.from_dict(nimble_shelf_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


