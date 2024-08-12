# QospolicyDetails

QoS policy details for given time range for a device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qos_capped_objs_data** | [**CappedObjData**](CappedObjData.md) |  | [optional] 
**qos_un_capped_objs_data** | [**UncappedObjData**](UncappedObjData.md) |  | [optional] 
**recvd_total** | **int** | Total number of received QoS policy details for a device based on the given query parameters | [optional] 
**total** | **int** | Total number of QoS policy details for a device based on the given query parameters | [optional] 

## Example

```python
from dscc.models.qospolicy_details import QospolicyDetails

# TODO update the JSON string below
json = "{}"
# create an instance of QospolicyDetails from a JSON string
qospolicy_details_instance = QospolicyDetails.from_json(json)
# print the JSON string representation of the object
print(QospolicyDetails.to_json())

# convert the object into a dict
qospolicy_details_dict = qospolicy_details_instance.to_dict()
# create an instance of QospolicyDetails from a dict
qospolicy_details_from_dict = QospolicyDetails.from_dict(qospolicy_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


