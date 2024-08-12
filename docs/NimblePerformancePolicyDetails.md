# NimblePerformancePolicyDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**block_size** | **int** | Block Size in bytes to be used by the volumes created with this specific performance policy. Supported block sizes are 4096 bytes (4 KB), 8192 bytes (8 KB), 16384 bytes(16 KB), and 32768 bytes (32 KB). Block size of a performance policy cannot be changed once the performance policy is created. | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dedupe_override_pools** | [**List[NimbleNsPoolSummary]**](NimbleNsPoolSummary.md) | List of pools that override performance policy&#39;s dedupe setting. | [optional] 
**description** | **str** | Description of a performance policy. | [optional] 
**full_name** | **str** | Fully qualified name of the Performance Policy. | [optional] 
**generation** | **int** | generation | [optional] 
**perfpolicy_creator_id** | **str** | Originator id for the performance policy. | [optional] 
**perfpolicy_creator_name** | **str** | Originator name for the performance policy. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**search_name** | **str** | Name of the Performance Policy used for object search. | [optional] 
**type** | **str** | type | [optional] 
**volume_count** | **int** | Number of volumes using this performance policy. | [optional] 

## Example

```python
from dscc.models.nimble_performance_policy_details import NimblePerformancePolicyDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NimblePerformancePolicyDetails from a JSON string
nimble_performance_policy_details_instance = NimblePerformancePolicyDetails.from_json(json)
# print the JSON string representation of the object
print(NimblePerformancePolicyDetails.to_json())

# convert the object into a dict
nimble_performance_policy_details_dict = nimble_performance_policy_details_instance.to_dict()
# create an instance of NimblePerformancePolicyDetails from a dict
nimble_performance_policy_details_from_dict = NimblePerformancePolicyDetails.from_dict(nimble_performance_policy_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


