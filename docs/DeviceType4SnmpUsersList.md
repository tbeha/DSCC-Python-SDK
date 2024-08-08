# DeviceType4SnmpUsersList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4SnmpUsersDetails]**](DeviceType4SnmpUsersDetails.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed nodes object | [optional] 
**total** | **int** | Number of Snmp Users | [optional] 

## Example

```python
from dscc.models.device_type4_snmp_users_list import DeviceType4SnmpUsersList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SnmpUsersList from a JSON string
device_type4_snmp_users_list_instance = DeviceType4SnmpUsersList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SnmpUsersList.to_json())

# convert the object into a dict
device_type4_snmp_users_list_dict = device_type4_snmp_users_list_instance.to_dict()
# create an instance of DeviceType4SnmpUsersList from a dict
device_type4_snmp_users_list_from_dict = DeviceType4SnmpUsersList.from_dict(device_type4_snmp_users_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


