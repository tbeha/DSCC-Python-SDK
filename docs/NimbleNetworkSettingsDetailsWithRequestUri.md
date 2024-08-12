# NimbleNetworkSettingsDetailsWithRequestUri


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_uri** | **str** | requestUri for detailed network setting object | [optional] 
**id** | **str** | Identifier for network settings. | [optional] 
**name** | **str** | Name of the network configuration. Possible values: &#39;active&#39;, &#39;backup&#39;, &#39;draft&#39; | [optional] 
**role** | **str** | Role of network configuration. Possible values: &#39;active&#39;, &#39;backup&#39;, &#39;draft&#39; | [optional] 
**active_since** | **int** | Start time of activity. | [optional] 
**array_list** | [**List[NimbleArrayNet]**](NimbleArrayNet.md) | List of array network configs. | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**creation_time** | **int** | Time when this net configuration was created. | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**group_leader_array** | **str** | Name of the group leader array. | [optional] 
**iscsi_automatic_connection_method** | **bool** | Indicates whether automatic connection method is enabled. | [optional] 
**iscsi_connection_rebalancing** | **bool** | Indicates whether rebalancing is enabled. | [optional] 
**last_active** | **int** | Time of last activity. | [optional] 
**last_modified** | **int** | Time when this network configuration was last modified. | [optional] 
**mgmt_ip** | **str** | Management IP address for the Group. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**route_list** | [**List[NimbleRoute]**](NimbleRoute.md) | List of static routes. | [optional] 
**secondary_mgmt_ip** | **str** | Secondary management IP address for the Group. | [optional] 
**subnet_list** | [**List[NimbleSubnet]**](NimbleSubnet.md) | List of subnet configs. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.nimble_network_settings_details_with_request_uri import NimbleNetworkSettingsDetailsWithRequestUri

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNetworkSettingsDetailsWithRequestUri from a JSON string
nimble_network_settings_details_with_request_uri_instance = NimbleNetworkSettingsDetailsWithRequestUri.from_json(json)
# print the JSON string representation of the object
print(NimbleNetworkSettingsDetailsWithRequestUri.to_json())

# convert the object into a dict
nimble_network_settings_details_with_request_uri_dict = nimble_network_settings_details_with_request_uri_instance.to_dict()
# create an instance of NimbleNetworkSettingsDetailsWithRequestUri from a dict
nimble_network_settings_details_with_request_uri_from_dict = NimbleNetworkSettingsDetailsWithRequestUri.from_dict(nimble_network_settings_details_with_request_uri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


