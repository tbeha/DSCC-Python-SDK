# NimbleProtectionTemplateDetailsWithRequestUri


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_uri** | **str** | requestUri for detailed protection-templates object | [optional] 
**agent_hostname** | **str** | Generic Backup agent hostname. Custom port number can be specified with agent hostname using \\\\\&quot;:\\\\\&quot;. | [optional] 
**app_cluster_name** | **str** | If the application is running within a Windows cluster environment then this is the cluster name. | [optional] 
**app_id** | **str** | Application ID running on the server. Application ID can only be specified if application synchronization is VSS.  Possible values:&#39;exchange_dag&#39;, &#39;sql2012&#39;, &#39;sql2014&#39;, &#39;inval&#39;, &#39;sql2005&#39;, &#39;sql2016&#39;, &#39;exchange&#39;, &#39;sql2017&#39;, &#39;sql2018&#39;, &#39;hyperv&#39;. | [optional] 
**app_server** | **str** | Application server hostname. | [optional] 
**app_service_name** | **str** | If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster environment. | [optional] 
**app_sync** | **str** | Application synchronization ({none|vss|vmware|generic}). Possible values:&#39;vss&#39;, &#39;vmware&#39;, &#39;none&#39;, &#39;generic&#39;. | [optional] 
**creation_time** | **int** | Time when this protection template was created. | [optional] 
**id** | **str** | Identifier for protection template. | [optional] 
**last_modified** | **int** | Time when this protection template was last modified. | [optional] 
**name** | **str** | Fully qualified name of protection template. | [optional] 
**vcenter_hostname** | **str** | VMware vCenter hostname. Custom port number can be specified with vCenter hostname. | [optional] 
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
from dscc.models.nimble_protection_template_details_with_request_uri import NimbleProtectionTemplateDetailsWithRequestUri

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleProtectionTemplateDetailsWithRequestUri from a JSON string
nimble_protection_template_details_with_request_uri_instance = NimbleProtectionTemplateDetailsWithRequestUri.from_json(json)
# print the JSON string representation of the object
print(NimbleProtectionTemplateDetailsWithRequestUri.to_json())

# convert the object into a dict
nimble_protection_template_details_with_request_uri_dict = nimble_protection_template_details_with_request_uri_instance.to_dict()
# create an instance of NimbleProtectionTemplateDetailsWithRequestUri from a dict
nimble_protection_template_details_with_request_uri_from_dict = NimbleProtectionTemplateDetailsWithRequestUri.from_dict(nimble_protection_template_details_with_request_uri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


