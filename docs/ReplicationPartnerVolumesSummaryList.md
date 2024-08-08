# ReplicationPartnerVolumesSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ReplicationPartnerVolumeList]**](ReplicationPartnerVolumeList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for source and remote volume list as part of remote protected volume set | [optional] 
**total** | **int** | Total number of replication partner volumes. | [optional] 

## Example

```python
from dscc.models.replication_partner_volumes_summary_list import ReplicationPartnerVolumesSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationPartnerVolumesSummaryList from a JSON string
replication_partner_volumes_summary_list_instance = ReplicationPartnerVolumesSummaryList.from_json(json)
# print the JSON string representation of the object
print(ReplicationPartnerVolumesSummaryList.to_json())

# convert the object into a dict
replication_partner_volumes_summary_list_dict = replication_partner_volumes_summary_list_instance.to_dict()
# create an instance of ReplicationPartnerVolumesSummaryList from a dict
replication_partner_volumes_summary_list_from_dict = ReplicationPartnerVolumesSummaryList.from_dict(replication_partner_volumes_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


