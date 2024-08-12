# NimblefibreChannelConfigsWithRequestUri


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_uri** | **str** | requestUri for detailed fibre channel configs object | [optional] 
**group_leader_array** | **str** | Name of the group leader array. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**id** | **str** | Identifier for the array. A 42 digit hexadecimal number. | [optional] 
**array_list** | [**List[NimbleArraysList]**](NimbleArraysList.md) | List of array Fibre Channel configs. List of array Fibre Channel configurations. | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**controller_name** | **str** | Name (A or B) of the controller where the interface is hosted. Plain string. | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.nimblefibre_channel_configs_with_request_uri import NimblefibreChannelConfigsWithRequestUri

# TODO update the JSON string below
json = "{}"
# create an instance of NimblefibreChannelConfigsWithRequestUri from a JSON string
nimblefibre_channel_configs_with_request_uri_instance = NimblefibreChannelConfigsWithRequestUri.from_json(json)
# print the JSON string representation of the object
print(NimblefibreChannelConfigsWithRequestUri.to_json())

# convert the object into a dict
nimblefibre_channel_configs_with_request_uri_dict = nimblefibre_channel_configs_with_request_uri_instance.to_dict()
# create an instance of NimblefibreChannelConfigsWithRequestUri from a dict
nimblefibre_channel_configs_with_request_uri_from_dict = NimblefibreChannelConfigsWithRequestUri.from_dict(nimblefibre_channel_configs_with_request_uri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


