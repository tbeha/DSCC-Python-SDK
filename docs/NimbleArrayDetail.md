# NimbleArrayDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evac_time** | **int** | Start time of array evacuation. | [optional] 
**evac_usage** | **int** | Initial data in the array. | [optional] 
**migrate** | **str** | Migrate status of array. Possible values: &#39;in&#39;, &#39;none&#39;, &#39;out&#39;. | [optional] 
**snap_usage_compressed_bytes** | **int** | Usage of snapshots in the array. | [optional] 
**usable_capacity** | **int** | Usable capacity of the array. | [optional] 
**usage** | **int** | Usage of the array. | [optional] 
**usage_valid** | **bool** | Indicate whether usage of the array is valid. | [optional] 
**vol_usage_compressed_bytes** | **int** | Usage of volumes in the array. | [optional] 
**array_id** | **str** | Identifier for array. A 42 digit hexadecimal number. | [optional] 
**array_name** | **str** | The user provided name of the array. It is also the array&#39;s hostname. String of up to 63 alphanumeric and can include hyphens characters but cannot start with hyphen. | [optional] 
**id** | **str** | Identifier for array. A 42 digit hexadecimal number. | [optional] 
**name** | **str** | The user provided name of the array. It is also the array&#39;s hostname. String of up to 63 alphanumeric and can include hyphens characters but cannot start with hyphen. | [optional] 

## Example

```python
from dscc.models.nimble_array_detail import NimbleArrayDetail

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleArrayDetail from a JSON string
nimble_array_detail_instance = NimbleArrayDetail.from_json(json)
# print the JSON string representation of the object
print(NimbleArrayDetail.to_json())

# convert the object into a dict
nimble_array_detail_dict = nimble_array_detail_instance.to_dict()
# create an instance of NimbleArrayDetail from a dict
nimble_array_detail_from_dict = NimbleArrayDetail.from_dict(nimble_array_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


