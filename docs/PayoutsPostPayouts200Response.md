# PayoutsPostPayouts200Response

Result of a payout request. Funds are immediately held (moved from wallet to suspense) and an approval case is created. The payout is not settled until an approver (who is not the requestor) approves it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payout_case_id** | **UUID** | Approval case ID. Use this to approve or reject the payout. | 
**hold_journal_entry_id** | **UUID** | Journal entry recording the balance hold (funds moved to suspense) | 
**wallet_id** | **UUID** | Wallet the funds were held from | 
**amount** | **str** | Held amount in smallest currency unit | 
**currency_code** | **str** |  | 
**status** | **str** | Always &#39;pending_approval&#39; — payout requires maker-checker approval before settlement | 

## Example

```python
from fwallet.models.payouts_post_payouts200_response import PayoutsPostPayouts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutsPostPayouts200Response from a JSON string
payouts_post_payouts200_response_instance = PayoutsPostPayouts200Response.from_json(json)
# print the JSON string representation of the object
print(PayoutsPostPayouts200Response.to_json())

# convert the object into a dict
payouts_post_payouts200_response_dict = payouts_post_payouts200_response_instance.to_dict()
# create an instance of PayoutsPostPayouts200Response from a dict
payouts_post_payouts200_response_from_dict = PayoutsPostPayouts200Response.from_dict(payouts_post_payouts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


