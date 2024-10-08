# NimbleNsCtrlrHwSensorInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ctrlr_owner** | **str** | The controller owning this sensor. Possible values: &#39;A&#39;, &#39;B&#39;, &#39;independent&#39;. | [optional] 
**current_reading** | **int** | A sensor type specific reading (RPM for fans, degrees celsius for temperature). | [optional] 
**display_name** | **str** | A human readable name for the sensor. | [optional] 
**location** | **str** | The location of this sensor. | [optional] 
**name** | **str** | A uniquely identifying name. | [optional] 
**state** | **str** | The current state of this sensor. Possible values: &#39;sensor_ok&#39;, &#39;sensor_alert_cond&#39;, &#39;sensor_missing&#39;, &#39;sensor_reading_unavail&#39;, &#39;sensor_failed&#39;. | [optional] 

## Example

```python
from dscc.models.nimble_ns_ctrlr_hw_sensor_info import NimbleNsCtrlrHwSensorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNsCtrlrHwSensorInfo from a JSON string
nimble_ns_ctrlr_hw_sensor_info_instance = NimbleNsCtrlrHwSensorInfo.from_json(json)
# print the JSON string representation of the object
print(NimbleNsCtrlrHwSensorInfo.to_json())

# convert the object into a dict
nimble_ns_ctrlr_hw_sensor_info_dict = nimble_ns_ctrlr_hw_sensor_info_instance.to_dict()
# create an instance of NimbleNsCtrlrHwSensorInfo from a dict
nimble_ns_ctrlr_hw_sensor_info_from_dict = NimbleNsCtrlrHwSensorInfo.from_dict(nimble_ns_ctrlr_hw_sensor_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


