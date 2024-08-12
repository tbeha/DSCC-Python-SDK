# DeviceType4enclosureCardPciDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**enclosure_card_id** | **int** | ID of enclosure card. | [optional] 
**enclosure_card_pci_type** | **str** | Enclosure card Pci type. | [optional] 
**enclosure_card_uid** | **str** | Unique Identifier of the enclosure card. | [optional] 
**enclosure_id** | **int** | ID of the enclosure | [optional] 
**enclosure_uid** | **str** | Unique Identifier of the enclosure. | [optional] 
**fw_version** | **str** | Firmware Version | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | id | [optional] 
**manufacturing** | [**DeviceType4ManufacturingSingle**](DeviceType4ManufacturingSingle.md) |  | [optional] 
**port_count** | **int** | Number of ports on enclosure card PCI. | [optional] 
**revision** | **str** | Revision firmware of the PCI card | [optional] 
**slot** | **int** | Enclosure card PCI slot number. | [optional] 
**system_id** | **str** | systemId | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.device_type4enclosure_card_pci_details import DeviceType4enclosureCardPciDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4enclosureCardPciDetails from a JSON string
device_type4enclosure_card_pci_details_instance = DeviceType4enclosureCardPciDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4enclosureCardPciDetails.to_json())

# convert the object into a dict
device_type4enclosure_card_pci_details_dict = device_type4enclosure_card_pci_details_instance.to_dict()
# create an instance of DeviceType4enclosureCardPciDetails from a dict
device_type4enclosure_card_pci_details_from_dict = DeviceType4enclosureCardPciDetails.from_dict(device_type4enclosure_card_pci_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


