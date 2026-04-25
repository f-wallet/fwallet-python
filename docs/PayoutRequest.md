# PayoutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **UUID** | Wallet to withdraw from | 
**amount** | **float** | Payout amount in human-readable units | 
**currency_code** | **str** | Payout currency (must match wallet currency) | 
**payout_method** | **str** | How the payout should be delivered: &#39;momo&#39; (Mobile Money disbursement), &#39;bank&#39; (bank transfer), or &#39;cash&#39; (cash at branch) | 
**requested_by** | **str** | ID of the person requesting the payout. Cannot be the same person who approves it (maker-checker). | 

## Example

```python
from fwallet.models.payout_request import PayoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutRequest from a JSON string
payout_request_instance = PayoutRequest.from_json(json)
# print the JSON string representation of the object
print(PayoutRequest.to_json())

# convert the object into a dict
payout_request_dict = payout_request_instance.to_dict()
# create an instance of PayoutRequest from a dict
payout_request_from_dict = PayoutRequest.from_dict(payout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


