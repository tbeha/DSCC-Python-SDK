# ReplicationPartnersList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ReplicationPartners]**](ReplicationPartners.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for replication partner objects | [optional] 
**total** | **int** | Total number of replication partners. | [optional] 

## Example

```python
from dscc.models.replication_partners_list import ReplicationPartnersList

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationPartnersList from a JSON string
replication_partners_list_instance = ReplicationPartnersList.from_json(json)
# print the JSON string representation of the object
print(ReplicationPartnersList.to_json())

# convert the object into a dict
replication_partners_list_dict = replication_partners_list_instance.to_dict()
# create an instance of ReplicationPartnersList from a dict
replication_partners_list_from_dict = ReplicationPartnersList.from_dict(replication_partners_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


