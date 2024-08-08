# DeviceType4EnclosureConnectorsSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4enclosureConnectorsList]**](DeviceType4enclosureConnectorsList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | resourceUri for detailed enclosure connectors object | [optional] 
**total** | **int** | number of enclosure connetcors | [optional] 

## Example

```python
from dscc.models.device_type4_enclosure_connectors_summary_list import DeviceType4EnclosureConnectorsSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosureConnectorsSummaryList from a JSON string
device_type4_enclosure_connectors_summary_list_instance = DeviceType4EnclosureConnectorsSummaryList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosureConnectorsSummaryList.to_json())

# convert the object into a dict
device_type4_enclosure_connectors_summary_list_dict = device_type4_enclosure_connectors_summary_list_instance.to_dict()
# create an instance of DeviceType4EnclosureConnectorsSummaryList from a dict
device_type4_enclosure_connectors_summary_list_from_dict = DeviceType4EnclosureConnectorsSummaryList.from_dict(device_type4_enclosure_connectors_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


