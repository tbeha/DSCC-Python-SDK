# NimbleVolumeExportDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_groups** | [**List[NimbleHostGroupDetail]**](NimbleHostGroupDetail.md) |  | [optional] 

## Example

```python
from dscc.models.nimble_volume_export_details import NimbleVolumeExportDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleVolumeExportDetails from a JSON string
nimble_volume_export_details_instance = NimbleVolumeExportDetails.from_json(json)
# print the JSON string representation of the object
print(NimbleVolumeExportDetails.to_json())

# convert the object into a dict
nimble_volume_export_details_dict = nimble_volume_export_details_instance.to_dict()
# create an instance of NimbleVolumeExportDetails from a dict
nimble_volume_export_details_from_dict = NimbleVolumeExportDetails.from_dict(nimble_volume_export_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


