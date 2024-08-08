# SystemDetails

System and Resource Details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **str** |  | [optional] 
**system_uri** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from dscc.models.system_details import SystemDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SystemDetails from a JSON string
system_details_instance = SystemDetails.from_json(json)
# print the JSON string representation of the object
print(SystemDetails.to_json())

# convert the object into a dict
system_details_dict = system_details_instance.to_dict()
# create an instance of SystemDetails from a dict
system_details_from_dict = SystemDetails.from_dict(system_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


