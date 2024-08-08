# NimblePerformancePolicyFieldsWithSortKey


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

## Example

```python
from dscc.models.nimble_performance_policy_fields_with_sort_key import NimblePerformancePolicyFieldsWithSortKey

# TODO update the JSON string below
json = "{}"
# create an instance of NimblePerformancePolicyFieldsWithSortKey from a JSON string
nimble_performance_policy_fields_with_sort_key_instance = NimblePerformancePolicyFieldsWithSortKey.from_json(json)
# print the JSON string representation of the object
print(NimblePerformancePolicyFieldsWithSortKey.to_json())

# convert the object into a dict
nimble_performance_policy_fields_with_sort_key_dict = nimble_performance_policy_fields_with_sort_key_instance.to_dict()
# create an instance of NimblePerformancePolicyFieldsWithSortKey from a dict
nimble_performance_policy_fields_with_sort_key_from_dict = NimblePerformancePolicyFieldsWithSortKey.from_dict(nimble_performance_policy_fields_with_sort_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


