# NimbleMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Identifier of key-value pair. | [optional] 
**value** | **str** | Value of key-value pair. | [optional] 

## Example

```python
from dscc.models.nimble_metadata import NimbleMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleMetadata from a JSON string
nimble_metadata_instance = NimbleMetadata.from_json(json)
# print the JSON string representation of the object
print(NimbleMetadata.to_json())

# convert the object into a dict
nimble_metadata_dict = nimble_metadata_instance.to_dict()
# create an instance of NimbleMetadata from a dict
nimble_metadata_from_dict = NimbleMetadata.from_dict(nimble_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


