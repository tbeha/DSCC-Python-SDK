# HostStorageVolumes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[HostVolumes]**](HostVolumes.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed object | [optional] 
**total** | **int** | Number of volume count for the host. | [optional] 

## Example

```python
from dscc.models.host_storage_volumes import HostStorageVolumes

# TODO update the JSON string below
json = "{}"
# create an instance of HostStorageVolumes from a JSON string
host_storage_volumes_instance = HostStorageVolumes.from_json(json)
# print the JSON string representation of the object
print(HostStorageVolumes.to_json())

# convert the object into a dict
host_storage_volumes_dict = host_storage_volumes_instance.to_dict()
# create an instance of HostStorageVolumes from a dict
host_storage_volumes_from_dict = HostStorageVolumes.from_dict(host_storage_volumes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


