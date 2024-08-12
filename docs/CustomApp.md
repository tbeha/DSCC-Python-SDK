# CustomApp

Params required to create custom workload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compression** | **bool** | is compression required | [optional] 
**deduplication** | **bool** | is deduplication required | [optional] 
**name** | **str** | Name of policy | [optional] 

## Example

```python
from dscc.models.custom_app import CustomApp

# TODO update the JSON string below
json = "{}"
# create an instance of CustomApp from a JSON string
custom_app_instance = CustomApp.from_json(json)
# print the JSON string representation of the object
print(CustomApp.to_json())

# convert the object into a dict
custom_app_dict = custom_app_instance.to_dict()
# create an instance of CustomApp from a dict
custom_app_from_dict = CustomApp.from_dict(custom_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


