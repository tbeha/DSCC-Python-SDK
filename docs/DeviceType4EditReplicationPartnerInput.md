# DeviceType4EditReplicationPartnerInput

Request body to edit replication partner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_rc_links** | [**DeviceType4AddRemoteCopyLinks**](DeviceType4AddRemoteCopyLinks.md) |  | [optional] 
**remove_rc_links** | [**DeviceType4RemoveRemoteCopyLinksInput**](DeviceType4RemoveRemoteCopyLinksInput.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_edit_replication_partner_input import DeviceType4EditReplicationPartnerInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EditReplicationPartnerInput from a JSON string
device_type4_edit_replication_partner_input_instance = DeviceType4EditReplicationPartnerInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EditReplicationPartnerInput.to_json())

# convert the object into a dict
device_type4_edit_replication_partner_input_dict = device_type4_edit_replication_partner_input_instance.to_dict()
# create an instance of DeviceType4EditReplicationPartnerInput from a dict
device_type4_edit_replication_partner_input_from_dict = DeviceType4EditReplicationPartnerInput.from_dict(device_type4_edit_replication_partner_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


