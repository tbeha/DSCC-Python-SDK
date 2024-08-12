# PortISCSIPing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | IP Address to ping | [optional] 
**ip_addressv6** | **str** | IP Address to ping | [optional] 
**ping_count** | **int** | ping count | [optional] 

## Example

```python
from dscc.models.port_iscsi_ping import PortISCSIPing

# TODO update the JSON string below
json = "{}"
# create an instance of PortISCSIPing from a JSON string
port_iscsi_ping_instance = PortISCSIPing.from_json(json)
# print the JSON string representation of the object
print(PortISCSIPing.to_json())

# convert the object into a dict
port_iscsi_ping_dict = port_iscsi_ping_instance.to_dict()
# create an instance of PortISCSIPing from a dict
port_iscsi_ping_from_dict = PortISCSIPing.from_dict(port_iscsi_ping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


