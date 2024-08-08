# Applications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_set_type** | **str** | Name of the application | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**total_size_mi_b** | **float** | The total volume size in MiB of the application | [optional] 
**total_used_size_mi_b** | **float** | The total used size in Mib of the application | [optional] 
**volumes_count** | **int** | The number of volumes in an application | [optional] 

## Example

```python
from dscc.models.applications import Applications

# TODO update the JSON string below
json = "{}"
# create an instance of Applications from a JSON string
applications_instance = Applications.from_json(json)
# print the JSON string representation of the object
print(Applications.to_json())

# convert the object into a dict
applications_dict = applications_instance.to_dict()
# create an instance of Applications from a dict
applications_from_dict = Applications.from_dict(applications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


