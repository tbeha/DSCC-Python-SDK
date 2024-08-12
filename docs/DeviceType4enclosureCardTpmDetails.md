# DeviceType4enclosureCardTpmDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**enclosure_card_id** | **int** | ID of enclosure card. | [optional] 
**enclosure_card_tpm_id** | **int** | ID of enclosure card Tpm Id. | [optional] 
**enclosure_card_tpm_type** | **str** | Enclosure Card Tpm Type. | [optional] 
**enclosure_card_uid** | **str** | Unique Identifier of the enclosure card. | [optional] 
**enclosure_id** | **int** | ID of the enclosure | [optional] 
**enclosure_uid** | **str** | Unique Identifier of the enclosure. | [optional] 
**family** | **str** | Family of TPM | [optional] 
**fw_version** | **str** | Firmware Version | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | id | [optional] 
**level** | **int** | Level of TPM | [optional] 
**manufacturing** | [**DeviceType4ManufacturingSingle**](DeviceType4ManufacturingSingle.md) |  | [optional] 
**revision** | **str** | Revision firmware of the TPM card | [optional] 
**system_id** | **str** | systemId | [optional] 
**type** | **str** | type | [optional] 
**vendor** | **str** | vendor information | [optional] 

## Example

```python
from dscc.models.device_type4enclosure_card_tpm_details import DeviceType4enclosureCardTpmDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4enclosureCardTpmDetails from a JSON string
device_type4enclosure_card_tpm_details_instance = DeviceType4enclosureCardTpmDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4enclosureCardTpmDetails.to_json())

# convert the object into a dict
device_type4enclosure_card_tpm_details_dict = device_type4enclosure_card_tpm_details_instance.to_dict()
# create an instance of DeviceType4enclosureCardTpmDetails from a dict
device_type4enclosure_card_tpm_details_from_dict = DeviceType4enclosureCardTpmDetails.from_dict(device_type4enclosure_card_tpm_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


