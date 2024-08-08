# UpdateHostGroupInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_proximity_values** | [**List[HostProximityValue]**](HostProximityValue.md) | Change Proximity for list of hosts | [optional] 
**hosts_to_create** | [**List[CreateHostInput]**](CreateHostInput.md) | List of hosts to be replaced to the group | [optional] 
**name** | **str** | Name of the host group | [optional] 
**removed_hosts** | **List[Optional[str]]** | List of host IDs to be removed from the group | [optional] 
**updated_hosts** | **List[Optional[str]]** | List of host IDs to be added to the group | [optional] 

## Example

```python
from dscc.models.update_host_group_input import UpdateHostGroupInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHostGroupInput from a JSON string
update_host_group_input_instance = UpdateHostGroupInput.from_json(json)
# print the JSON string representation of the object
print(UpdateHostGroupInput.to_json())

# convert the object into a dict
update_host_group_input_dict = update_host_group_input_instance.to_dict()
# create an instance of UpdateHostGroupInput from a dict
update_host_group_input_from_dict = UpdateHostGroupInput.from_dict(update_host_group_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


