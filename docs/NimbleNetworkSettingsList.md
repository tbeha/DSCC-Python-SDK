# NimbleNetworkSettingsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleNetworkSettingsListItemsInner]**](NimbleNetworkSettingsListItemsInner.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for network setting objects | [optional] 
**total** | **int** | Total number of network settings. | [optional] 

## Example

```python
from dscc.models.nimble_network_settings_list import NimbleNetworkSettingsList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNetworkSettingsList from a JSON string
nimble_network_settings_list_instance = NimbleNetworkSettingsList.from_json(json)
# print the JSON string representation of the object
print(NimbleNetworkSettingsList.to_json())

# convert the object into a dict
nimble_network_settings_list_dict = nimble_network_settings_list_instance.to_dict()
# create an instance of NimbleNetworkSettingsList from a dict
nimble_network_settings_list_from_dict = NimbleNetworkSettingsList.from_dict(nimble_network_settings_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


