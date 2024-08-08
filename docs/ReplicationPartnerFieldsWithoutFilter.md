# ReplicationPartnerFieldsWithoutFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id of the replication partner. | [optional] 
**name** | **str** | Name of the replication partner. | [optional] 
**replication_partner_type** | **str** | Link protocol type. | [optional] 
**status** | **str** | Status of the partner. Possible values - New, Ready, Unsupported, Failing, Failed or Disabled. | [optional] 

## Example

```python
from dscc.models.replication_partner_fields_without_filter import ReplicationPartnerFieldsWithoutFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationPartnerFieldsWithoutFilter from a JSON string
replication_partner_fields_without_filter_instance = ReplicationPartnerFieldsWithoutFilter.from_json(json)
# print the JSON string representation of the object
print(ReplicationPartnerFieldsWithoutFilter.to_json())

# convert the object into a dict
replication_partner_fields_without_filter_dict = replication_partner_fields_without_filter_instance.to_dict()
# create an instance of ReplicationPartnerFieldsWithoutFilter from a dict
replication_partner_fields_without_filter_from_dict = ReplicationPartnerFieldsWithoutFilter.from_dict(replication_partner_fields_without_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


