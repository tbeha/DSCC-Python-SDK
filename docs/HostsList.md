# HostsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[HostObject]**](HostObject.md) |  | [optional] 
**page_limit** | **int** | Page Limit | [optional] 
**page_offset** | **int** | Page Offset | [optional] 
**request_uri** | **str** | requestUri for host initiators | [optional] 
**total** | **int** | Number of hosts | [optional] 

## Example

```python
from dscc.models.hosts_list import HostsList

# TODO update the JSON string below
json = "{}"
# create an instance of HostsList from a JSON string
hosts_list_instance = HostsList.from_json(json)
# print the JSON string representation of the object
print(HostsList.to_json())

# convert the object into a dict
hosts_list_dict = hosts_list_instance.to_dict()
# create an instance of HostsList from a dict
hosts_list_from_dict = HostsList.from_dict(hosts_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


