# NimbleVolumeCollectionListItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_cluster_name** | **str** | If the application is running within a Windows cluster environment, this is the cluster name. &#x60;Filter, Sort&#x60; | [optional] 
**app_id** | **str** | Application ID running on the server. Application ID can only be specified if application synchronization is \\\\\&quot;vss\\\\\&quot;. &#x60;Filter, Sort&#x60; Possible values: &#39;exchange_dag&#39;, &#39;sql2012&#39;, &#39;inval&#39;, &#39;sql2014&#39;, &#39;sql2005&#39;, &#39;sql2016&#39;, &#39;exchange&#39;, &#39;sql2017&#39;, &#39;sql2018&#39;, &#39;hyperv&#39;. | [optional] 
**app_server** | **str** | Application server hostname. &#x60;Filter, Sort&#x60; | [optional] 
**app_service_name** | **str** | If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster environment. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Identifier of the Volume-Collection. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Name of volume collection. &#x60;Filter, Sort&#x60; | [optional] 
**prottmpl_id** | **str** | Identifier of the protection template whose attributes will be used to create this volume collection. This attribute is only used for input when creating a volume collection and is not outputed. &#x60;Filter, Sort&#x60; | [optional] 
**replication_type** | **str** | Type of replication configured for the volume collection. Possible values: &#39;synchronous&#39;, &#39;periodic_snapshot&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**synchronous_replication_state** | **str** | State of synchronous replication on the volume collection. Possible values: &#39;in_sync&#39;, &#39;not_applicable&#39;, &#39;out_of_sync&#39;, &#39;unknown&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**synchronous_replication_type** | **str** | Type of synchronous replication configured for the volume collection. Possible values: &#39;soft_available&#39;, &#39;not_applicable&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**agent_hostname** | **str** | Generic backup agent hostname. Custom port number can be specified with agent hostname using \\\\\&quot;:\\\\\&quot;. | [optional] 
**app_sync** | **str** | Application Synchronization. Possible values: &#39;vss&#39;, &#39;vmware&#39;, &#39;none&#39;, &#39;generic&#39;. | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**cache_pinned_volume_list** | [**List[NimbleVolumeSummary]**](NimbleVolumeSummary.md) | List of cache pinned volumes associated with volume collection. | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**creation_time** | **int** | Application server hostname. | [optional] 
**customer_id** | **str** | customerId | [optional] 
**description** | **str** | Text descrption of volume collection. | [optional] 
**downstream_volume_list** | [**List[NimbleVolumeCollectionVolumePoolInfo]**](NimbleVolumeCollectionVolumePoolInfo.md) | List of downstream volumes associated with the volume collection. | [optional] 
**full_name** | **str** | Fully qualified name of volume collection. | [optional] 
**generation** | **int** | generation | [optional] 
**handover_replication_partner** | **str** | Replication partner to which ownership is being transferred as part of handover operation. | [optional] 
**is_handing_over** | **bool** | Indicates whether a handover operation is in progress on this volume collection. | [optional] 
**is_mfa_protected** | **bool** | Protected by multi-factor authentication. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**is_standalone_volcoll** | **bool** | Last snapshot collection on this volume collection. | [optional] 
**lag_time** | **int** | Replication lag time for volume collection. | [optional] 
**last_replicated_snapcoll** | [**NimbleSnapcollSummary**](NimbleSnapcollSummary.md) | Last replicated snapshot collection on this volume collection. | [optional] 
**last_snapcoll** | [**NimbleSnapcollSummary**](NimbleSnapcollSummary.md) | Last snapshot collection on this volume collection. | [optional] 
**metadata** | [**List[NimbleNsKeyValue]**](NimbleNsKeyValue.md) | Key-value pairs that augment a volume collection&#39;s attributes. | [optional] 
**pol_owner_name** | **str** | PolOwnerName - Owner group. | [optional] 
**protection_type** | **str** | Specifies if volume collection is protected with schedules. If protected, indicated whether replication is setup. | [optional] 
**repl_bytes_transferred** | **int** | Total size of volumes replicated for this volume collection. | [optional] 
**repl_priority** | **str** | Replication priority for the volume collection with the following choices: {normal | high}.  Possible values: &#39;normal&#39;, &#39;high&#39;. | [optional] 
**replication_partner** | **List[str]** | List of replication partners associated with the volume collection. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**schedule_list** | [**List[NimbleNsSchedule]**](NimbleNsSchedule.md) | List of schedules for this volume collection. | [optional] 
**search_name** | **str** | Name of volume collection used for object search. | [optional] 
**snapcoll_count** | **int** | Count of snapshot collections associated with volume collection. | [optional] 
**srep_last_sync** | **int** | Time when a synchronously replicated volume collection was last synchronized. | [optional] 
**srep_resync_percent** | **int** | Percentage of the resync progress for a synchronously replicated volume collection. | [optional] 
**total_repl_bytes** | **int** | Total size of volumes to be replicated for this volume collection. | [optional] 
**type** | **str** | type | [optional] 
**upstream_volume_list** | [**List[NimbleVolumeCollectionVolumePoolInfo]**](NimbleVolumeCollectionVolumePoolInfo.md) | List of upstream volumes associated with the volume collection. | [optional] 
**vcenter_hostname** | **str** | VMware vCenter hostname. Custom port number can be specified with vCenter hostname using \\\\\&quot;:\\\\\&quot;. | [optional] 
**vcenter_username** | **str** | Application VMware vCenter username. | [optional] 
**volcoll_creator_id** | **str** | Originator id for the volume collection. | [optional] 
**volcoll_creator_name** | **str** | Originator name for the volume collection. | [optional] 
**volume_count** | **int** | Count of volumes associated with the volume collection. | [optional] 
**volume_list** | [**List[NimbleVolumeSummary]**](NimbleVolumeSummary.md) | List of volumes associated with the volume collection. | [optional] 

## Example

```python
from dscc.models.nimble_volume_collection_list_items_inner import NimbleVolumeCollectionListItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleVolumeCollectionListItemsInner from a JSON string
nimble_volume_collection_list_items_inner_instance = NimbleVolumeCollectionListItemsInner.from_json(json)
# print the JSON string representation of the object
print(NimbleVolumeCollectionListItemsInner.to_json())

# convert the object into a dict
nimble_volume_collection_list_items_inner_dict = nimble_volume_collection_list_items_inner_instance.to_dict()
# create an instance of NimbleVolumeCollectionListItemsInner from a dict
nimble_volume_collection_list_items_inner_from_dict = NimbleVolumeCollectionListItemsInner.from_dict(nimble_volume_collection_list_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


