# Source

Source partner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | IP address or hostname of partner interface. This must be the partner&#39;s Group Management IP address. String of up to 64 alphanumeric characters, - and . and colon are allowed after first character. | 
**name** | **str** | Name of the replication partner. String of up to 63 alphanumeric and can include hyphens characters but cannot start with hyphen. | 
**subnet_label** | **str** | Label of the subnet used to replicate to this partner. String of up to 64 alphanumeric characters, - and . and colon are allowed after first character. | 
**subnet_type** | **str** | Type of the subnet used to replicate to this partner. Possible values are &#39;invalid&#39;, &#39;unconfigured&#39;, &#39;mgmt&#39;, &#39;data&#39;, &#39;mgmt_data&#39;. | [optional] 

## Example

```python
from dscc.models.source import Source

# TODO update the JSON string below
json = "{}"
# create an instance of Source from a JSON string
source_instance = Source.from_json(json)
# print the JSON string representation of the object
print(Source.to_json())

# convert the object into a dict
source_dict = source_instance.to_dict()
# create an instance of Source from a dict
source_from_dict = Source.from_dict(source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


