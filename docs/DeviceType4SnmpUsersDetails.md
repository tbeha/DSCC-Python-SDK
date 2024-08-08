# DeviceType4SnmpUsersDetails

Get snmp users

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[DeviceType4AssociatedLinksInner]**](DeviceType4AssociatedLinksInner.md) | Associated Links Details | [optional] 
**authprotocol** | **str** | Specify the SNMP users authentication protocols. | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**privprotocol** | **str** | Specify the SNMP users privacy protocols. | [optional] 
**resource_uri** | **str** | resourceUri for detailed snmpUsers object | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**system_wwn** | **str** | WWN of the array | [optional] 
**type** | **str** | type | [optional] 
**username** | **str** | Specify the SNMPv3 user name | [optional] 

## Example

```python
from dscc.models.device_type4_snmp_users_details import DeviceType4SnmpUsersDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SnmpUsersDetails from a JSON string
device_type4_snmp_users_details_instance = DeviceType4SnmpUsersDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SnmpUsersDetails.to_json())

# convert the object into a dict
device_type4_snmp_users_details_dict = device_type4_snmp_users_details_instance.to_dict()
# create an instance of DeviceType4SnmpUsersDetails from a dict
device_type4_snmp_users_details_from_dict = DeviceType4SnmpUsersDetails.from_dict(device_type4_snmp_users_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


