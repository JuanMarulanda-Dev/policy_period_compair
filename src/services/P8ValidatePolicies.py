from itertools import count

import requests
API_KEY = "ibHEEwSxOOZNtIeDWFwMzSUJm9T8V9sDchzCrns6fyPNzTrt"

master_policies = [
    "028008161050", # expedida
    "028008280764", # expedida
    "028008339665"  # expedida pero no genero caratula
]

def get_document(policy):
    url = "https://api.sura.co/apip8/v1/documentos"
    headers = {
        "x-apikey": API_KEY,
    }
    params = {
        "className": "Seguros",
        "query": f"DSTipoDocumental='Caratula poliza' and NMNroPoliza like '{policy}' and DateCreated >= 20241201T000000Z",
        "order": "DateCreated DESC",
        "top": 1000,
        "properties": "FEFechaMovimiento,DSTipoDocumental,NMNroPoliza"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def document_verification(document):
     if document.get('count') == 1:
        return 'si'
     else:
        return 'no'

def process_policy_verification_in_p8(policies):
    count = 0
    for policy in policies:
        document = get_document(policy)
        has_document = document_verification(document)
        if has_document == 'si':
            count+=1
        print(f"{policy};{has_document}")
    print(f"Polizas Cargadas en P8: {count}" )

process_policy_verification_in_p8(master_policies)
