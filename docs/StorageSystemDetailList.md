# StorageSystemDetailList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_list** | [**List[NimbleArraySummary]**](NimbleArraySummary.md) | The list of Nimble arrays part of this system. | [optional] 
**associated_links** | [**List[DeviceType4AssociatedLinksInner]**](DeviceType4AssociatedLinksInner.md) | Associated Links Details | [optional] 
**callhome_status** | **str** | Device Call-home connectivity status. | [optional] 
**collection_status** | [**CollectionStatus**](CollectionStatus.md) |  | [optional] 
**connection_status** | [**ConnectionStatus**](ConnectionStatus.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**description** | **str** | A brief description of the storage system. | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | UUID string uniquely identifying the storage system object. | [optional] 
**last_connected_time** | **int** | Last time when the system was connected | [optional] 
**max_volume_deco_size_mib** | **str** | Maximum supported volume DECO size. This is applicable for 10.4.0 and above versions. | [optional] 
**mgmt_ip** | [**Ips**](Ips.md) |  | [optional] 
**min_volume_deco_size_mib** | **str** | Minimum supported volume DECO size. This is applicable for 10.4.0 and above versions. | [optional] 
**model** | **str** | Model of the storage system &#x60;Filter, Sort&#x60; | [optional] 
**name** | **str** | A name to identify the storage system. &#x60;Filter, Sort&#x60; | [optional] 
**product_family** | **str** | Storage device type | [optional] 
**resource_uri** | **str** | resourceUri for detailed storage object | [optional] 
**software_version** | **str** | Software version of the storage system &#x60;Filter, Sort&#x60; | [optional] 
**state** | **str** | For deviceType1 State derived from ports, enclosure, disk and node state for deviceType2 state is state reported by deviceType2 array &#x60;Filter&#x60; | [optional] 
**system_wwn** | **str** | WWN of the array | [optional] 
**tier_type** | **str** | StorageTier. | [optional] 
**type** | **str** | type | [optional] 
**up_since** | **int** | The time that the system has been up since | [optional] 

## Example

```python
from dscc.models.storage_system_detail_list import StorageSystemDetailList

# TODO update the JSON string below
json = "{}"
# create an instance of StorageSystemDetailList from a JSON string
storage_system_detail_list_instance = StorageSystemDetailList.from_json(json)
# print the JSON string representation of the object
print(StorageSystemDetailList.to_json())

# convert the object into a dict
storage_system_detail_list_dict = storage_system_detail_list_instance.to_dict()
# create an instance of StorageSystemDetailList from a dict
storage_system_detail_list_from_dict = StorageSystemDetailList.from_dict(storage_system_detail_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


