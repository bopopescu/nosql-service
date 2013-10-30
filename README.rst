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
	
	[Credentials]
	aws_access_key_id = <access_key_here>
	aws_secret_access_key = <secret_key_here>

************
Test
************

From nosql-service directory:

python tests/integration/dynamodb2/test_highlevel.py