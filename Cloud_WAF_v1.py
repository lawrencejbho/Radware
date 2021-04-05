import requests, json
from bs4 import BeautifulSoup

username = "lawrence.jb.ho1@gmail.com"
password = "Radware123@"

#run get_tenantid if you don't already know this 
tenantid = "607b9775-a04a-4efa-ba97-228909abc300"   

#for certificates 
certificate = "-----BEGIN CERTIFICATE-----\nMIIExjCCAq6gAwIBAgIUXLyeTE6/6Ybf9SuFktKnyUrHt/UwDQYJKoZIhvcNAQEL\nBQAwXjELMAkGA1UEBhMCVVMxCzAJBgNVBAgMAkNBMQswCQYDVQQHDAJTRjEQMA4G\nA1UECgwHUmFkd2FyZTELMAkGA1UECwwCU0UxFjAUBgNVBAMMDWxhd3JlbmNlLXJv\nb3QwHhcNMjAwODAyMjIzNzMzWhcNMjIwODAyMjIzNzMzWjCBhTELMAkGA1UEBhMC\nVVMxCzAJBgNVBAgMAkNBMQswCQYDVQQHDAJTRjEQMA4GA1UECgwHUmFkd2FyZTEL\nMAkGA1UECwwCU0UxFTATBgNVBAMMDGxhd3JlbmNlLmNvbTEmMCQGCSqGSIb3DQEJ\nARYXbGF3cmVuY2UuaG9AcmFkd2FyZS5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IB\nDwAwggEKAoIBAQC8Qb6ivqwLuro6B/TwaCvZoThkKam8K/kyLKlB0Zv0dThISMQB\nBfK2OdINCvxNMplvHR//pBvH2DEvzgf8ia1UIStVS8jMDsEZtZXO0ZYIAkkWoBub\nIX3e+fxIzTY/E5EyIj0Fhs5pBExL1Rtyy8NoXdE/NQc/GMs9I1k1IonwjDiQdbsu\n5lI4brLEAZumf8AJBSBohL+CP5mmTEdBtUCsKEg8U/6Qr35y1g2/vqoRgqGR0aGO\ndDv+l2yChEZwF0BF7Euzj6MQpQipNh0J45mdEOWrD7D1L6HLT0k+IvZTKydhuyAt\nKOqFBJXo6CX6fwuaAaBAOVa1V+l/aaKGkETnAgMBAAGjVDBSMB8GA1UdIwQYMBaA\nFArOeI8LjmxySyl/ysb4CUnbPvmQMAkGA1UdEwQCMAAwCwYDVR0PBAQDAgTwMBcG\nA1UdEQQQMA6CDGxhd3JlbmNlLmNvbTANBgkqhkiG9w0BAQsFAAOCAgEAYp58SwWd\nLmNWnJALTfVcLzRbsmj6SC7kq9Pf1slIod2dqB6UuY49l05YUzZmMPBZaUTvQKht\n8jnR24WLkKYyFrL9mumS2h26VNhoW+wCITYe6CbfsfcooAfnay2KvIT9UYBxQyMm\naC7hL5cZuNLQVEfhBWwNRSsV3JzyceNbvKSX3rUs513oh6QN48a4b8XPCiRFI2uA\nJVP0L06MJeklhysXMw/0IIIBPjDPUso8f46tBl3YZ0XfzcB3jFA7OeDcRkhY9Cmc\nIZbLtTXWJ4lJ3ir1FaBdhAcwFZPh20ytXGoDtXBGemnHWN0Y4GCA8eh+6qZYh/gd\nZyMDXJ9p4uyUd9oMFd9RvIEkHdFHIJ+8IUP10muzOVmYSMsOgvto861BvOzPeMKL\nyyVM3uuDgRjZJalQxIqYOjxCNtLz2baurEAIQA3GcxnfBSfk++NjWmgi/GAQS+gm\nNukMObBt47yx82dKYU5STkx35n4DRDAtrP7GoR1KR89JBYzg+1O3Z4AZdjIsBC4B\noxroNn9LPFi3Lon1xoZCYzHgAFk9vuEuTJ3ZrrB0YfBIm5NQAM2edpiBRdfeVptv\n82xdN3Bj+FfKj7wCdUNrg1aOPSVpvTFldyuYEpzSoMfeNp2FmqmUZlCbVRVPSgjS\nxpVdwXE58XhXlZbxmZc930xS0VXpgobPCaE=\n-----END CERTIFICATE-----\n"
chain = ""
key = "-----BEGIN PRIVATE KEY-----\nMIIEwAIBADANBgkqhkiG9w0BAQEFAASCBKowggSmAgEAAoIBAQC8Qb6ivqwLuro6\nB/TwaCvZoThkKam8K/kyLKlB0Zv0dThISMQBBfK2OdINCvxNMplvHR//pBvH2DEv\nzgf8ia1UIStVS8jMDsEZtZXO0ZYIAkkWoBubIX3e+fxIzTY/E5EyIj0Fhs5pBExL\n1Rtyy8NoXdE/NQc/GMs9I1k1IonwjDiQdbsu5lI4brLEAZumf8AJBSBohL+CP5mm\nTEdBtUCsKEg8U/6Qr35y1g2/vqoRgqGR0aGOdDv+l2yChEZwF0BF7Euzj6MQpQip\nNh0J45mdEOWrD7D1L6HLT0k+IvZTKydhuyAtKOqFBJXo6CX6fwuaAaBAOVa1V+l/\naaKGkETnAgMBAAECggEBAKyIWI3Qz97EGG6c4jf+UMnYvtTVdjD14CHC2rBuyU6G\nq7lbrv79E488eKzpd4fMquAxwiTJo4hJM/MLETi6eTcUWyGGHhYeI41LZWuxm53l\nclShEgvf6vsTAss5/9BZP4XB6UkKXlvSy5XoToqsAn/BE8eo8uY58/IpVlWjPOZO\nGNQas8l1b7wI9W+0D08E9LsV0rYlYZp/f5IDPzNLGiBwyEnVRHe/AyIxJvio2mJt\nmttU77ciLCovQcJ25pnwJAE0UFqChZwqXuZpH+/sTeFP9BMQLv8YFdzHTPuNniRo\nr7qIPhftYrUwhUN4vJ5Y7GSDZ2ZpjDa9enj1vetksUkCgYEA7aSue994qPrExT1B\nsjb0GxMxFgnms0jcXi/nWpKzYLCeonyvk9+44z1Cgd3RZfcvBWvAgXduK76Qe0NE\n6lBnLS2MIyQs1oIPOy6U5W8dqEnNYO4rjx5C9K5shZHmmAXcDtFvZuJ435MWDOsa\nB/twpQ68Ezte0xGnyez3C8PGeXMCgYEAysx2M8Nn6RuY7rZzMlX+FdTZbtwCud3J\n1wjYCom4ayUjFmZjvJoclTqCwLAHtEc7rBozq5L5E0dsqxezN/5uVsx0w4V2ziXq\nEw08epSYpRsqXZxh3u9LneFeLEAjyzsPGlKwsUPr6TqJiDP0zxgh9xK1O8G9x7Wq\nzrZQI1yKOb0CgYEAq47HqAWcReFDTGD8nHuvnhwsw4xCUAu5iwVqL6jYdmULIKKC\n3m4UO3huGvLXyJS6DV/Miap+jnX0OAhIKCADXEoVcQkclX8vH7pxI3EkJ+mfqupF\n5/wguiNxlLvPjNAuHUR0+AFm4YB92rWfBUQv/fi1Le0ed6G3T78SWhvrnKECgYEA\nudm+yZledQbRlJKn541fGWrDCRGffe5/tw1nz+B+ndKe4TxcUs95Olkw0p1/sftF\n+Gbay3YZxU1DjVhe6gXF4M3mg/if9DRS27rZngzoBwdqP/e8ya3LQpjy0OLG6szo\n/lqhixKP9GGtAKF8zP10wxTl+imHXqpiKqZxsrZwBpECgYEA2R08Y+bqHYqzdfWv\nv2HbIoiiWkR7yvGkJ7pi6/Rq4zprh9cDBEQ/gdIvd6UfnhVNh7kAZKiKLSzSVxkV\nbM+6NXfjAKoi649XgF9mV/R5n9ofts/Q3NBuIoXEu0qq/TN9RFmW05sEMzsyVjUB\nsZ25L25voiCCpJKQSNcm57YvhJA=\n-----END PRIVATE KEY-----\n"
passphrase = ""
fingerprint = "65A303E33B4699A72D749AA2FCF3D32CE1FEA967"

#for specific calls to an application that aren't shown here
applicationID = ""



def get_sessiontoken():

    url = "https://radware-public.okta.com/api/v1/authn"

    payload= {
        "username": username,
        "password": password,
        "options": {
        "multiOptionalFactorEnroll": "true",
        "warnBeforePasswordExpired": "true"
            }
        }

    headers = {
    'Content-Type': 'application/json',
    'Cookie': 'DT=DI07MLV__cbRRCIYs3Z0nQNIQ; JSESSIONID=7CFE7D47FB23DC4CA65DB04CB44F7B0A; proximity_5e67cdbc383c2cf0195ea87054080e59=BLfSD4JPDNg2ODCSXHYTmFfC9uWB5srAKrMI7AZiAtpGRdq6BYxbWERufGtxj515UIX8nid3R7FlUapuwCdFAHWLbd7zILm4xNeyY5pLMh+WndUACzvI8z63SyrGS0XLMHPmK0vwn5gECw2B32TR+LnSJhVRKBwN9tlwEl9M3kX8ufySPgmpc+qERB2eG7/P'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))     #use json.dumnps here so you can use variables in the dictionary
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
        "requestEntityIds": tenantid,
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
        "requestEntityIds": tenantid,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    parse_json = json.loads(response.text)
    for i in parse_json:
        print(i['fingerprint'])

def upload_certificate(sessionidentifier):
    url = "https://portal.radwarecloud.com/v1/configuration/sslcertificates/secret"
    payload = {
        "certificate": certificate,
        "chain": chain,
        "key": key,
        "passphrase": passphrase
    }
    authorization = 'Bearer ' + sessionidentifier
    headers = {
        'Authorization': authorization, 
        "requestEntityIds": tenantid,
        "selfSigned": 'true',
        "Content-Type": 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload)) 
    print(response.text)
    parse_json = json.loads(response.text)
    fingerprint = parse_json['fingerprint']
    print(fingerprint)

def delete_certificate(sessionidentifier):
    url = "https://portal.radwarecloud.com/v1/configuration/sslcertificates/{}".format(fingerprint)
    payload = {}
    authorization = 'Bearer ' + sessionidentifier
    headers = {
        'Authorization': authorization, 
        "requestEntityIds": tenantid,
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)
    print(response.text)


sessionidentifier = get_sessionidentifier(get_sessiontoken())


#Use to get your tenantid for future calls

get_tenantid(sessionidentifier)    

#A sample call that you can run after getting the tenant id

#get_applications(sessionidentifier)

#Use this to see the fingerprints of your certificates

get_certificates(sessionidentifier)

#Uploads the certificate, also outputs the fingerprint which you will need later if deleting a certificate

#upload_certificate(sessionidentifier)


#Deletes the certificate

#delete_certificate(get_sessionidentifier(get_sessiontoken()))
