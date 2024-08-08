# NimbleVolumeCommonExportDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume_export_details** | [**NimbleVolumeExportDetails**](NimbleVolumeExportDetails.md) |  | [optional] 

## Example

```python
from dscc.models.nimble_volume_common_export_details import NimbleVolumeCommonExportDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleVolumeCommonExportDetails from a JSON string
nimble_volume_common_export_details_instance = NimbleVolumeCommonExportDetails.from_json(json)
# print the JSON string representation of the object
print(NimbleVolumeCommonExportDetails.to_json())

# convert the object into a dict
nimble_volume_common_export_details_dict = nimble_volume_common_export_details_instance.to_dict()
# create an instance of NimbleVolumeCommonExportDetails from a dict
nimble_volume_common_export_details_from_dict = NimbleVolumeCommonExportDetails.from_dict(nimble_volume_common_export_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


