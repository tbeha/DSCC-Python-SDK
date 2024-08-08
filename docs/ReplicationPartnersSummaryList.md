# ReplicationPartnersSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ReplicationPartnerList]**](ReplicationPartnerList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for replication partner list where volume set is remote protected | [optional] 
**total** | **int** | Number of  replication partners. | [optional] 

## Example

```python
from dscc.models.replication_partners_summary_list import ReplicationPartnersSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationPartnersSummaryList from a JSON string
replication_partners_summary_list_instance = ReplicationPartnersSummaryList.from_json(json)
# print the JSON string representation of the object
print(ReplicationPartnersSummaryList.to_json())

# convert the object into a dict
replication_partners_summary_list_dict = replication_partners_summary_list_instance.to_dict()
# create an instance of ReplicationPartnersSummaryList from a dict
replication_partners_summary_list_from_dict = ReplicationPartnersSummaryList.from_dict(replication_partners_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


