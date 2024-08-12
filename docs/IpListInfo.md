# IpListInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | Associated ip address | [optional] 
**vlan_id** | **int** | vlan id. | [optional] 

## Example

```python
from dscc.models.ip_list_info import IpListInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IpListInfo from a JSON string
ip_list_info_instance = IpListInfo.from_json(json)
# print the JSON string representation of the object
print(IpListInfo.to_json())

# convert the object into a dict
ip_list_info_dict = ip_list_info_instance.to_dict()
# create an instance of IpListInfo from a dict
ip_list_info_from_dict = IpListInfo.from_dict(ip_list_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


