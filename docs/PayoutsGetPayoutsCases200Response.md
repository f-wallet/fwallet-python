# PayoutsGetPayoutsCases200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApprovalCase]**](ApprovalCase.md) |  | 

## Example

```python
from fwallet.models.payouts_get_payouts_cases200_response import PayoutsGetPayoutsCases200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutsGetPayoutsCases200Response from a JSON string
payouts_get_payouts_cases200_response_instance = PayoutsGetPayoutsCases200Response.from_json(json)
# print the JSON string representation of the object
print(PayoutsGetPayoutsCases200Response.to_json())

# convert the object into a dict
payouts_get_payouts_cases200_response_dict = payouts_get_payouts_cases200_response_instance.to_dict()
# create an instance of PayoutsGetPayoutsCases200Response from a dict
payouts_get_payouts_cases200_response_from_dict = PayoutsGetPayoutsCases200Response.from_dict(payouts_get_payouts_cases200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


