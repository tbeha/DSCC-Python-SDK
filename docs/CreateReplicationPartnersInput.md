# CreateReplicationPartnersInput

Request body to create replication partners

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partners** | [**List[ReplicationPartnerInput]**](ReplicationPartnerInput.md) |  | 

## Example

```python
from dscc.models.create_replication_partners_input import CreateReplicationPartnersInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReplicationPartnersInput from a JSON string
create_replication_partners_input_instance = CreateReplicationPartnersInput.from_json(json)
# print the JSON string representation of the object
print(CreateReplicationPartnersInput.to_json())

# convert the object into a dict
create_replication_partners_input_dict = create_replication_partners_input_instance.to_dict()
# create an instance of CreateReplicationPartnersInput from a dict
create_replication_partners_input_from_dict = CreateReplicationPartnersInput.from_dict(create_replication_partners_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


