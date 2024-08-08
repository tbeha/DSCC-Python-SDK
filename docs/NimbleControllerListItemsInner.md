# NimbleControllerListItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **str** | Rest ID of the array containing this controller. &#x60;Filter, Sort&#x60; | [optional] 
**array_name** | **str** | Name of the array containing this controller. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Identifier of the controller. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Name of the controller. &#x60;Filter, Sort&#x60; | [optional] 
**serial** | **str** | Serial number for this controller. &#x60;Filter, Sort&#x60; | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**asup_time** | **int** | Time of the last autosupport by the controller. | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**ctrlr_side** | **str** | Identifies which controller this is on its array. Possible values: &#39;A&#39;, &#39;B&#39;. | [optional] 
**customer_id** | **str** | customerId | [optional] 
**fan_status** | **str** | Overall fan status for the controller. Possible values: &#39;fan_failed&#39;, &#39;fan_okay&#39;, &#39;fan_alerted&#39;, &#39;fan_unknown&#39;. | [optional] 
**fans** | [**List[NimbleNsCtrlrHwSensorInfo]**](NimbleNsCtrlrHwSensorInfo.md) | Status for each fan in the controller. | [optional] 
**generation** | **int** | generation | [optional] 
**hostname** | **str** | Host name for the controller. | [optional] 
**nvme_cards** | [**List[NimbleNsCtrlrNvmeCard]**](NimbleNsCtrlrNvmeCard.md) | List of NVMe accelerator cards. | [optional] 
**nvme_cards_enabled** | **int** | Indicates if the NVMe accelerator card is enabled. | [optional] 
**partial_response_ok** | **bool** | Indicate that it is ok to provide partially available response. | [optional] 
**partition_status** | [**List[NimbleNsCtrlrRaidInfo]**](NimbleNsCtrlrRaidInfo.md) | Status of the system&#39;s raid partitions. | [optional] 
**power_status** | **str** | Overall power supply status for the controller. Possible values: &#39;ps_alerted&#39;, &#39;ps_okay&#39;, &#39;ps_failed&#39;, &#39;ps_unknown&#39;. | [optional] 
**power_supplies** | [**List[NimbleNsCtrlrHwSensorInfo]**](NimbleNsCtrlrHwSensorInfo.md) | Status for each power supply in the controller. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**state** | **str** | Indicates whether this controller is active or not. Possible values: &#39;start_active&#39;, &#39;start_standby&#39;, &#39;stale&#39;, &#39;standby&#39;, &#39;active&#39;, &#39;solo&#39;, &#39;none&#39;. | [optional] 
**support_address** | **str** | IP address used for support. | [optional] 
**support_netmask** | **str** | IP netmask used for support. | [optional] 
**support_nic** | **str** | Network card used for support. | [optional] 
**temperature_sensors** | [**List[NimbleNsCtrlrHwSensorInfo]**](NimbleNsCtrlrHwSensorInfo.md) | Status for temperature sensor in the controller. | [optional] 
**temperature_status** | **str** | Overall temperature status for the controller. Possible values: &#39;temperature_unknown&#39;, &#39;temperature_alerted&#39;, &#39;temperature_okay&#39;, &#39;temperature_fail&#39;. | [optional] 
**type** | **str** | type | [optional] 
**update_end_time** | **int** | End time of last update. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**update_error_code** | **str** | If the software update has failed, this indicates the error code corresponding to the failure. Non-negative integer in range [0,9000]. | [optional] 
**update_progress_msg** | **str** | Group update detailed progress message. Plain string. | [optional] 
**update_start_time** | **int** | Start time of last update. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**update_state** | **str** | Group update state.Possible values: &#39;invalid&#39;, &#39;normal&#39;, &#39;updating&#39;, &#39;timed_out&#39;, &#39;failed&#39;, &#39;paused&#39;. | [optional] 
**version_current** | **str** | Version of software running on the group. | [optional] 
**version_rollback** | **str** | Rollback software version for the group. | [optional] 
**version_target** | **str** | Desired software version for the group. | [optional] 

## Example

```python
from dscc.models.nimble_controller_list_items_inner import NimbleControllerListItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleControllerListItemsInner from a JSON string
nimble_controller_list_items_inner_instance = NimbleControllerListItemsInner.from_json(json)
# print the JSON string representation of the object
print(NimbleControllerListItemsInner.to_json())

# convert the object into a dict
nimble_controller_list_items_inner_dict = nimble_controller_list_items_inner_instance.to_dict()
# create an instance of NimbleControllerListItemsInner from a dict
nimble_controller_list_items_inner_from_dict = NimbleControllerListItemsInner.from_dict(nimble_controller_list_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


