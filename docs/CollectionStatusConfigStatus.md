# CollectionStatusConfigStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Hstatus**](Hstatus.md) |  | [optional] 

## Example

```python
from dscc.models.collection_status_config_status import CollectionStatusConfigStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionStatusConfigStatus from a JSON string
collection_status_config_status_instance = CollectionStatusConfigStatus.from_json(json)
# print the JSON string representation of the object
print(CollectionStatusConfigStatus.to_json())

# convert the object into a dict
collection_status_config_status_dict = collection_status_config_status_instance.to_dict()
# create an instance of CollectionStatusConfigStatus from a dict
collection_status_config_status_from_dict = CollectionStatusConfigStatus.from_dict(collection_status_config_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


