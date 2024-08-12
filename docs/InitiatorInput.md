# InitiatorInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address of the initiator. | 
**driver_version** | **str** | Driver version of the host initiator. | [optional] 
**firmware_version** | **str** | Firmware version of the host initiator. | [optional] 
**hba_model** | **str** | Host bus adaptor model of the host initiator | [optional] 
**host_speed** | **int** | Host speed | [optional] 
**ip_address** | **str** | IP address of the initiator. | [optional] 
**name** | **str** | Name of the initiator. | [optional] 
**protocol** | **str** | protocol supported are : FC, iSCSI or NVMe | 
**vendor** | **str** | Vendor of the host initiator | [optional] 

## Example

```python
from dscc.models.initiator_input import InitiatorInput

# TODO update the JSON string below
json = "{}"
# create an instance of InitiatorInput from a JSON string
initiator_input_instance = InitiatorInput.from_json(json)
# print the JSON string representation of the object
print(InitiatorInput.to_json())

# convert the object into a dict
initiator_input_dict = initiator_input_instance.to_dict()
# create an instance of InitiatorInput from a dict
initiator_input_from_dict = InitiatorInput.from_dict(initiator_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


