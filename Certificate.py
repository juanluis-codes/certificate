import datetime as dt
from datetime import date, timedelta
import RSA as rsa
# Represents a Certificate
ISSUING_NAME = "Certlu"
ISSUING_COUNTRY = "ES"
class Certificate:
    # Builder
    def __init__(self, organization_name, organization_country, organization_location, organization_domain, tls_version):
        self.organization_name = organization_name
        self.organization_country = organization_country
        self.organization_location = organization_location
        self.organization_domain = organization_domain
        self.issue_date = date.today()
        self.expiration_date = self.issue_date + timedelta(365/2)
        self.tls_version = tls_version
        self.rsakeyset = rsa.RSA()
        self.generateFile()

    def generateFile(self):
        self.file = open("cert.txt", "w")
        text = ("Información sobre la organización\n Organización: " + self.organization_name +
                         "\n País: " + self.organization_country +
                         "\n Localidad: " + self.organization_location +
                         "\n Dominio: " + self.organization_domain +
                         "\nInformación sobre la organización emisora\n Organización: " + ISSUING_NAME +
                         "\n País: " + ISSUING_COUNTRY +
                         "\nValidez\n No antes: " + str(self.issue_date) +
                         "\n No despues: " + str(self.expiration_date) +
                         "\nInformación de clave pública\n Algoritmo: RSA\n Tamaño de la clave: 2048\n Exponente: 65537\n Módulo: " + hex(self.rsakeyset.n) +
                         "\nFirma: ")
        self.file.write(text)
        self.file.close()
    
