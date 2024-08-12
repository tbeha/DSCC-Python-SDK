# CreateHostGroupInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment | [optional] 
**host_ids** | **List[str]** | List of host ids of existing hosts | [optional] 
**hosts_to_create** | [**List[CreateHostInput]**](CreateHostInput.md) | List of hosts to be created and added to this hostGroup | [optional] 
**name** | **str** | Name of the host group | 
**user_created** | **bool** | Indicates whether user created host group or discovered host group. value should always be set as \&quot;true\&quot;. API will internally override the passed value to set it as \&quot;true\&quot;. | [optional] 

## Example

```python
from dscc.models.create_host_group_input import CreateHostGroupInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHostGroupInput from a JSON string
create_host_group_input_instance = CreateHostGroupInput.from_json(json)
# print the JSON string representation of the object
print(CreateHostGroupInput.to_json())

# convert the object into a dict
create_host_group_input_dict = create_host_group_input_instance.to_dict()
# create an instance of CreateHostGroupInput from a dict
create_host_group_input_from_dict = CreateHostGroupInput.from_dict(create_host_group_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


