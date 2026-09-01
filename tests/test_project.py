import pandas as pd

def test_claim_schema():
    df = pd.DataFrame({"claim_id":["1"],"claim_status":["Denied"],
                       "denial_reason":["Authorization"],"payer":["A"],
                       "payment_amount":[0]})
    assert {"claim_id","claim_status","denial_reason","payer","payment_amount"}.issubset(df.columns)
