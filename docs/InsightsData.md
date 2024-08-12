# InsightsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Category of the insight | [optional] 
**cause** | **str** |  | [optional] 
**create_time** | **int** | Timestamp for the insight. | [optional] 
**var_date** | **date** | Date in string format corresponding to the timestamp field. | [optional] 
**details** | [**InsightDetails**](InsightDetails.md) |  | [optional] 
**id** | **str** | Primary identifier for the insight. | [optional] 
**insight_details_uri** | **str** | URI of the insight details page | [optional] 
**insight_uri** | **str** | URI of the insight | [optional] 
**last_updated_time** | **int** |  | [optional] 
**remediation** | **str** |  | [optional] 
**resource_details** | [**ResourceDetail**](ResourceDetail.md) |  | [optional] 
**score** | **int** | Score of the insight - 0,1,2...10 | [optional] 
**severity** | **str** | Severity of the insight - CRITICAL, INFO, WARNING | [optional] 
**state** | **str** |  | [optional] 
**sub_type** | **str** | Sub-type of the insight (eg. DISK/CPU) | [optional] 
**symptom** | **str** |  | [optional] 
**system_details** | [**SystemDetails**](SystemDetails.md) |  | [optional] 
**system_id** | **str** | Identifier of the system | [optional] 
**tenant_id** | **str** | Primary identifier for the customer (UUID) associated with the insight | [optional] 
**title** | **str** | One line description of the insight | [optional] 
**type** | **str** | Type of the insight | [optional] 
**value** | **float** | insight values - No. of annotations, saturation value | [optional] 

## Example

```python
from dscc.models.insights_data import InsightsData

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsData from a JSON string
insights_data_instance = InsightsData.from_json(json)
# print the JSON string representation of the object
print(InsightsData.to_json())

# convert the object into a dict
insights_data_dict = insights_data_instance.to_dict()
# create an instance of InsightsData from a dict
insights_data_from_dict = InsightsData.from_dict(insights_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


