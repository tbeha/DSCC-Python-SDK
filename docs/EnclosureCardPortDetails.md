# EnclosureCardPortDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dc4data** | [**EcpDc4data**](EcpDc4data.md) |  | [optional] 
**dcsdata** | [**EcpDcsdata**](EcpDcsdata.md) |  | [optional] 
**disabled** | **bool** |  | [optional] 
**displayname** | **str** |  | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**element_status_code** | **str** | Enclosure status code | [optional] 
**enclosure_card_device_id** | **int** |  | [optional] 
**enclosure_card_id** | **str** | UID for the resource | [optional] 
**enclosure_card_port_id** | **int** | Numeric ID of the resource | [optional] 
**enclosure_card_port_type** | **str** |  | [optional] 
**enclosure_device_id** | **int** |  | [optional] 
**enclosure_id** | **str** | Parent UID of the resource | [optional] 
**enclosure_name** | **str** | Name of the enclosure | [optional] 
**enclosure_type** | [**EnclosureTypeSingle**](EnclosureTypeSingle.md) |  | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource | [optional] 
**link_speed** | **str** | Name of the enclosure | [optional] 
**locate_enabled** | **bool** | Indicates if the locate beacon is enabled or not | [optional] 
**loop_a** | **bool** |  | [optional] 
**loop_index** | **int** |  | [optional] 
**node_port** | [**EncPortPosition**](EncPortPosition.md) |  | [optional] 
**os_display_name** | **str** |  | [optional] 
**port_wwn** | **str** |  | [optional] 
**request_uri** | **str** | resourceUri for detailed enclosure fan object | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure fan object | [optional] 
**sfp** | [**FcPortSfpSingle**](FcPortSfpSingle.md) |  | [optional] 
**system_id** | **str** | SystemId/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.enclosure_card_port_details import EnclosureCardPortDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EnclosureCardPortDetails from a JSON string
enclosure_card_port_details_instance = EnclosureCardPortDetails.from_json(json)
# print the JSON string representation of the object
print(EnclosureCardPortDetails.to_json())

# convert the object into a dict
enclosure_card_port_details_dict = enclosure_card_port_details_instance.to_dict()
# create an instance of EnclosureCardPortDetails from a dict
enclosure_card_port_details_from_dict = EnclosureCardPortDetails.from_dict(enclosure_card_port_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


