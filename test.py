from bitcoinrpc.authproxy import AuthServiceProxy
from decimal import Decimal, getcontext

getcontext().prec = 8

SATOSHIS_PER_BITCOIN = 100000000

FULL_NODE_RPC_USER = ''
FULL_NODE_RPC_PASSWORD = ''
FULL_NODE_URL = '127.0.0.1:18332'


def get_rpc_connection():
    return AuthServiceProxy("http://{}:{}@{}".format(
        FULL_NODE_RPC_USER,
        FULL_NODE_RPC_PASSWORD,
        FULL_NODE_URL
    ))


def query_funds(address):
    """Queries the node for the funds of a given address
    """

    rpc_connection = get_rpc_connection()
    unspent = rpc_connection.listunspent(1, 9999999, [address])

    amount = Decimal(0.0)
    if unspent:
        for unsp in unspent:
            amount += unsp['amount']

    return amount


def query_unspent(addresses):
    """Queries the node for the unspent of a list of addresses

    Returns {address1: {unspent: N, amount: N.nn}, ....}
    """

    rpc_connection = get_rpc_connection()
    unspent = rpc_connection.listunspent(1, 9999999, addresses)

    addr_unspent = {}
    for unsp in unspent:
        addr = unsp['address']
        if addr not in addr_unspent:
            addr_unspent[addr] = {'unspent': 1, 'amount': unsp['amount']}
        else:
            addr_unspent[addr]['unspent'] += 1
            addr_unspent[addr]['amount'] += unsp['amount']

    for addr in addresses:
        if addr not in addr_unspent:
            addr_unspent[addr] = {'unspent': 0, 'amount': Decimal(0)}

    return addr_unspent


if __name__ == '__main__':
    print(query_funds('n3yDfK6mk2ytFdXRqoavBTJynrnrBGkE5y'))