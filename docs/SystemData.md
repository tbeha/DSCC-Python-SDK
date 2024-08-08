# SystemData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headroom** | **float** | headroom utilized on system | [optional] 
**headroom_utilised** | **str** | headroom utilized in terms of Low/Medium/High | [optional] 

## Example

```python
from dscc.models.system_data import SystemData

# TODO update the JSON string below
json = "{}"
# create an instance of SystemData from a JSON string
system_data_instance = SystemData.from_json(json)
# print the JSON string representation of the object
print(SystemData.to_json())

# convert the object into a dict
system_data_dict = system_data_instance.to_dict()
# create an instance of SystemData from a dict
system_data_from_dict = SystemData.from_dict(system_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


