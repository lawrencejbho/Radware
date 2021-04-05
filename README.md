# Radware-WAF

Python Script for Cloud WAF API user 
- pull main, global-config, and helper
- runs the same API calls in python3 and parses the html or json for subsequent calls


Radware Cloud WAF Postman Collection and Environment
- for POSTMAN
- scripts can be run for api user access to Cloud WAF
- includes - get, upload, create, update, delete 
- latency testing

Instructions:
        
1 – download Postman https://www.postman.com/downloads/ and install\
2 – download the collection and environment files in the Postman folder\
3 – import the collection and environment into Postman\
4 – make sure you have an API user on Cloud WAF\
5 – in Postman, load up your credentials (username/password) into the environment variables, also set your environment as Radware Cloud WAF\
6 – run get session token, get session identifier, get tenant ID.  The scripts automatically load the values as environment variables to be used for the next call.\
7 – Grab your application ID to view your existing apps and then run PUT requests to update.  Or you can run POST requests to create a new app or upload a new certificate.
