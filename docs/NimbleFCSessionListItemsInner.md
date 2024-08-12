# NimbleFCSessionListItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the Fibre Channel session. A 42 digit hexadecimal number. | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**initiator_info** | [**NimbleFCInitiatorInfo**](NimbleFCInitiatorInfo.md) |  | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**sc_host_initiator_id** | **str** | Host Service Initiator Id | [optional] 
**target_info** | [**NimbleFCTargetInfo**](NimbleFCTargetInfo.md) |  | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.nimble_fc_session_list_items_inner import NimbleFCSessionListItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleFCSessionListItemsInner from a JSON string
nimble_fc_session_list_items_inner_instance = NimbleFCSessionListItemsInner.from_json(json)
# print the JSON string representation of the object
print(NimbleFCSessionListItemsInner.to_json())

# convert the object into a dict
nimble_fc_session_list_items_inner_dict = nimble_fc_session_list_items_inner_instance.to_dict()
# create an instance of NimbleFCSessionListItemsInner from a dict
nimble_fc_session_list_items_inner_from_dict = NimbleFCSessionListItemsInner.from_dict(nimble_fc_session_list_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


