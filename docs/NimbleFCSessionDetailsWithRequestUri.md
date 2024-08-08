# NimbleFCSessionDetailsWithRequestUri


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_uri** | **str** | requestUri for detailed Fibre Channel Session object | [optional] 
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
from dscc.models.nimble_fc_session_details_with_request_uri import NimbleFCSessionDetailsWithRequestUri

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleFCSessionDetailsWithRequestUri from a JSON string
nimble_fc_session_details_with_request_uri_instance = NimbleFCSessionDetailsWithRequestUri.from_json(json)
# print the JSON string representation of the object
print(NimbleFCSessionDetailsWithRequestUri.to_json())

# convert the object into a dict
nimble_fc_session_details_with_request_uri_dict = nimble_fc_session_details_with_request_uri_instance.to_dict()
# create an instance of NimbleFCSessionDetailsWithRequestUri from a dict
nimble_fc_session_details_with_request_uri_from_dict = NimbleFCSessionDetailsWithRequestUri.from_dict(nimble_fc_session_details_with_request_uri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


