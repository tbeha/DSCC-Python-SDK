# UpdateHostChapInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[HostChapInputObject]**](HostChapInputObject.md) |  | [optional] 

## Example

```python
from dscc.models.update_host_chap_input import UpdateHostChapInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHostChapInput from a JSON string
update_host_chap_input_instance = UpdateHostChapInput.from_json(json)
# print the JSON string representation of the object
print(UpdateHostChapInput.to_json())

# convert the object into a dict
update_host_chap_input_dict = update_host_chap_input_instance.to_dict()
# create an instance of UpdateHostChapInput from a dict
update_host_chap_input_from_dict = UpdateHostChapInput.from_dict(update_host_chap_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


