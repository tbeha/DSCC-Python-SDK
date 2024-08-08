# EditReplicationPartnerInput

Request body to edit replication partner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_rc_links** | [**AddRemoteCopyLinks**](AddRemoteCopyLinks.md) |  | [optional] 
**remove_rc_links** | [**RemoveRemoteCopyLinksInput**](RemoveRemoteCopyLinksInput.md) |  | [optional] 

## Example

```python
from dscc.models.edit_replication_partner_input import EditReplicationPartnerInput

# TODO update the JSON string below
json = "{}"
# create an instance of EditReplicationPartnerInput from a JSON string
edit_replication_partner_input_instance = EditReplicationPartnerInput.from_json(json)
# print the JSON string representation of the object
print(EditReplicationPartnerInput.to_json())

# convert the object into a dict
edit_replication_partner_input_dict = edit_replication_partner_input_instance.to_dict()
# create an instance of EditReplicationPartnerInput from a dict
edit_replication_partner_input_from_dict = EditReplicationPartnerInput.from_dict(edit_replication_partner_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


