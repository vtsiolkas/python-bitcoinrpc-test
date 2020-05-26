import decimal
import json

responsedata = '{"result":[{"txid":"bee4f42c3ea5acb32bc521c3c30a6e6a8743a0730dce901f73675b9cc49874ea","vout":10,"address":"n3yDfK6mk2ytFdXRqoavBTJynrnrBGkE5y","label":"","scriptPubKey":"76a914f64a68da88b18ed8200edd6941461df6fb2aef0f88ac","amount":1.08401840,"confirmations":92,"spendable":true,"solvable":true,"desc":"pkh([f64a68da]037dbedcebf19e92d3d2f10846f3470797d7ba74f3faf111ab2fa94f77fd7e58d7)#h7qljegf","safe":true}],"error":null,"id":1}\n'

def EncodeDecimal(o):
    if isinstance(o, decimal.Decimal):
        return float(round(o, 8))
    raise TypeError(repr(o) + " is not JSON serializable")

response = json.loads(responsedata, parse_float=decimal.Decimal)

if "error" in response and response["error"] is None:
    debug = json.dumps(response["result"], default=EncodeDecimal)