# InitiatorObjectDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address of the initiator.  | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**id** | **str** | Identifier for an initiator. | [optional] 
**ip_address** | **str** | IP address of the initiator. | [optional] 
**name** | **str** | Name of the initiator. | [optional] 
**protocol** | **str** | protocol supported are : FC ,iSCSI or NVMe | [optional] 
**systems** | **List[Optional[str]]** | system IDs to which the initiator belongs to. (This field is deprecated) | [optional] 
**type** | **str** | The type of resource. | [optional] 

## Example

```python
from dscc.models.initiator_object_details import InitiatorObjectDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InitiatorObjectDetails from a JSON string
initiator_object_details_instance = InitiatorObjectDetails.from_json(json)
# print the JSON string representation of the object
print(InitiatorObjectDetails.to_json())

# convert the object into a dict
initiator_object_details_dict = initiator_object_details_instance.to_dict()
# create an instance of InitiatorObjectDetails from a dict
initiator_object_details_from_dict = InitiatorObjectDetails.from_dict(initiator_object_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


