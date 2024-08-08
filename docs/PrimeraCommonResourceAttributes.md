# PrimeraCommonResourceAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_state** | **str** | cloud connectivity status of the system where the resource belongs | [optional] 

## Example

```python
from dscc.models.primera_common_resource_attributes import PrimeraCommonResourceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of PrimeraCommonResourceAttributes from a JSON string
primera_common_resource_attributes_instance = PrimeraCommonResourceAttributes.from_json(json)
# print the JSON string representation of the object
print(PrimeraCommonResourceAttributes.to_json())

# convert the object into a dict
primera_common_resource_attributes_dict = primera_common_resource_attributes_instance.to_dict()
# create an instance of PrimeraCommonResourceAttributes from a dict
primera_common_resource_attributes_from_dict = PrimeraCommonResourceAttributes.from_dict(primera_common_resource_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


