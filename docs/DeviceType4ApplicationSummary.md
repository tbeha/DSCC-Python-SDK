# DeviceType4ApplicationSummary

Application summary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**items** | [**List[DeviceType4applications]**](DeviceType4applications.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**total** | **int** | Number of node Cards. | [optional] 

## Example

```python
from dscc.models.device_type4_application_summary import DeviceType4ApplicationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ApplicationSummary from a JSON string
device_type4_application_summary_instance = DeviceType4ApplicationSummary.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ApplicationSummary.to_json())

# convert the object into a dict
device_type4_application_summary_dict = device_type4_application_summary_instance.to_dict()
# create an instance of DeviceType4ApplicationSummary from a dict
device_type4_application_summary_from_dict = DeviceType4ApplicationSummary.from_dict(device_type4_application_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


