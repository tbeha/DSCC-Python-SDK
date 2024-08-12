# NimbleSpaceDomainDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**deduped_volume_count** | **int** | Number of deduplicated volumes belonging to the space domain. | [optional] 
**generation** | **int** | generation | [optional] 
**perf_policy_names** | [**List[NimblePerfPolicySummary]**](NimblePerfPolicySummary.md) | Name of the performance policies associated with the space domain. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**sample_rate** | **int** | Sample rate value. | [optional] 
**type** | **str** | type | [optional] 
**volume_count** | **int** | Number of volumes belonging to the space domain. | [optional] 
**volumes** | [**List[NimbleVolumeSummary]**](NimbleVolumeSummary.md) | Volumes belonging to the space domain. | [optional] 

## Example

```python
from dscc.models.nimble_space_domain_details import NimbleSpaceDomainDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleSpaceDomainDetails from a JSON string
nimble_space_domain_details_instance = NimbleSpaceDomainDetails.from_json(json)
# print the JSON string representation of the object
print(NimbleSpaceDomainDetails.to_json())

# convert the object into a dict
nimble_space_domain_details_dict = nimble_space_domain_details_instance.to_dict()
# create an instance of NimbleSpaceDomainDetails from a dict
nimble_space_domain_details_from_dict = NimbleSpaceDomainDetails.from_dict(nimble_space_domain_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


