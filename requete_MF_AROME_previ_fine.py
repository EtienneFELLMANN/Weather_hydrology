"script pour tester la requete Python"
"pour rapatrier les données météorologiques du portail de Météo-France"



# pour générer l'URL lié à l'APIM ainsi que la requête, se référer au lien teams suivant: https://tobumo.sharepoint.com/:f:/r/teams/AKRRENEW/Documents%20partages/Etienne%20FELLMANN?csf=1&web=1&e=PU0x1S/mode_emploi_APIM_portail_meteo_france


# méthode ci-dessous trouvée dans ce convertisseur cURL-Python ici : https://curlconverter.com/python/

import requests

headers = {
    'accept': '*/*',
    # ici on entre le jwt Token don la clé générée sur le portail de l'APIM
    'apikey': 'eyJ4NXQiOiJZV0kxTTJZNE1qWTNOemsyTkRZeU5XTTRPV014TXpjek1UVmhNbU14T1RSa09ETXlOVEE0Tnc9PSIsImtpZCI6ImdhdGV3YXlfY2VydGlmaWNhdGVfYWxpYXMiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJldGllbm5lLmZlbGxtYW5uQGNhcmJvbi5zdXBlciIsImFwcGxpY2F0aW9uIjp7Im93bmVyIjoiZXRpZW5uZS5mZWxsbWFubiIsInRpZXJRdW90YVR5cGUiOm51bGwsInRpZXIiOiJVbmxpbWl0ZWQiLCJuYW1lIjoidGVzdF9maWNoaWVyX2dyaWJfbWV0ZW8iLCJpZCI6MTg4MSwidXVpZCI6IjUyYTkyMmY1LTE4MmUtNDcyMi05OWIwLTUyZGI4ODAzNjNhNiJ9LCJpc3MiOiJodHRwczpcL1wvcG9ydGFpbC1hcGkubWV0ZW9mcmFuY2UuZnI6NDQzXC9vYXV0aDJcL3Rva2VuIiwidGllckluZm8iOnsiNTBQZXJNaW4iOnsidGllclF1b3RhVHlwZSI6InJlcXVlc3RDb3VudCIsImdyYXBoUUxNYXhDb21wbGV4aXR5IjowLCJncmFwaFFMTWF4RGVwdGgiOjAsInN0b3BPblF1b3RhUmVhY2giOnRydWUsInNwaWtlQXJyZXN0TGltaXQiOjAsInNwaWtlQXJyZXN0VW5pdCI6InNlYyJ9fSwia2V5dHlwZSI6IlBST0RVQ1RJT04iLCJwZXJtaXR0ZWRSZWZlcmVyIjoiIiwic3Vic2NyaWJlZEFQSXMiOlt7InN1YnNjcmliZXJUZW5hbnREb21haW4iOiJjYXJib24uc3VwZXIiLCJuYW1lIjoiQVJPTUUiLCJjb250ZXh0IjoiXC9wdWJsaWNcL2Fyb21lXC8xLjAiLCJwdWJsaXNoZXIiOiJhZG1pbl9tZiIsInZlcnNpb24iOiIxLjAiLCJzdWJzY3JpcHRpb25UaWVyIjoiNTBQZXJNaW4ifV0sImV4cCI6MTc3NzgwOTE1OSwicGVybWl0dGVkSVAiOiIiLCJpYXQiOjE2ODMyMDExNTksImp0aSI6IjNhNDE1YzQ2LWJhZDAtNDY5MC1iNGE5LWNmZDMxMGMzNDE0ZiJ9.EsomXLPsIbk7c7lROl-onVuo2a2cs886BHpwtvuO7jEMUhJQgEafW0q-oSAHs3x3F_zgfHBfeY25SLzNmYHiogfeFNbWupaic5b7yE6HOXNZzSNLrhxycPFBGpM-iojbmTw3bEvBuiEkMyfJ73UcjF0nFNe6feEy1doMjbkG1eMmaWtQFzZzSE_fjHaXUwtzd8rb-VD3rIllqJ8Vx1_WNQpNJfZEFqOxuU1pQv_0XLuDo84i6oFlsE7-oZ5HsEVTc0jitvraM7IbbRAJBL9fBtFPBhj6he0fKiwSHtWlg0oZFz-p4FGaG3NvqF0NuOWcIY3G4_84kP6Y5Dfx1Bf5HA==',
}

# dans la reponse on entre l'URL WCS grib2 que l'on a pioché sur le portail ici : 
# https://donneespubliques.meteofrance.fr/?fond=produit&id_produit=131&id_rubrique=51
# pour lui signifier le paramètre, la plage de temps, la plage géographique ainsi que la resolution spatiale
"attention, lorsque vous choisissez la resolution dans le domaine de la visualisation WMS, "
"la mention 'France' ne signifie pas que la simulation concerne uniquement le territoire français"




response = requests.get(
    'https://public-api.meteofrance.fr/public/arome/1.0/wcs/MF-NWP-HIGHRES-AROME-001-FRANCE-WCS/GetCoverage?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&format=application/wmo-grib&coverageId=CONVECTIVE_AVAILABLE_POTENTIAL_ENERGY__GROUND_OR_WATER_SURFACE___2023-05-23T03:00:00Z&subset=time(2023-05-23T06:00:00Z)&subset=lat(42.05808970704676,47.00193736329676)&subset=long(-2.962155744433405,4.969973161816595)',
     headers=headers, 
)

with open('grib_AROME_file/weather_file_test_4.grb2', 'wb') as f:
    f.write(response.content)

 












# cependant il existe un exemple de requete aussi en Python trouvée depuis cette page web : 
# https://portail-api.meteofrance.fr/authenticationendpoint/aide_fr.do#subscribe-api

""" 
import json
import requests
import time

# Example of a Python implementation for a continuous authentication client.
# It's necessary to :
# - update APPLICATION_ID
# - update request_url at the end of the script

# unique application id : you can find this in the curl's command to generate jwt token or with Base64(consumer-key:consumer-secret) keys application
APPLICATION_ID = "eyJ4NXQiOiJZV0kxTTJZNE1qWTNOemsyTkRZeU5XTTRPV014TXpjek1UVmhNbU14T1RSa09ETXlOVEE0Tnc9PSIsImtpZCI6ImdhdGV3YXlfY2VydGlmaWNhdGVfYWxpYXMiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJldGllbm5lLmZlbGxtYW5uQGNhcmJvbi5zdXBlciIsImFwcGxpY2F0aW9uIjp7Im93bmVyIjoiZXRpZW5uZS5mZWxsbWFubiIsInRpZXJRdW90YVR5cGUiOm51bGwsInRpZXIiOiJVbmxpbWl0ZWQiLCJuYW1lIjoiYXBwbGljYXRpb25fdGVzdCIsImlkIjoxODYyLCJ1dWlkIjoiMTUwNzIwNjgtMmUxMC00MDVmLWJjMTYtMmZmZGQyNjM2OTdkIn0sImlzcyI6Imh0dHBzOlwvXC9wb3J0YWlsLWFwaS5tZXRlb2ZyYW5jZS5mcjo0NDNcL29hdXRoMlwvdG9rZW4iLCJ0aWVySW5mbyI6eyI1MFBlck1pbiI6eyJ0aWVyUXVvdGFUeXBlIjoicmVxdWVzdENvdW50IiwiZ3JhcGhRTE1heENvbXBsZXhpdHkiOjAsImdyYXBoUUxNYXhEZXB0aCI6MCwic3RvcE9uUXVvdGFSZWFjaCI6dHJ1ZSwic3Bpa2VBcnJlc3RMaW1pdCI6MCwic3Bpa2VBcnJlc3RVbml0Ijoic2VjIn19LCJrZXl0eXBlIjoiUFJPRFVDVElPTiIsInBlcm1pdHRlZFJlZmVyZXIiOiIiLCJzdWJzY3JpYmVkQVBJcyI6W3sic3Vic2NyaWJlclRlbmFudERvbWFpbiI6ImNhcmJvbi5zdXBlciIsIm5hbWUiOiJBUk9NRSIsImNvbnRleHQiOiJcL3B1YmxpY1wvYXJvbWVcLzEuMCIsInB1Ymxpc2hlciI6ImFkbWluX21mIiwidmVyc2lvbiI6IjEuMCIsInN1YnNjcmlwdGlvblRpZXIiOiI1MFBlck1pbiJ9XSwiZXhwIjoxNzc3NzkxNTMzLCJwZXJtaXR0ZWRJUCI6IiIsImlhdCI6MTY4MzE4MzUzMywianRpIjoiYzAwY2YyN2MtODI5Yy00YWNlLWEyMzUtMDUyMDhjZGE0ZWU3In0=.G7KjVslM6KO_13JghW_FgublLIyONVt1sJBxAQvZMBe0Xl4N3cXqo00sngmV4TBzqMYKGvGJzsciehrGQjfI1hVxgM1iU0kxkYeUO1Vpr182RnkG4fBkfWzDJC5bqLiswYoGnwYAy6IvKIrSvo8DHGlCP8puxPGQF-KL9Xd-9xiNtltcZB1V8QdG7uCr6uIHGF3vdszHNLY0sA3BYP-rkypZQN_zoM0ul4Gt7wJ6VspWutWGxUawQSRD-wNVeBN79YCSK_AER0fZVS2rgJ7Jj8AUc-lajix6TaQujM1PqdGAbVrcqekMKK3CY-DlcCoIC-WbgWMwTSXhFi9Id4wV0A=="

# url to obtain acces token
#TOKEN_URL = "https://portail-api.meteofrance.fr/private/nativeAPIs/token"
class Client(object):

    def __init__(self):
        self.session = requests.Session()

    def request(self, method, url, **kwargs):
        # First request will always need to obtain a token first
        if 'Authorization' not in self.session.headers:
            self.obtain_token()

        # Optimistically attempt to dispatch reqest
        response = self.session.request(method, url, **kwargs)
        if self.token_has_expired(response):
            # We got an 'Access token expired' response => refresh token
            self.obtain_token()
            # Re-dispatch the request that previously failed
            response = self.session.request(method, url, **kwargs)

        return response

    def token_has_expired(self, response):
        status = response.status_code
        content_type = response.headers['Content-Type']
        if status == 401 and 'application/json' in content_type:
            if 'expired' in response.headers['WWW-Authenticate']:
                return True

        return False

    def obtain_token(self):
        # Obtain new token
        data = {'grant_type': 'client_credentials'}
        headers = {'Authorization': 'Basic ' + APPLICATION_ID}
        access_token_response = requests.post(TOKEN_URL, data=data, verify=False, allow_redirects=False, headers=headers)
        token = access_token_response.json()['access_token']
        # Update session with fresh token
        self.session.headers.update({'Authorization': 'Bearer %s' % token})

def main():
    client = Client()
    # Issue a series of API requests an example. For use this test, you must first subscribe to the arome api with your application
    client.session.headers.update({'Accept': 'application/json'})

    for i in range(100):
        response = client.request('GET', 'https://public-api.meteofrance.fr/public/arome/1.0/wms/MF-NWP-HIGHRES-AROME-001-FRANCE-WMS/GetCapabilities?service=WMS&version=1.3.0', verify=False)
        print(response.status_code)
        time.sleep(120)


if __name__ == '__main__':
    main()

  """ 

