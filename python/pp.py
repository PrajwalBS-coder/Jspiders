import requests
try:
    r=requests.get("https://chatgpt.com/c/67595793-03cc-8011-8dc0-11ed4ac6be39/key='khadhs'/usn='legendamin008'&passwd='123456'")
    if r.status_code!='200':
        raise Exception

except Exception as e :
    print("An error occurred: ",e)