import json
import requests

def getData(url):

    txnId = url.replace("https://whale-alert.io", "")

    if(txnId[len(txnId)-2] == '/'):
        txnId = txnId.replace("/1", "")

    whaleUrl = "https://api.whale-alert.io/v1" + txnId + "?api_key=DhXYQnc58hH39P34zaSymBixjjhobBLk";

    r = requests.get(whaleUrl)

    content = r.json()

    #print(content)

    from_owner = ""
    to_owner = ""

    try:
        from_owner = content['transactions'][0]['from']['owner']
    except:
        from_owner = "Unknown wallet"

    try:
        to_owner = content['transactions'][0]['to']['owner']
    except:
        to_owner = "Unknown wallet"

    blockchain = content['transactions'][0]['blockchain']
    symbol = content['transactions'][0]['symbol']
    hash = content['transactions'][0]['hash']

    from_address = content['transactions'][0]['from']['address']

    to_address = content['transactions'][0]['to']['address']

    timestamp = content['transactions'][0]['timestamp']
    amount = content['transactions'][0]['amount']
    amount_usd = content['transactions'][0]['amount_usd']

    title = f"{amount} {symbol} worth {amount_usd} USD transferred from {from_owner} to {to_owner}"

    resp = {
        "title" : title,
        "blockchain" : blockchain,
        "symbol" : symbol,
        "hash" : hash,
        "from" : from_address,
        "from_owner" : from_owner,
        "to" : to_address,
        "to_owner" : to_owner,
        "timestamp" : timestamp,
        "amount" : amount,
        "amount_usd" : amount_usd
    }

    return json.dumps(resp)


#s = getData('https://whale-alert.io/transaction/ethereum/f6f20756cd6dc7d69cf2cac0733a1081ebba2f3eec76db857e7864f3255ad3b4', "tttt")
#print(s)
