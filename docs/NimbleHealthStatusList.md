# NimbleHealthStatusList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleHealthStatusListItemsInner]**](NimbleHealthStatusListItemsInner.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for health status objects | [optional] 
**total** | **int** | Total number ofhealth checks. | [optional] 

## Example

```python
from dscc.models.nimble_health_status_list import NimbleHealthStatusList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleHealthStatusList from a JSON string
nimble_health_status_list_instance = NimbleHealthStatusList.from_json(json)
# print the JSON string representation of the object
print(NimbleHealthStatusList.to_json())

# convert the object into a dict
nimble_health_status_list_dict = nimble_health_status_list_instance.to_dict()
# create an instance of NimbleHealthStatusList from a dict
nimble_health_status_list_from_dict = NimbleHealthStatusList.from_dict(nimble_health_status_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


