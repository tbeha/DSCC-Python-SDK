# ReplicationPartnerFieldsWithFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id of the replication partner. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Name of the replication partner. &#x60;Filter, Sort&#x60; | [optional] 
**replication_partner_type** | **str** | Link protocol type. &#x60;Filter, Sort&#x60; | [optional] 
**status** | **str** | Status of the partner. Possible values - New, Ready, Unsupported, Failing, Failed or Disabled. &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.replication_partner_fields_with_filter import ReplicationPartnerFieldsWithFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationPartnerFieldsWithFilter from a JSON string
replication_partner_fields_with_filter_instance = ReplicationPartnerFieldsWithFilter.from_json(json)
# print the JSON string representation of the object
print(ReplicationPartnerFieldsWithFilter.to_json())

# convert the object into a dict
replication_partner_fields_with_filter_dict = replication_partner_fields_with_filter_instance.to_dict()
# create an instance of ReplicationPartnerFieldsWithFilter from a dict
replication_partner_fields_with_filter_from_dict = ReplicationPartnerFieldsWithFilter.from_dict(replication_partner_fields_with_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


