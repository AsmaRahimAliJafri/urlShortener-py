import hashlib
import socket
import time
import uuid
import requests
import validators
from dbClient import urlMappingCollection

def main():
    inputUrl = 'https://www.google.com/search?sca_esv=0bc39af9d1d15b37&rlz=1C1VDKB_enUS1068US1068&sxsrf=ACQVn0_j64acu_lP21MJanRZg_aefmILlQ:1713106911584&q=cats&uds=AMwkrPuurAXqxNouqA_OXBEs5-yptF3T1Qw8YTSCYyR_ozQame5VYMs4cD6KcX2qUDLB9aMvPjYDcAfQru9GEaEMAy-avc9u6nGnxU0gz9-Hk1mt-esbODLJWl05z2zZy3wfugbnbyaFzoNvR1YWi42Lt7BMPnfpKM-Mc6rWHOJowpk7WV38xIg4iRcKZ65ZYN7xwQqInlZI4gZl-ruw3O2O4W6pYsW00Hj_aEBowgFwUIN2ed1sPaOW2HfFQq_dAtX3NNcK309wYpkOSbzwKQpjtVMTy3hwT4YVnq_Q97kepdx58ebyqmM&udm=2&prmd=ivsnmbtz&sa=X&ved=2ahUKEwjWjbXH_MGFAxWNlIkEHR-sCJsQtKgLegQIERAB&biw=1422&bih=650&dpr=1.35#vhid=zWdzdPdo-A-wdM&vssid=mosaic'

    if validators.url(inputUrl):
      print("Valid URL")
    else:
      print("URL not valid")

    #check for DNs resolution
    try:
      socket.gethostbyname(inputUrl.split("//")[-1].split('/')[0])
    except socket.gaierror:
      print("Domain unregistered or DNS resolution Failed")

      # testing HTTPs connection  - sometimes, the DNS might be registered but the page might not be served by the server or inernet might be off
    try:
          response = requests.get(inputUrl)
          if response.status_code == 200:
              print("URL is working and responsive")
          else:
              print("Server returned a response = ", response.status_code)
    except requests.RequestException as e:
          print("Unable to connect to the URL ", e)


    current_time = int(time.time())
    random_uuid = uuid.uuid4().hex
    combinedStr = f"{inputUrl}{current_time}{random_uuid}"
    unique_id = hashlib.sha256(combinedStr.encode()).hexdigest()
    print("This is the unique identifier = ", unique_id)  #generates a long string that is secure and less prone to collisons but is still pretty long

    if unique_id:
        urlMappingCollection.insert_one({"shortId":unique_id, "originalUrl":inputUrl })
    else:
        print("Some issue occured when generating uuid")
    print("mongodb after inserting= ", urlMappingCollection.find())

    # adding base URL to the shortended UUID
    baseUrl = 'http://127.0.0.1:5000/'
    shortenedUrl = baseUrl + unique_id
    print(shortenedUrl)


if __name__ == "__main__":
    main()











