# QosPolicy

qos policy details for given time range

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qospolicy_details** | [**QospolicyDetails**](QospolicyDetails.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 

## Example

```python
from dscc.models.qos_policy import QosPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of QosPolicy from a JSON string
qos_policy_instance = QosPolicy.from_json(json)
# print the JSON string representation of the object
print(QosPolicy.to_json())

# convert the object into a dict
qos_policy_dict = qos_policy_instance.to_dict()
# create an instance of QosPolicy from a dict
qos_policy_from_dict = QosPolicy.from_dict(qos_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


