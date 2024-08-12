# TrustedCertificatesSummaryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TrustedCertificatesList]**](TrustedCertificatesList.md) |  | [optional] 
**page_limit** | **int** | Page Limit | [optional] 
**page_offset** | **int** | Page Offset | [optional] 
**request_uri** | **str** | requestUri for detailed certificates object | [optional] 
**total** | **int** | Number of trusted certificates | [optional] 

## Example

```python
from dscc.models.trusted_certificates_summary_list import TrustedCertificatesSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedCertificatesSummaryList from a JSON string
trusted_certificates_summary_list_instance = TrustedCertificatesSummaryList.from_json(json)
# print the JSON string representation of the object
print(TrustedCertificatesSummaryList.to_json())

# convert the object into a dict
trusted_certificates_summary_list_dict = trusted_certificates_summary_list_instance.to_dict()
# create an instance of TrustedCertificatesSummaryList from a dict
trusted_certificates_summary_list_from_dict = TrustedCertificatesSummaryList.from_dict(trusted_certificates_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


