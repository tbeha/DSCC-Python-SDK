# DeviceType4snmpDetails

Snmp Details for a device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4snmp]**](DeviceType4snmp.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | Number of snmp managers | [optional] 

## Example

```python
from dscc.models.device_type4snmp_details import DeviceType4snmpDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4snmpDetails from a JSON string
device_type4snmp_details_instance = DeviceType4snmpDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4snmpDetails.to_json())

# convert the object into a dict
device_type4snmp_details_dict = device_type4snmp_details_instance.to_dict()
# create an instance of DeviceType4snmpDetails from a dict
device_type4snmp_details_from_dict = DeviceType4snmpDetails.from_dict(device_type4snmp_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


