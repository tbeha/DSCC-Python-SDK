# NimbleDriveSetDetails

List of Drive Sets for the respective shelf.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_dedupe_impact** | **bool** | Accept the reduction or elimination of deduplication capability on the system as a result of activating a shelf that does not meet the necessary deduplication requirements. Possible values: &#39;true&#39;, &#39;false&#39;. | 
**accept_foreign** | **bool** | Accept the removal of data on the shelf disks and activate foreign shelf. Possible values: &#39;true&#39;, &#39;false&#39;. | 
**driveset** | **int** | Driveset to activate. | 

## Example

```python
from dscc.models.nimble_drive_set_details import NimbleDriveSetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleDriveSetDetails from a JSON string
nimble_drive_set_details_instance = NimbleDriveSetDetails.from_json(json)
# print the JSON string representation of the object
print(NimbleDriveSetDetails.to_json())

# convert the object into a dict
nimble_drive_set_details_dict = nimble_drive_set_details_instance.to_dict()
# create an instance of NimbleDriveSetDetails from a dict
nimble_drive_set_details_from_dict = NimbleDriveSetDetails.from_dict(nimble_drive_set_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


