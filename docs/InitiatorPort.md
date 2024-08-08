# InitiatorPort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | **str** | Initiator port alias | [optional] 
**current_speed** | **str** | Initiator port current | [optional] 
**hba_driver_version** | **str** | Initiator port hba driver version | [optional] 
**hba_firmware_version** | **str** | Initiator port hba firmware version | [optional] 
**hba_manufacturer** | **str** | Initiator port hba manufacturer | [optional] 
**hba_model** | **str** | Initiator port hba model | [optional] 
**hba_os_name_version** | **str** | Initiator port hba os version | [optional] 
**host_name** | **str** | Initiator port host name | [optional] 
**number** | **int** | Initiator port number | [optional] 
**os_device_name** | **str** | Initiator port os device name | [optional] 
**ssan_qos_support** | **str** | Initiator port Smart SAN qos support | [optional] 
**ssan_security_support** | **str** | Initiator port Smart SAN security | [optional] 
**supported_speeds** | **str** | Initiator port supported speeds | [optional] 
**wwn** | **str** | Initiator port wwn | [optional] 

## Example

```python
from dscc.models.initiator_port import InitiatorPort

# TODO update the JSON string below
json = "{}"
# create an instance of InitiatorPort from a JSON string
initiator_port_instance = InitiatorPort.from_json(json)
# print the JSON string representation of the object
print(InitiatorPort.to_json())

# convert the object into a dict
initiator_port_dict = initiator_port_instance.to_dict()
# create an instance of InitiatorPort from a dict
initiator_port_from_dict = InitiatorPort.from_dict(initiator_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


