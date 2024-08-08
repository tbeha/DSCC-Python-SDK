# PoolRebalanceMigStatus

Status of data rebalance operations in a pool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_data_migration_status** | [**List[ArrayMigStatus]**](ArrayMigStatus.md) | Data migration status for a list of arrays in the pool. | [optional] 
**id** | **str** | Unique ID of the pool. | [optional] 
**name** | **str** | Name of the Pool. | [optional] 
**pool_avg_space_utilization** | **int** | Average space utilization for the arrays in the pool. | [optional] 

## Example

```python
from dscc.models.pool_rebalance_mig_status import PoolRebalanceMigStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PoolRebalanceMigStatus from a JSON string
pool_rebalance_mig_status_instance = PoolRebalanceMigStatus.from_json(json)
# print the JSON string representation of the object
print(PoolRebalanceMigStatus.to_json())

# convert the object into a dict
pool_rebalance_mig_status_dict = pool_rebalance_mig_status_instance.to_dict()
# create an instance of PoolRebalanceMigStatus from a dict
pool_rebalance_mig_status_from_dict = PoolRebalanceMigStatus.from_dict(pool_rebalance_mig_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


