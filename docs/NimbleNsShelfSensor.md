# NimbleNsShelfSensor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cid** | **str** | Which controller this sensor applies to. Possible values:&#39;A&#39;, &#39;B&#39;, &#39;unknown&#39;. | [optional] 
**display_name** | **str** | Name for display purpose. | [optional] 
**location** | **str** | Location of the sensor. | [optional] 
**name** | **str** | Internal name of the sensor. | [optional] 
**status** | **str** | Sensor status. Possible values:&#39;Missing&#39;, &#39;Failed&#39;, &#39;OK&#39;, &#39;Alerted&#39;. | [optional] 
**type** | **str** | Type of the sensor. Possible values:&#39;fan&#39;, &#39;nvram&#39;, &#39;temperature&#39;, &#39;power supply&#39;. | [optional] 
**value** | **int** | Value of the sensor reading. | [optional] 

## Example

```python
from dscc.models.nimble_ns_shelf_sensor import NimbleNsShelfSensor

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNsShelfSensor from a JSON string
nimble_ns_shelf_sensor_instance = NimbleNsShelfSensor.from_json(json)
# print the JSON string representation of the object
print(NimbleNsShelfSensor.to_json())

# convert the object into a dict
nimble_ns_shelf_sensor_dict = nimble_ns_shelf_sensor_instance.to_dict()
# create an instance of NimbleNsShelfSensor from a dict
nimble_ns_shelf_sensor_from_dict = NimbleNsShelfSensor.from_dict(nimble_ns_shelf_sensor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


