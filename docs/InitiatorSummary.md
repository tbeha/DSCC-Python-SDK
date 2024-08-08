# InitiatorSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address of the initiator.  | [optional] 
**id** | **str** | Identifier for an initiator. | [optional] 
**ip_address** | **str** | IP address of the initiator. | [optional] 
**name** | **str** | Name of the initiator. | [optional] 
**protocol** | **str** | protocol supported are : FC ,iSCSI or NVMe | [optional] 
**systems** | **List[str]** | system IDs to which the initiator belongs to. | [optional] 

## Example

```python
from dscc.models.initiator_summary import InitiatorSummary

# TODO update the JSON string below
json = "{}"
# create an instance of InitiatorSummary from a JSON string
initiator_summary_instance = InitiatorSummary.from_json(json)
# print the JSON string representation of the object
print(InitiatorSummary.to_json())

# convert the object into a dict
initiator_summary_dict = initiator_summary_instance.to_dict()
# create an instance of InitiatorSummary from a dict
initiator_summary_from_dict = InitiatorSummary.from_dict(initiator_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


