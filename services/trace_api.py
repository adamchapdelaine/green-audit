import requests

def queryAPI(company_name):
    try: 
        requests.get()
    except requests.exceptions.RequestException:
        print("Exception")