# CollectionStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_status** | [**CollectionStatusConfigStatus**](CollectionStatusConfigStatus.md) |  | [optional] 
**metric_status** | [**CollectionStatusConfigStatus**](CollectionStatusConfigStatus.md) |  | [optional] 
**over_all_status** | [**Hstatus**](Hstatus.md) |  | [optional] 

## Example

```python
from dscc.models.collection_status import CollectionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionStatus from a JSON string
collection_status_instance = CollectionStatus.from_json(json)
# print the JSON string representation of the object
print(CollectionStatus.to_json())

# convert the object into a dict
collection_status_dict = collection_status_instance.to_dict()
# create an instance of CollectionStatus from a dict
collection_status_from_dict = CollectionStatus.from_dict(collection_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


