# NimbleEditDiskInput

Edit Nimble / Alletra 6K disk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_op** | **str** | The intended operation to be performed on the specified disk. Disk operation. Possible values: &#39;add&#39;, &#39;remove&#39;. | [optional] 
**force** | **bool** | Forcibly add a disk. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 

## Example

```python
from dscc.models.nimble_edit_disk_input import NimbleEditDiskInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleEditDiskInput from a JSON string
nimble_edit_disk_input_instance = NimbleEditDiskInput.from_json(json)
# print the JSON string representation of the object
print(NimbleEditDiskInput.to_json())

# convert the object into a dict
nimble_edit_disk_input_dict = nimble_edit_disk_input_instance.to_dict()
# create an instance of NimbleEditDiskInput from a dict
nimble_edit_disk_input_from_dict = NimbleEditDiskInput.from_dict(nimble_edit_disk_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


