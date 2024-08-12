# SnmpDetails

Snmp Details for a device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Snmp]**](Snmp.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | Number of snmp managers | [optional] 

## Example

```python
from dscc.models.snmp_details import SnmpDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpDetails from a JSON string
snmp_details_instance = SnmpDetails.from_json(json)
# print the JSON string representation of the object
print(SnmpDetails.to_json())

# convert the object into a dict
snmp_details_dict = snmp_details_instance.to_dict()
# create an instance of SnmpDetails from a dict
snmp_details_from_dict = SnmpDetails.from_dict(snmp_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


