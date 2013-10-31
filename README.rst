####
nosql-service
####
Extracted from Amazon's Boto version 2.13.3

Released: 29-October-2013

************
Introduction
************

nosql-service interfaces to DynamoDB v2 on Amazon Web Services

nosql-service supports:

* Database

  * Amazon DynamoDB

Works with Python 2.6 or greater

************
Installation
************

Install:

::

	$ git clone https://github.com/pgplayfirst/nosql-service.git
	$ cd nosql-service
	$ python setup.py install
	$ vim ~/.boto

File contents:	
	[Credentials]
	aws_access_key_id = <access_key_here>
	aws_secret_access_key = <secret_key_here>

************
Web server
************

Install:
	pip install cherrypy
	
Start:
	python nosql_service-cherry.py
	
************
Tests
************

From nosql-service directory:

pip install mock
pip install httpretty
pip install sure

python tests/integration/dynamodb2/test_highlevel.py

python tests/unit/test_connection.py

Yields:

"http_proxy environment variable does not specify a port, using default

Ran 18 tests in 0.232s

OK"

Create a users table on the credentialed DynamoDB Amazon instance for the chosen region:

python tests/createtable_test.py
