import requests
import json

iTOKEN = "ca7443aa566bc74fda969f9018ef1297"
iTIPOCONSULTA = 1


if iTIPOCONSULTA == 1:
    iCITY = input('Informe o nome da cidade: ')
    iURL  = (f'http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={iCITY}&token={iTOKEN}')
    iRESPONSE = requests.request('GET', iURL)
    iRETORNO_REQ =  json.loads(iRESPONSE.text)
    print(iRETORNO_REQ)