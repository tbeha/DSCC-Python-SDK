# NimbleFCConfigsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleFCConfigsListItemsInner]**](NimbleFCConfigsListItemsInner.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for  Fibre Channel Configs | [optional] 
**total** | **int** | Total number of Fibre Channel Configs. | [optional] 

## Example

```python
from dscc.models.nimble_fc_configs_list import NimbleFCConfigsList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleFCConfigsList from a JSON string
nimble_fc_configs_list_instance = NimbleFCConfigsList.from_json(json)
# print the JSON string representation of the object
print(NimbleFCConfigsList.to_json())

# convert the object into a dict
nimble_fc_configs_list_dict = nimble_fc_configs_list_instance.to_dict()
# create an instance of NimbleFCConfigsList from a dict
nimble_fc_configs_list_from_dict = NimbleFCConfigsList.from_dict(nimble_fc_configs_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


