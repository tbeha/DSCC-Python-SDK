# EditSourcePartner

Source partner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | IP address or hostname of partner interface. This must be the partner&#39;s Group Management IP address. String of up to 64 alphanumeric characters, - and . and colon are allowed after first character. | [optional] 
**name** | **str** | Name of the replication partner. String of up to 63 alphanumeric and can include hyphens characters but cannot start with hyphen. | [optional] 
**subnet_label** | **str** | Label of the subnet used to replicate to this partner. String of up to 64 alphanumeric characters, - and . and colon are allowed after first character. | [optional] 
**subnet_type** | **str** | Type of the subnet used to replicate to this partner. Possible values are &#39;invalid&#39;, &#39;unconfigured&#39;, &#39;mgmt&#39;, &#39;data&#39;, &#39;mgmt_data&#39;. | [optional] 

## Example

```python
from dscc.models.edit_source_partner import EditSourcePartner

# TODO update the JSON string below
json = "{}"
# create an instance of EditSourcePartner from a JSON string
edit_source_partner_instance = EditSourcePartner.from_json(json)
# print the JSON string representation of the object
print(EditSourcePartner.to_json())

# convert the object into a dict
edit_source_partner_dict = edit_source_partner_instance.to_dict()
# create an instance of EditSourcePartner from a dict
edit_source_partner_from_dict = EditSourcePartner.from_dict(edit_source_partner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


