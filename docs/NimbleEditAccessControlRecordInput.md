# NimbleEditAccessControlRecordInput

Edit Nimble access-control record input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_to** | **str** | Type of object this access control record applies to. Possible values:&#39;volume&#39;, &#39;pe&#39;, &#39;vvol_volume&#39;, &#39;vvol_snapshot&#39;, &#39;snapshot&#39;, &#39;both&#39;. | [optional] 

## Example

```python
from dscc.models.nimble_edit_access_control_record_input import NimbleEditAccessControlRecordInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleEditAccessControlRecordInput from a JSON string
nimble_edit_access_control_record_input_instance = NimbleEditAccessControlRecordInput.from_json(json)
# print the JSON string representation of the object
print(NimbleEditAccessControlRecordInput.to_json())

# convert the object into a dict
nimble_edit_access_control_record_input_dict = nimble_edit_access_control_record_input_instance.to_dict()
# create an instance of NimbleEditAccessControlRecordInput from a dict
nimble_edit_access_control_record_input_from_dict = NimbleEditAccessControlRecordInput.from_dict(nimble_edit_access_control_record_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


