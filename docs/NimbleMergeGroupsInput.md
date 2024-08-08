# NimbleMergeGroupsInput

Perform group merge with the specified group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **bool** | Ignore warnings and forcibly merge specified group with this group. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**skip_secondary_mgmt_ip** | **bool** | Skip check for secondary management IP address. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**src_group_ip** | **str** | IP address of the source group. Four numbers in the range [0,255] separated by periods. Example: &#39;128.0.0.1&#39;. | 
**src_group_name** | **str** | Name of the source group. String of up to 64 alphanumeric characters, - is allowed after first character. Example: &#39;g1-exchange&#39;. | 
**src_passphrase** | **str** | Source group encryption passphrase. Encryption passphrase. String with size from 8 to 64 printable characters. Example: &#39;passphrase-91&#39;. | [optional] 
**src_password** | **str** | Password of the source group. String of 8 to 255 printable characters excluding ampersand and ;[]&#x60;. Example: &#39;password-91&#39;. | 
**src_username** | **str** | Username of the source group. String of up to 80 alphanumeric characters, beginning with a letter. For Active Directory users, it can include backslash (\\), dash (-), period (.), underscore (_) and space. Example: &#39;user1&#39;, &#39;companydomain\\user1&#39;. | 

## Example

```python
from dscc.models.nimble_merge_groups_input import NimbleMergeGroupsInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleMergeGroupsInput from a JSON string
nimble_merge_groups_input_instance = NimbleMergeGroupsInput.from_json(json)
# print the JSON string representation of the object
print(NimbleMergeGroupsInput.to_json())

# convert the object into a dict
nimble_merge_groups_input_dict = nimble_merge_groups_input_instance.to_dict()
# create an instance of NimbleMergeGroupsInput from a dict
nimble_merge_groups_input_from_dict = NimbleMergeGroupsInput.from_dict(nimble_merge_groups_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


