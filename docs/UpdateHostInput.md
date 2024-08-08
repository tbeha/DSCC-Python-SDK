# UpdateHostInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiators_to_create** | [**List[InitiatorInput]**](InitiatorInput.md) | List of initiators to be created and added to this host | [optional] 
**name** | **str** | Name of the host. | [optional] 
**updated_initiators** | **List[str]** | List of existing initiator IDs to be replaced to the host | [optional] 

## Example

```python
from dscc.models.update_host_input import UpdateHostInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHostInput from a JSON string
update_host_input_instance = UpdateHostInput.from_json(json)
# print the JSON string representation of the object
print(UpdateHostInput.to_json())

# convert the object into a dict
update_host_input_dict = update_host_input_instance.to_dict()
# create an instance of UpdateHostInput from a dict
update_host_input_from_dict = UpdateHostInput.from_dict(update_host_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


