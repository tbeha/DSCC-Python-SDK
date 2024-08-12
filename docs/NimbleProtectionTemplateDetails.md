# NimbleProtectionTemplateDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_username** | **str** | Generic Backup agent username. | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**description** | **str** | Text description of protection template. | [optional] 
**full_name** | **str** | Fully qualified name of protection template. | [optional] 
**generation** | **int** | generation | [optional] 
**repl_priority** | **str** | Replication priority for the protection template with the following choices: {normal | high}. Possible values:&#39;normal&#39;, &#39;high&#39;. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**schedule_list** | [**List[NimbleNsSchedule]**](NimbleNsSchedule.md) | List of schedules for this protection policy. | [optional] 
**search_name** | **str** | Name of protection template used for object search. | [optional] 
**type** | **str** | type | [optional] 
**vcenter_username** | **str** | VMware vCenter username. | [optional] 

## Example

```python
from dscc.models.nimble_protection_template_details import NimbleProtectionTemplateDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleProtectionTemplateDetails from a JSON string
nimble_protection_template_details_instance = NimbleProtectionTemplateDetails.from_json(json)
# print the JSON string representation of the object
print(NimbleProtectionTemplateDetails.to_json())

# convert the object into a dict
nimble_protection_template_details_dict = nimble_protection_template_details_instance.to_dict()
# create an instance of NimbleProtectionTemplateDetails from a dict
nimble_protection_template_details_from_dict = NimbleProtectionTemplateDetails.from_dict(nimble_protection_template_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


