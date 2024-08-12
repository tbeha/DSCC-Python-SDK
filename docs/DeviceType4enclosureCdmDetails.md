# DeviceType4enclosureCdmDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Enclosure Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**element_status_code** | **str** | Enclosure status code | [optional] 
**enclosure_id** | **int** | ID of the enclosure | [optional] 
**enclosure_uid** | **str** | Unique Identifier of the enclosure. | [optional] 
**fail_ind** | **str** | Status of the Failure Visual Indication. | [optional] 
**fw_version** | **str** | Firmware Version. | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource | [optional] 
**manufacturing** | [**DeviceType4ManufacturingSingle**](DeviceType4ManufacturingSingle.md) |  | [optional] 
**ok_int** | **str** | Status of the OK Visual Indication. | [optional] 
**os_version** | **str** | Enclosure Card CDM OS name/version | [optional] 
**p_uid** | **str** | Enclosure Card CDM puid. | [optional] 
**safe_to_remove** | **str** | Indicates if the component is safe to remove | [optional] 
**system_id** | **str** | systemId | [optional] 
**type** | **str** | type | [optional] 
**updating** | **str** | Revision firmware of the PCI card | [optional] 

## Example

```python
from dscc.models.device_type4enclosure_cdm_details import DeviceType4enclosureCdmDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4enclosureCdmDetails from a JSON string
device_type4enclosure_cdm_details_instance = DeviceType4enclosureCdmDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4enclosureCdmDetails.to_json())

# convert the object into a dict
device_type4enclosure_cdm_details_dict = device_type4enclosure_cdm_details_instance.to_dict()
# create an instance of DeviceType4enclosureCdmDetails from a dict
device_type4enclosure_cdm_details_from_dict = DeviceType4enclosureCdmDetails.from_dict(device_type4enclosure_cdm_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


