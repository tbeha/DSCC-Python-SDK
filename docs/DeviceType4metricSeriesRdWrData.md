# DeviceType4metricSeriesRdWrData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the object at particular timestamp | [optional] 
**read_value** | **float** | average read metric value at particular timestamp | [optional] 
**timestampms** | **int** | epoch timestamp | [optional] 
**write_value** | **float** | average write metric value at particular timestamp | [optional] 

## Example

```python
from dscc.models.device_type4metric_series_rd_wr_data import DeviceType4metricSeriesRdWrData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4metricSeriesRdWrData from a JSON string
device_type4metric_series_rd_wr_data_instance = DeviceType4metricSeriesRdWrData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4metricSeriesRdWrData.to_json())

# convert the object into a dict
device_type4metric_series_rd_wr_data_dict = device_type4metric_series_rd_wr_data_instance.to_dict()
# create an instance of DeviceType4metricSeriesRdWrData from a dict
device_type4metric_series_rd_wr_data_from_dict = DeviceType4metricSeriesRdWrData.from_dict(device_type4metric_series_rd_wr_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


