# DiskFilterableFieldsWithoutFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **str** | ID of array the disk belongs to. A 42 digit hexadecimal number. | [optional] 
**array_name** | **str** | Name of array the disk belongs to. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**disk_type** | **str** | Type of disk (HDD, SSD, N/A). Disk type. Possible values: &#39;hdd&#39;, &#39;ssd&#39;. | [optional] 
**id** | **str** | Identifier of disk. A 42 digit hexadecimal number. | [optional] 
**model** | **str** | Disk model name. | [optional] 
**serial** | **str** | Disk serial number(N/A if empty). | [optional] 
**shelf_id** | **str** | Identifies the physical shelf the disk belongs to. A 42 digit hexadecimal number. | [optional] 
**shelf_serial** | **str** | Serial number of the shelf the disk is attached to. | [optional] 
**state** | **str** | Disk hardware state. Disk state. Possible values: &#39;valid&#39;, &#39;in use&#39;, &#39;failed&#39;, absent&#39;, &#39;removed&#39;, &#39;void&#39;, &#39;t_fail&#39;, &#39;foreign&#39;. | [optional] 

## Example

```python
from dscc.models.disk_filterable_fields_without_filter import DiskFilterableFieldsWithoutFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DiskFilterableFieldsWithoutFilter from a JSON string
disk_filterable_fields_without_filter_instance = DiskFilterableFieldsWithoutFilter.from_json(json)
# print the JSON string representation of the object
print(DiskFilterableFieldsWithoutFilter.to_json())

# convert the object into a dict
disk_filterable_fields_without_filter_dict = disk_filterable_fields_without_filter_instance.to_dict()
# create an instance of DiskFilterableFieldsWithoutFilter from a dict
disk_filterable_fields_without_filter_from_dict = DiskFilterableFieldsWithoutFilter.from_dict(disk_filterable_fields_without_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


