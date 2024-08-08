# Descriptors

System descriptors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | CommeUser-specified comment for the system | [optional] 
**contact** | **str** | User-specified contact for the system | [optional] 
**location** | **str** | User-specified location of the system | [optional] 
**owner** | **str** | User-specified owner for the system | [optional] 

## Example

```python
from dscc.models.descriptors import Descriptors

# TODO update the JSON string below
json = "{}"
# create an instance of Descriptors from a JSON string
descriptors_instance = Descriptors.from_json(json)
# print the JSON string representation of the object
print(Descriptors.to_json())

# convert the object into a dict
descriptors_dict = descriptors_instance.to_dict()
# create an instance of Descriptors from a dict
descriptors_from_dict = Descriptors.from_dict(descriptors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


