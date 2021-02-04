The whole solution is implemented in python version 3.8.5

### How to Install
All the requirements can be installed as

pip install -r requirements.txt

### How to execute

Console/REST API server can be started as 

python kheiron_main.py 

This will show 2 options 

1. console mode 

2. Rest server mode - Reset server is running on port 8085

#####Eg: Console 
Which mode you want to start the application (1.Console/2.Rest Server) >1\
*******Kheiron Calculator (Prefix/Infix)********* 
 
Type q to exit 

####Eg: REST API 

curl -X POST \
  http://127.0.0.1:8085/kheiron/api/v1/calculator \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 2a936191-ed45-6133-2aea-0eb185f41c1b' \
  -d '{
	"expression": "( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )"
}'

###Testing
Calculator package test cases are located in kheiron/calculator_test.py 

REST server related tests are located in test_rest_server.py
