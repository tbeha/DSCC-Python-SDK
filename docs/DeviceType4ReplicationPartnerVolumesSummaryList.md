# DeviceType4ReplicationPartnerVolumesSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4ReplicationPartnerVolumeList]**](DeviceType4ReplicationPartnerVolumeList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for source and remote volume list as part of remote protected volume set | [optional] 
**total** | **int** | Total number of replication partner volumes. | [optional] 

## Example

```python
from dscc.models.device_type4_replication_partner_volumes_summary_list import DeviceType4ReplicationPartnerVolumesSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ReplicationPartnerVolumesSummaryList from a JSON string
device_type4_replication_partner_volumes_summary_list_instance = DeviceType4ReplicationPartnerVolumesSummaryList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ReplicationPartnerVolumesSummaryList.to_json())

# convert the object into a dict
device_type4_replication_partner_volumes_summary_list_dict = device_type4_replication_partner_volumes_summary_list_instance.to_dict()
# create an instance of DeviceType4ReplicationPartnerVolumesSummaryList from a dict
device_type4_replication_partner_volumes_summary_list_from_dict = DeviceType4ReplicationPartnerVolumesSummaryList.from_dict(device_type4_replication_partner_volumes_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


