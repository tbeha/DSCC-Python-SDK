# NimbleCommonResourceAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_state** | **str** | Cloud connectivity status of the system where the resource belongs | [optional] 

## Example

```python
from dscc.models.nimble_common_resource_attributes import NimbleCommonResourceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleCommonResourceAttributes from a JSON string
nimble_common_resource_attributes_instance = NimbleCommonResourceAttributes.from_json(json)
# print the JSON string representation of the object
print(NimbleCommonResourceAttributes.to_json())

# convert the object into a dict
nimble_common_resource_attributes_dict = nimble_common_resource_attributes_instance.to_dict()
# create an instance of NimbleCommonResourceAttributes from a dict
nimble_common_resource_attributes_from_dict = NimbleCommonResourceAttributes.from_dict(nimble_common_resource_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


