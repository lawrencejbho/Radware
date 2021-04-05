import global_config
import requests, json
from bs4 import BeautifulSoup

def get_sessiontoken():

    url = "https://radware-public.okta.com/api/v1/authn"

    payload= {
        "username": global_config.username,
        "password": global_config.password,
        "options": {
        "multiOptionalFactorEnroll": "true",
        "warnBeforePasswordExpired": "true"
            }
        }

    headers = {
    'Content-Type': 'application/json',
    'Cookie': 'DT=DI07MLV__cbRRCIYs3Z0nQNIQ; JSESSIONID=7CFE7D47FB23DC4CA65DB04CB44F7B0A; proximity_5e67cdbc383c2cf0195ea87054080e59=BLfSD4JPDNg2ODCSXHYTmFfC9uWB5srAKrMI7AZiAtpGRdq6BYxbWERufGtxj515UIX8nid3R7FlUapuwCdFAHWLbd7zILm4xNeyY5pLMh+WndUACzvI8z63SyrGS0XLMHPmK0vwn5gECw2B32TR+LnSJhVRKBwN9tlwEl9M3kX8ufySPgmpc+qERB2eG7/P'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))     #needs json.dumps for POST
    parse_json = json.loads(response.text)
    sessiontoken = parse_json['sessionToken']
    return(sessiontoken)

def get_sessionidentifier(sessiontoken):
    url = "https://radware-public.okta.com/oauth2/aus7ky2d5wXwflK5N1t7/v1/authorize?client_id=M1Bx6MXpRXqsv3M1JKa6&nonce=n-0S6_WzA2M&prompt=none&redirect_uri=https%3A%2F%2Fportal.radwarecloud.com&response_mode=form_post&response_type=token&scope=api_scope&sessionToken={}&state=parallel_af0ifjsldkj".format(sessiontoken)

    payload={}
    headers = {
    'Cookie': 'DT=DI07MLV__cbRRCIYs3Z0nQNIQ; JSESSIONID=D40171F6E5CA644DEE2B117B9C41554A; proximity_5e67cdbc383c2cf0195ea87054080e59=BLfSD4JPDNg2ODCSXHYTmFfC9uWB5srAKrMI7AZiAtpGRdq6BYxbWERufGtxj515UIX8nid3R7FlUapuwCdFAHWLbd7zILm4xNeyY5pLMh+WndUACzvI8z63SyrGS0XLMHPmK0vwn5gECw2B32TR+LnSJhVRKBwN9tlwEl9M3kX8ufySPgmpc+qERB2eG7/P; sid=102gSATzV-rRneCGyVUs6_51A; t=default'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    parse_html = BeautifulSoup(response.text, 'html.parser')
    access_token = parse_html.find("input", {'name':"access_token"})
    sessionidentifier = access_token.get('value')
    return(sessionidentifier)

def get_tenantid(sessionidentifier):
    url = "https://portal.radwarecloud.com/v1/users/me/summary"

    payload={}
    headers = {}
    headers['Authorization'] = 'Bearer ' + sessionidentifier     
    
    response = requests.request("GET", url, headers=headers, data=payload)
    parse_json = json.loads(response.text)
    tenantentityid = parse_json['tenantEntityId']
    print(tenantentityid)

def get_applications(sessionidentifier):
    url = "https://portal.radwarecloud.com/v1/gms/applications"

    payload={}
    authorization = 'Bearer ' + sessionidentifier
    headers = {
        'Authorization': authorization, 
        "requestEntityIds": global_config.tenantid,
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    parse_json = json.loads(response.text)
    print(parse_json)

def get_certificates(sessionidentifier):
    url = "https://portal.radwarecloud.com/v1/configuration/sslcertificates/"
    payload={}
    authorization = 'Bearer ' + sessionidentifier
    headers = {
        'Authorization': authorization, 
        "requestEntityIds": global_config.tenantid,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    parse_json = json.loads(response.text)
    for i in parse_json:
        print(i['fingerprint'])

def upload_certificate(sessionidentifier):
    url = "https://portal.radwarecloud.com/v1/configuration/sslcertificates/secret"
    payload = {
        "certificate": global_config.certificate,
        "chain": global_config.chain,
        "key": global_config.key,
        "passphrase": global_config.passphrase
    }
    authorization = 'Bearer ' + sessionidentifier
    headers = {
        'Authorization': authorization, 
        "requestEntityIds": global_config.tenantid,
        "selfSigned": 'true',
        "Content-Type": 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload)) 
    print(response.text)
    parse_json = json.loads(response.text)
    fingerprint = parse_json['fingerprint']
    print(fingerprint)

def upload_multiple_certificate(sessionidentifier):
    url = "https://portal.radwarecloud.com/v1/configuration/sslcertificates/secret"

# zip joins two lists together so we can iterate at the same time
    for i,j in zip(global_config.certificate_list, global_config.key_list):
        payload = {
            "certificate": i,
            "chain": global_config.chain,
            "key": j,
            "passphrase": global_config.passphrase
        }
        authorization = 'Bearer ' + sessionidentifier
        headers = {
            'Authorization': authorization, 
            "requestEntityIds": global_config.tenantid,
            "selfSigned": 'true',
            "Content-Type": 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=json.dumps(payload)) 
        print(response.text)
        parse_json = json.loads(response.text)
        fingerprint = parse_json['fingerprint']
        print(fingerprint)    

def delete_certificate(sessionidentifier):
    url = "https://portal.radwarecloud.com/v1/configuration/sslcertificates/{}".format(global_config.fingerprint)
    payload = {}
    authorization = 'Bearer ' + sessionidentifier
    headers = {
        'Authorization': authorization, 
        "requestEntityIds": global_config.tenantid,
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)
    print(response.text)