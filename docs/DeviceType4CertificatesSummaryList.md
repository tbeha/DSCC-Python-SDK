# DeviceType4CertificatesSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4certificatesList]**](DeviceType4certificatesList.md) |  | [optional] 
**page_limit** | **int** | Page Limit | [optional] 
**page_offset** | **int** | Page Offset | [optional] 
**request_uri** | **str** | requestUri for detailed certificates object | [optional] 
**total** | **int** | Number of certificates | [optional] 

## Example

```python
from dscc.models.device_type4_certificates_summary_list import DeviceType4CertificatesSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4CertificatesSummaryList from a JSON string
device_type4_certificates_summary_list_instance = DeviceType4CertificatesSummaryList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4CertificatesSummaryList.to_json())

# convert the object into a dict
device_type4_certificates_summary_list_dict = device_type4_certificates_summary_list_instance.to_dict()
# create an instance of DeviceType4CertificatesSummaryList from a dict
device_type4_certificates_summary_list_from_dict = DeviceType4CertificatesSummaryList.from_dict(device_type4_certificates_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


