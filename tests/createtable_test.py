import time

import sys
sys.path.append('/Users/pgregg/nosql-service')
sys.path.append('/Users/pgregg/nosql-service/tests')
sys.path.append('/Users/pgregg/nosql-service/tests/integration')
sys.path.append('/Users/pgregg/nosql-service/tests/integration/dynamodb2')

import unittest
from boto.dynamodb2 import exceptions
from boto.dynamodb2.fields import HashKey, RangeKey, KeysOnlyIndex
from boto.dynamodb2.items import Item
from boto.dynamodb2.table import Table
from boto.dynamodb2.types import NUMBER
    
dynamodb = True

# Test creating a full table with all options specified.
users = Table.create('users', schema=[
    HashKey('username'),
    RangeKey('friend_count', data_type=NUMBER)
], throughput={
    'read': 5,
    'write': 5,
}, indexes=[
    KeysOnlyIndex('LastNameIndex', parts=[
        HashKey('username'),
        RangeKey('last_name')
    ]),
])
