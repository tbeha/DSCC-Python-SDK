# NimblePerformancePolicyListItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_category** | **str** | Specifies the application category of the associated volume. &#x60;Filter, Sort&#x60; | [optional] 
**cache** | **bool** | Flag denoting if data in the associated volume should be cached. &#x60;Filter, Sort&#x60; | [optional] 
**cache_policy** | **str** | Specifies how data of associated volume should be cached. Supports two policies, &#39;normal&#39; and &#39;aggressive&#39;. &#39;normal&#39; policy caches data but skips in certain conditions such as sequential I/O. &#39;aggressive&#39; policy will accelerate caching of all data belonging to this volume, regardless of sequentiality. Possible values:&#39;normal&#39;, &#39;no_write&#39;, &#39;aggressive_read_no_write&#39;, &#39;disabled&#39;, &#39;aggressive&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**compress** | **bool** | Flag denoting if data in the associated volume should be compressed. &#x60;Filter, Sort&#x60; | [optional] 
**creation_time** | **int** | Time when the performance policy was created. &#x60;Filter, Sort&#x60; | [optional] 
**dedupe_enabled** | **bool** | Specifies if dedupe is enabled for volumes created with this performance policy. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier for the Performance Policy. &#x60;Filter&#x60; | [optional] 
**last_modified** | **int** | Time when the performance policy&#39;s configurations were last modified. &#x60;Filter, Sort&#x60; | [optional] 
**name** | **str** | Name of the Performance Policy. &#x60;Filter, Sort&#x60; | [optional] 
**predefined** | **bool** | Specifies if this performance policy is predefined (read-only). &#x60;Filter, Sort&#x60; | [optional] 
**space_policy** | **str** | Specifies the state of the volume upon space constraint violation such as volume limit violation or volumes above their volume reserve, if the pool free space is exhausted. Supports two policies, &#39;offline&#39; and &#39;non_writable&#39;. Possible values:&#39;offline&#39;, &#39;login_only&#39;, &#39;non_writable&#39;, &#39;read_only&#39;, &#39;invalid&#39;. &#x60;Filter, Sort&#x60; | [optional] 
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
from dscc.models.nimble_performance_policy_list_items_inner import NimblePerformancePolicyListItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of NimblePerformancePolicyListItemsInner from a JSON string
nimble_performance_policy_list_items_inner_instance = NimblePerformancePolicyListItemsInner.from_json(json)
# print the JSON string representation of the object
print(NimblePerformancePolicyListItemsInner.to_json())

# convert the object into a dict
nimble_performance_policy_list_items_inner_dict = nimble_performance_policy_list_items_inner_instance.to_dict()
# create an instance of NimblePerformancePolicyListItemsInner from a dict
nimble_performance_policy_list_items_inner_from_dict = NimblePerformancePolicyListItemsInner.from_dict(nimble_performance_policy_list_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


