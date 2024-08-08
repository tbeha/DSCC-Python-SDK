# RemoveReplicationPartnersInput

Request body for deleting replication partner pairs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partners** | [**List[RemoveRemoteCopyTargetInput]**](RemoveRemoteCopyTargetInput.md) | List of replication partner pairs to be deleted | 

## Example

```python
from dscc.models.remove_replication_partners_input import RemoveReplicationPartnersInput

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveReplicationPartnersInput from a JSON string
remove_replication_partners_input_instance = RemoveReplicationPartnersInput.from_json(json)
# print the JSON string representation of the object
print(RemoveReplicationPartnersInput.to_json())

# convert the object into a dict
remove_replication_partners_input_dict = remove_replication_partners_input_instance.to_dict()
# create an instance of RemoveReplicationPartnersInput from a dict
remove_replication_partners_input_from_dict = RemoveReplicationPartnersInput.from_dict(remove_replication_partners_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


