import simplejson as json
import cherrypy
from cherrypy import expose

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

class nosql_service:

    @expose
    def pf_create_table(self, name):
        # creating a full table with all options specified.
        users = Table.create(name, schema=[
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
        
        # Wait for it.
        time.sleep(60)
        
        return json.dumps(name + " table created")

    @expose
    def pf_delete_table(self, name):
        Table(name).delete
        
        # Wait for it.
        time.sleep(60)
        
        return json.dumps(name + " table deleted")

    # future syntax
    @expose
    def pf_ddb_create_table(self, name):
        # creating a full table with all options specified.
        users = Table.create(name, schema=[
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

        # Wait for it.
        time.sleep(60)
        
        return json.dumps(name + " table created")

    @expose
    def pf_ddb_delete_table(self, name):
        Table(name).delete
        
        # Wait for it.
        time.sleep(60)
        
        return json.dumps(name + " table deleted")

cherrypy.quickstart(nosql_service())