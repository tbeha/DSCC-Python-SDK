# DeviceType4onlineClone

Online clone of a volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_lun** | **bool** | Specify to use auto lun number. | [optional] 
**destination_cpg** | **str** | Name of the User CPG | [optional] 
**host_group_id** | **str** | Unique identifier of host group. | [optional] 
**lun** | **int** | LUN of volume. | [optional] 
**nvme_transport_type** | **str** | Transport type of the protocol. Configuration of the transport type is only supported for NVMe protocol starting from the system OS version 10.3.0 and the default transport type value is FC. | [optional] 

## Example

```python
from dscc.models.device_type4online_clone import DeviceType4onlineClone

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4onlineClone from a JSON string
device_type4online_clone_instance = DeviceType4onlineClone.from_json(json)
# print the JSON string representation of the object
print(DeviceType4onlineClone.to_json())

# convert the object into a dict
device_type4online_clone_dict = device_type4online_clone_instance.to_dict()
# create an instance of DeviceType4onlineClone from a dict
device_type4online_clone_from_dict = DeviceType4onlineClone.from_dict(device_type4online_clone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


