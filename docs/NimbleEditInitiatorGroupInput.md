# NimbleEditInitiatorGroupInput

Edit Nimble initiator group input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_uuid** | **str** | Application identifier of initiator group. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed. | [optional] 
**description** | **str** | Text description of initiator group. String of up to 255 printable ASCII characters. | [optional] 
**fc_initiators** | [**List[NimbleFCInitiator]**](NimbleFCInitiator.md) | List of FC initiators. When create/update fc_initiators, wwpn is required. List of Fibre Channel initiators. | [optional] 
**fc_tdz_ports** | [**List[NimbleFCTdzPorts]**](NimbleFCTdzPorts.md) | List of target Fibre Channel ports with Target Driven Zoning configured on this initiator group. List of target ports. | [optional] 
**host_type** | **str** | Initiator group host type. Available options are auto and hpux. The default option is auto. This attribute will be applied to all the initiators in the initiator group. Initiators with different host OSes should not be kept in the same initiator group having a non-default host type attribute. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**iscsi_initiators** | [**List[NimbleISCSIInitiator]**](NimbleISCSIInitiator.md) | List of iSCSI initiators. When create/update iscsi_initiators, either iqn or ip_address is always required with label. | [optional] 
**metadata** | [**List[NimbleMetadata]**](NimbleMetadata.md) | Key-value pairs that augment an initiator group&#39;s attributes. | [optional] 
**name** | **str** | Name of initiator group. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**target_subnets** | [**List[NimbleTargetSubnets]**](NimbleTargetSubnets.md) | List of target subnet labels. If specified, discovery and access to volumes will be restricted to to the specified subnets. List of target subnet tables. | [optional] 

## Example

```python
from dscc.models.nimble_edit_initiator_group_input import NimbleEditInitiatorGroupInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleEditInitiatorGroupInput from a JSON string
nimble_edit_initiator_group_input_instance = NimbleEditInitiatorGroupInput.from_json(json)
# print the JSON string representation of the object
print(NimbleEditInitiatorGroupInput.to_json())

# convert the object into a dict
nimble_edit_initiator_group_input_dict = nimble_edit_initiator_group_input_instance.to_dict()
# create an instance of NimbleEditInitiatorGroupInput from a dict
nimble_edit_initiator_group_input_from_dict = NimbleEditInitiatorGroupInput.from_dict(nimble_edit_initiator_group_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


