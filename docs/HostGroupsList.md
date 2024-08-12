# HostGroupsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[HostGroupObject]**](HostGroupObject.md) |  | [optional] 
**page_limit** | **int** | Page Limit | [optional] 
**page_offset** | **int** | Page Offset | [optional] 
**request_uri** | **str** | requestUri for host initiator groups | [optional] 
**total** | **int** | Number of hosts | [optional] 

## Example

```python
from dscc.models.host_groups_list import HostGroupsList

# TODO update the JSON string below
json = "{}"
# create an instance of HostGroupsList from a JSON string
host_groups_list_instance = HostGroupsList.from_json(json)
# print the JSON string representation of the object
print(HostGroupsList.to_json())

# convert the object into a dict
host_groups_list_dict = host_groups_list_instance.to_dict()
# create an instance of HostGroupsList from a dict
host_groups_list_from_dict = HostGroupsList.from_dict(host_groups_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


