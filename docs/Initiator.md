# Initiator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address of the initiator. &#x60;Filter&#x60; | [optional] 
**associated_links** | [**List[ScAssociatedLinksInner]**](ScAssociatedLinksInner.md) | Associated Links Details | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**driver_version** | **str** | Driver version of the host initiator. | [optional] 
**firmware_version** | **str** | Firmware version of the host initiator. | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**hba_model** | **str** | Host bus adaptor model of the host initiator | [optional] 
**host_speed** | **int** | Host speed | [optional] 
**hosts** | [**List[HostSummaryForInitiatorObject]**](HostSummaryForInitiatorObject.md) | List of hosts. | [optional] 
**id** | **str** | Identifier for an initiator. | [optional] 
**ip_address** | **str** | IP address of the initiator. | [optional] 
**name** | **str** | Name of the initiator. | [optional] 
**protocol** | **str** | protocol supported are : FC ,iSCSI or NVMe | [optional] 
**systems** | **List[str]** | system IDs to which the host initiator is linked to. | [optional] 
**type** | **str** | The type of resource. | [optional] 
**vendor** | **str** | Vendor of the host initiator | [optional] 

## Example

```python
from dscc.models.initiator import Initiator

# TODO update the JSON string below
json = "{}"
# create an instance of Initiator from a JSON string
initiator_instance = Initiator.from_json(json)
# print the JSON string representation of the object
print(Initiator.to_json())

# convert the object into a dict
initiator_dict = initiator_instance.to_dict()
# create an instance of Initiator from a dict
initiator_from_dict = Initiator.from_dict(initiator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


