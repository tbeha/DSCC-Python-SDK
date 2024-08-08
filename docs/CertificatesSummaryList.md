# CertificatesSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CertificatesList]**](CertificatesList.md) |  | [optional] 
**page_limit** | **int** | Page Limit | [optional] 
**page_offset** | **int** | Page Offset | [optional] 
**request_uri** | **str** | requestUri for detailed certificates object | [optional] 
**total** | **int** | Number of certificates | [optional] 

## Example

```python
from dscc.models.certificates_summary_list import CertificatesSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of CertificatesSummaryList from a JSON string
certificates_summary_list_instance = CertificatesSummaryList.from_json(json)
# print the JSON string representation of the object
print(CertificatesSummaryList.to_json())

# convert the object into a dict
certificates_summary_list_dict = certificates_summary_list_instance.to_dict()
# create an instance of CertificatesSummaryList from a dict
certificates_summary_list_from_dict = CertificatesSummaryList.from_dict(certificates_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


