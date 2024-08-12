# NimbleReplicationPartnersList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleReplicationPartner]**](NimbleReplicationPartner.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | RequestUri for replication partner objects | [optional] 
**total** | **int** | Total number of replication partners. | [optional] 

## Example

```python
from dscc.models.nimble_replication_partners_list import NimbleReplicationPartnersList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleReplicationPartnersList from a JSON string
nimble_replication_partners_list_instance = NimbleReplicationPartnersList.from_json(json)
# print the JSON string representation of the object
print(NimbleReplicationPartnersList.to_json())

# convert the object into a dict
nimble_replication_partners_list_dict = nimble_replication_partners_list_instance.to_dict()
# create an instance of NimbleReplicationPartnersList from a dict
nimble_replication_partners_list_from_dict = NimbleReplicationPartnersList.from_dict(nimble_replication_partners_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


