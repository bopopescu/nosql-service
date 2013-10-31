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
	
When running this is the view in a separate shell window:
"[31/Oct/2013:15:37:51] ENGINE Listening for SIGHUP.
[31/Oct/2013:15:37:51] ENGINE Listening for SIGTERM.
[31/Oct/2013:15:37:51] ENGINE Listening for SIGUSR1.
[31/Oct/2013:15:37:51] ENGINE Bus STARTING
CherryPy Checker:
The Application mounted at '' has an empty config.

[31/Oct/2013:15:37:51] ENGINE Started monitor thread '_TimeoutMonitor'.
[31/Oct/2013:15:37:51] ENGINE Started monitor thread 'Autoreloader'.
[31/Oct/2013:15:37:52] ENGINE Serving on 127.0.0.1:8080
[31/Oct/2013:15:37:52] ENGINE Bus STARTED"
	
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
