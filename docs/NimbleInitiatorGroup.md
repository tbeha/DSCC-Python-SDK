# NimbleInitiatorGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_protocol** | **str** | Initiator group access protocol. Possible values: &#39;iscsi&#39;, &#39;fc&#39;.&#x60;Filter, Sort&#x60; | [optional] 
**app_uuid** | **str** | Application identifier of initiator group. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed.&#x60;Filter, Sort&#x60; | [optional] 
**host_type** | **str** | Initiator group host type. Available options are auto and hpux. The default option is auto. This attribute will be applied to all the initiators in the initiator group. Initiators with different host OSes should not be kept in the same initiator group having a non-default host type attribute. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Identifier for initiator group. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Name of initiator group. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.&#x60;Filter, Sort&#x60; | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**creation_time** | **int** | Time when this initiator group was created. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**customer_id** | **str** | customerId | [optional] 
**description** | **str** | Text description of initiator group. String of up to 255 printable ASCII characters. | [optional] 
**fc_initiators** | [**List[NimbleFCInitiator]**](NimbleFCInitiator.md) | List of FC initiators. When create/update fc_initiators, wwpn is required. List of Fibre Channel initiators. | [optional] 
**fc_sessions** | [**List[NimbleFCSessionDetails]**](NimbleFCSessionDetails.md) | List of FC sessions. | [optional] 
**fc_tdz_ports** | [**List[NimbleFCTdzPorts]**](NimbleFCTdzPorts.md) | List of target Fibre Channel ports with Target Driven Zoning configured on this initiator group. | [optional] 
**full_name** | **str** | Initiator group&#39;s full name. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**iscsi_initiators** | [**List[NimbleISCSIInitiator]**](NimbleISCSIInitiator.md) | List of ISCSI initiators. When create/update iscsi_initiators, either iqn or ip_address is always required with label. | [optional] 
**last_modified** | **int** | Time when this initiator group was last modified. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**metadata** | [**List[NimbleMetadata]**](NimbleMetadata.md) | Key-value pairs that augment an initiator group&#39;s attributes. | [optional] 
**num_connections** | **int** | Total number of connections from initiators in the initiator group. (This field is deprecated) | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**sc_host_id** | **str** | Host Service Host Id | [optional] 
**search_name** | **str** | Initiator group name used for search. Alphanumeric string, up to 64 characters including hyphen, period, colon. | [optional] 
**target_subnets** | [**List[NimbleTargetSubnets]**](NimbleTargetSubnets.md) | List of target subnet labels. If specified, discovery and access to volumes will be restricted to the specified subnets. List of target subnet tables. | [optional] 
**type** | **str** | The type of resource | [optional] 
**volume_count** | **int** | Number of volumes that are accessible by the initiator group. (This field is deprecated) | [optional] 
**volume_list** | [**List[NimbleVolList]**](NimbleVolList.md) | List of volumes that are accessible by the initiator group. List of volumes. (This field is deprecated) | [optional] 

## Example

```python
from dscc.models.nimble_initiator_group import NimbleInitiatorGroup

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleInitiatorGroup from a JSON string
nimble_initiator_group_instance = NimbleInitiatorGroup.from_json(json)
# print the JSON string representation of the object
print(NimbleInitiatorGroup.to_json())

# convert the object into a dict
nimble_initiator_group_dict = nimble_initiator_group_instance.to_dict()
# create an instance of NimbleInitiatorGroup from a dict
nimble_initiator_group_from_dict = NimbleInitiatorGroup.from_dict(nimble_initiator_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


