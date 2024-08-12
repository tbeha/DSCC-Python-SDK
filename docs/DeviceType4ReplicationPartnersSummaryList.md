# DeviceType4ReplicationPartnersSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4ReplicationPartnerList]**](DeviceType4ReplicationPartnerList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for replication partner list where volume set is remote protected | [optional] 
**total** | **int** | Number of  replication partners. | [optional] 

## Example

```python
from dscc.models.device_type4_replication_partners_summary_list import DeviceType4ReplicationPartnersSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ReplicationPartnersSummaryList from a JSON string
device_type4_replication_partners_summary_list_instance = DeviceType4ReplicationPartnersSummaryList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ReplicationPartnersSummaryList.to_json())

# convert the object into a dict
device_type4_replication_partners_summary_list_dict = device_type4_replication_partners_summary_list_instance.to_dict()
# create an instance of DeviceType4ReplicationPartnersSummaryList from a dict
device_type4_replication_partners_summary_list_from_dict = DeviceType4ReplicationPartnersSummaryList.from_dict(device_type4_replication_partners_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


