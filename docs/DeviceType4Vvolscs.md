# DeviceType4Vvolscs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4vVolscDetails]**](DeviceType4vVolscDetails.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**total** | **int** | Number of storage container | [optional] 

## Example

```python
from dscc.models.device_type4_vvolscs import DeviceType4Vvolscs

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4Vvolscs from a JSON string
device_type4_vvolscs_instance = DeviceType4Vvolscs.from_json(json)
# print the JSON string representation of the object
print(DeviceType4Vvolscs.to_json())

# convert the object into a dict
device_type4_vvolscs_dict = device_type4_vvolscs_instance.to_dict()
# create an instance of DeviceType4Vvolscs from a dict
device_type4_vvolscs_from_dict = DeviceType4Vvolscs.from_dict(device_type4_vvolscs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


