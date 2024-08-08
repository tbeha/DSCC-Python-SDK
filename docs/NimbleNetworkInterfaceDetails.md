# NimbleNetworkInterfaceDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_name_or_serial** | **str** | Name or serial of the array where the interface is hosted. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**controller_id** | **str** | Identifier of the controller where the interface is hosted. A 42 digit hexadecimal number. | [optional] 
**ip_list** | [**IpListInfo**](IpListInfo.md) | Information about the Fibre Channel link at which interface is operating. | [optional] 
**is_present** | **bool** | Whether this interface is present on this controller. Possible values: true, false. | [optional] 
**link_speed** | **str** | Speed of the link. Possible values: link_speed_unknown, link_speed_10M, link_speed_100M, link_speed_1000M, link_speed_10000M. | [optional] 
**link_status** | **str** | Status of the link. Possible values: link_status_unknown, link_status_down, link_status_up. | [optional] 
**mac** | **str** | MAC address of the interface. Mac address of an interface. | [optional] 
**max_link_speed** | **str** | Maximum speed of the link. Possible values: link_speed_unknown, link_speed_10M, link_speed_100M, link_speed_1000M, link_speed_10000M. | [optional] 
**mtu** | **int** | MTU on the link. | [optional] 
**nic_type** | **str** | Interface type. Possible values: nic_type_unknown, nic_type_tp, nic_type_sfp. | [optional] 
**partial_response_ok** | **bool** | Port response. | [optional] 
**port** | **int** | Port number for this interface. | [optional] 
**slot** | **int** | Slot number for this interface. | [optional] 

## Example

```python
from dscc.models.nimble_network_interface_details import NimbleNetworkInterfaceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNetworkInterfaceDetails from a JSON string
nimble_network_interface_details_instance = NimbleNetworkInterfaceDetails.from_json(json)
# print the JSON string representation of the object
print(NimbleNetworkInterfaceDetails.to_json())

# convert the object into a dict
nimble_network_interface_details_dict = nimble_network_interface_details_instance.to_dict()
# create an instance of NimbleNetworkInterfaceDetails from a dict
nimble_network_interface_details_from_dict = NimbleNetworkInterfaceDetails.from_dict(nimble_network_interface_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


