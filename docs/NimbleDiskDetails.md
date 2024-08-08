# NimbleDiskDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_uri** | **str** | requestUri for detailed disk object | [optional] 
**array_id** | **str** | ID of array the disk belongs to. A 42 digit hexadecimal number. | [optional] 
**array_name** | **str** | Name of array the disk belongs to. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**disk_type** | **str** | Type of disk. Possible values: &#39;hdd&#39;, &#39;ssd&#39;. | [optional] 
**id** | **str** | Identifier of disk. A 42 digit hexadecimal number. | [optional] 
**model** | **str** | Disk model name. | [optional] 
**serial** | **str** | Disk serial number(N/A if empty). | [optional] 
**shelf_id** | **str** | Identifies the physical shelf the disk belongs to. A 42 digit hexadecimal number. | [optional] 
**shelf_serial** | **str** | Serial number of the shelf the disk is attached to. | [optional] 
**state** | **str** | Disk hardware state. Disk state. Possible values: &#39;valid&#39;, &#39;in use&#39;, &#39;failed&#39;, absent&#39;, &#39;removed&#39;, &#39;void&#39;, &#39;t_fail&#39;, &#39;foreign&#39;. | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**bank** | **int** | Disk bank number. | [optional] 
**block_type** | **str** | Native block type of the disk. Possible values: &#39;block_512e&#39;, &#39;block_4Kn&#39;, &#39;block_none&#39;, &#39;block_512n&#39;. | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**disk_internal_stat1** | **str** | Internal disk statistic 1. | [optional] 
**disk_op** | **str** | The intended operation to be performed on the specified disk. | [optional] 
**firmware_version** | **str** | Firmware version on the disk. | [optional] 
**force** | **bool** | Forcibly add a disk. | [optional] 
**generation** | **int** | generation | [optional] 
**hba** | **int** | HBA ID the disk is connected to. | [optional] 
**is_dfc** | **bool** | Is disk part of dual flash carrier. | [optional] 
**partial_response_ok** | **bool** | Whether response is partial or not. | [optional] 
**path** | **str** | Disk SCSI device path. | [optional] 
**port** | **int** | HBA port number the disk is connected to. | [optional] 
**raid_id** | **int** | Raid ID. | [optional] 
**raid_resync_average_speed** | **int** | Average RAID rebuild speed (bytes/sec). | [optional] 
**raid_resync_current_speed** | **int** | Current RAID rebuild speed (bytes/sec). | [optional] 
**raid_resync_percent** | **int** | Percentage RAID rebuild completed on this disk. | [optional] 
**raid_state** | **str** | RAID status for the disk (N/A, okay, resynchronizing, spare, faulty). Disk RAID state. Possible values: &#39;N/A&#39;, &#39;okay&#39;, &#39;resynchronizing&#39;, &#39;spare&#39;, &#39;faulty&#39;. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**shelf_location** | **str** | Identifies the controller, port, and chain position of the shelf the disk belongs to. | [optional] 
**shelf_location_id** | **int** | Identifies the position shelf the disk belongs to, as coded integer. | [optional] 
**size** | **int** | Disk size in bytes. | [optional] 
**slot** | **int** | Disk slot number. | [optional] 
**smart_attribute_list** | [**List[NimbleDiskSmartAttributes]**](NimbleDiskSmartAttributes.md) | S.M.A.R.T. attributes for the disk. List of Smart attributes. | [optional] 
**type** | **str** | type | [optional] 
**vendor** | **str** | Vendor name of the disk manufacturer. | [optional] 
**vshelf_id** | **int** | Identifies the local shelf id the disk belongs to. | [optional] 

## Example

```python
from dscc.models.nimble_disk_details import NimbleDiskDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleDiskDetails from a JSON string
nimble_disk_details_instance = NimbleDiskDetails.from_json(json)
# print the JSON string representation of the object
print(NimbleDiskDetails.to_json())

# convert the object into a dict
nimble_disk_details_dict = nimble_disk_details_instance.to_dict()
# create an instance of NimbleDiskDetails from a dict
nimble_disk_details_from_dict = NimbleDiskDetails.from_dict(nimble_disk_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


