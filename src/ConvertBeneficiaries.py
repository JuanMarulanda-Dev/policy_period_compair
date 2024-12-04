import json

# Definimos la clase Beneficiary para tener una referencia clara de los atributos
class Beneficiary:
    def __init__(self, master, dni, beneficiaryType, contactType, documentType, firstName, lastName, primaryPhone):
        self.Master = master
        self.DNI = dni
        self.BeneficiaryType = beneficiaryType
        self.ContactType = contactType
        self.DocumentType = documentType
        self.FirstName = firstName
        self.LastName = lastName
        self.PrimaryPhone = primaryPhone

def transform_json_to_string(json_file_path):
    # Leer el archivo JSON
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    beneficiaries_string = ""

    # Recorrer cada elemento en 'items'
    for item in data['items']:
        # Crear una instancia de Beneficiary
        beneficiary = Beneficiary(
            master=item.get('master', ''),
            dni=item.get('dni', ''),
            beneficiaryType=item.get('beneficiaryType', ''),
            contactType=item.get('contactType', ''),
            documentType=item.get('documentType', ''),
            firstName=item.get('firstName', ''),
            lastName=item.get('lastName', ''),
            primaryPhone=item.get('primaryPhone', '')
        )

        # Formatear el objeto Beneficiary en la cadena deseada
        beneficiaries_string += (
            f'beneficiaries.add(new Beneficiary(){{:Master = "{beneficiary.Master}", '
            f':DNI = "{beneficiary.DNI}", '
            f':BeneficiaryType = "{beneficiary.BeneficiaryType}", '
            f':ContactType = "{beneficiary.ContactType}", '
            f':DocumentType = "{beneficiary.DocumentType}", '
            f':FirstName = "{beneficiary.FirstName}", '
            f':LastName = "{beneficiary.LastName}", '
            f':PrimaryPhone = "{beneficiary.PrimaryPhone}"}})\n'
        )

    return beneficiaries_string

# Llama a la función con la ruta del archivo JSON
result_string = transform_json_to_string('C:\\Users\\juan.marulanda\\Desktop\\contacts-24.json')

# Imprimir el resultado
print(result_string)
