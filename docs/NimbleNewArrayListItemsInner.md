# NimbleNewArrayListItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for array. A 42 digit hexadecimal number. | [optional] 
**model** | **str** | Array model. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**name** | **str** | The user provided name of the array. It is also the array&#39;s hostname. String of up to 63 alphanumeric and can include hyphens characters but cannot start with hyphen. | [optional] 
**pool_id** | **str** | ID of pool to which this is a member. A 42 digit hexadecimal number. | [optional] 
**serial** | **str** | Serial number of the array. | [optional] 
**all_flash** | **bool** | Whether it is an all-flash array. | [optional] 
**allow_lower_limits** | **bool** | Setting this field to &#39;true&#39;  will allow the addition of an array with lower limits to a pool with higher limits. | [optional] 
**available_bytes** | **int** | The available space of the array. | [optional] 
**brand** | **str** | Brand of the array. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**create_pool** | **bool** | Whether to create associated pool during array create. | [optional] 
**creation_time** | **int** | Time when this array object was created. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**ctrlr_a_support_ip** | **str** | Controller A Support IP address. | [optional] 
**ctrlr_b_support_ip** | **str** | Controller B Support IP address. | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dedupe_capacity_bytes** | **int** | The dedupe capacity of a hybrid array. Does not apply to all-flash arrays. | [optional] 
**dedupe_usage_bytes** | **int** | The dedupe usage of a hybrid array. Does not apply to all-flash arrays. | [optional] 
**extended_model** | **str** | Extended model of the array. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**fc_port_count** | **int** | Count of Fibre Channel Ports installed on the array. | [optional] 
**force** | **bool** | Forcibly delete the specified array. | [optional] 
**full_name** | **str** | The array&#39;s fully qualified name. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**generation** | **int** | generation | [optional] 
**gig_nic_port_count** | **int** | Count of 1G NIC Ports installed on the array. | [optional] 
**group_state** | **str** | Group state. State of the array in the group. Possible values: &#39;invalid&#39;, &#39;initialized&#39;, &#39;unused&#39;, &#39;removing&#39;. | [optional] 
**is_fully_dedupe_capable** | **bool** | Flag specifies if the array fully capable to dedupe its usable capacity or not. | [optional] 
**is_sfa** | **bool** | Flag specifies if the array is sfa or not. | [optional] 
**is_supported_hw_config** | **bool** | Whether it is a supported hardware config. | [optional] 
**last_modified** | **int** | Time when this array object was last modified. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**model_sub_type** | **str** | Array model sub-type. | [optional] 
**nic_list** | [**List[NICDetails]**](NICDetails.md) | List of NICs information. Used while creating an array. | [optional] 
**oem** | **str** | OEM brand of the array. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**pending_delete_bytes** | **int** | The pending delete bytes in he tarray. | [optional] 
**pool_description** | **str** | Text description of the pool to be created during array creation. String of up to 255 printable ASCII characters. | [optional] 
**pool_name** | **str** | Name of pool to which this is a member. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**public_key** | [**PublicKeyDetails**](PublicKeyDetails.md) |  | [optional] 
**raw_capacity_bytes** | **int** | The raw capacity bytes of the array. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**role** | **str** | Role of an array in the group. Possible values: &#39;leader&#39;, &#39;non_member&#39;, &#39;invalid&#39;, &#39;backup_leader&#39;, &#39;member&#39;, &#39;failed&#39;. | [optional] 
**search_name** | **str** | The array name used for object search. Alphanumeric string, up to 64 characters including hyphen, period, colon. | [optional] 
**secondary_mgmt_ip** | **str** | Secondary management IP address for the Group. | [optional] 
**snap_compression** | **float** | The compression rate of snapshots in the array expressed as ratio. Fraction expressed as floating point number. | [optional] 
**snap_saved_bytes** | **int** | The saved space of snapshots in the array. | [optional] 
**snap_space_reduction** | **float** | The space reduction rate of snapshots in the array expressed as ratio. Fraction expressed as floating point number. | [optional] 
**snap_usage_bytes** | **int** | The compressed usage of snapshots in array. | [optional] 
**snap_usage_uncompressed_bytes** | **int** | Snap usage uncompressed bytes. | [optional] 
**status** | **str** | Reachability status of the array in the group. Possible values: &#39;unreachable&#39;, &#39;reachable&#39;. | [optional] 
**ten_gig_sfp_nic_port_count** | **int** | Count of 10G SFP NIC Ports installed on the array. | [optional] 
**ten_gig_t_nic_port_count** | **int** | Count of 10G BaseT NIC Ports installed on the array. | [optional] 
**upgrade** | [**UpgradeDetails**](UpgradeDetails.md) |  | [optional] 
**usable_cache_capacity_bytes** | **int** | Usable cache capacity in bytes. | [optional] 
**usable_capacity_bytes** | **int** | The usable capacity bytes of the array. | [optional] 
**usage** | **int** | Used space of the array in bytes. | [optional] 
**usage_valid** | **bool** | Indicates whether the usage of the array is valid. | [optional] 
**version** | **str** | Software version of the array. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**vol_compression** | **float** | The compression rate of volumes in the array expressed as ratio. Fraction expressed as floating point number. | [optional] 
**vol_saved_bytes** | **int** | The saved space of volumes in the array. | [optional] 
**vol_usage_bytes** | **int** | The compressed usage of volumes in the array. | [optional] 
**vol_usage_uncompressed_bytes** | **int** | The volume usage uncompressed bytes. | [optional] 
**zconf_ipaddrs** | [**List[ZConfIPaddrs]**](ZConfIPaddrs.md) | List of link-local zero-configuration addresses of the array. | [optional] 

## Example

```python
from dscc.models.nimble_new_array_list_items_inner import NimbleNewArrayListItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNewArrayListItemsInner from a JSON string
nimble_new_array_list_items_inner_instance = NimbleNewArrayListItemsInner.from_json(json)
# print the JSON string representation of the object
print(NimbleNewArrayListItemsInner.to_json())

# convert the object into a dict
nimble_new_array_list_items_inner_dict = nimble_new_array_list_items_inner_instance.to_dict()
# create an instance of NimbleNewArrayListItemsInner from a dict
nimble_new_array_list_items_inner_from_dict = NimbleNewArrayListItemsInner.from_dict(nimble_new_array_list_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


