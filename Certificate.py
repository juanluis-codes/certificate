import datetime as dt
from datetime import date, timedelta
import RSA as rsa
import hashlib as h
# Represents a Certificate
ISSUING_NAME = "Certlu"
ISSUING_COUNTRY = "ES"
class Certificate:
    # Builder
    def __init__(self, organization_name, organization_country, organization_location, organization_domain, tls_version):
        # Attributes
        self.organization_name = organization_name
        self.organization_country = organization_country
        self.organization_location = organization_location
        self.organization_domain = organization_domain
        self.issue_date = date.today()
        self.expiration_date = self.issue_date + timedelta(365/2)
        self.tls_version = tls_version
        self.rsakeyset = rsa.RSA()
        # It will generate the Certificate
        self.generateFile()

    # Creates the Certificate file
    def generateFile(self):
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

        # Text that will be signed
        # We delete \n and blanks
        text_to_sign = text.replace(" ", "").replace("\n", "")
        # Creating the hash object for the signature and the Fingerprints
        hash_text_to_sign = h.sha256()
        first_fingerprint_sha1 = h.sha1()
        second_fingerprint_sha256 = h.sha256()
        # Hashing the text and signing it
        hash_text_to_sign.update(text_to_sign.encode("utf-8"))
        hash_text_to_sign = int(hash_text_to_sign.hexdigest().replace("0x", ""), 16)
        self.signature = rsa.RSASignature(rsakeyset = self.rsakeyset)
        self.signature.sign(hash_text_to_sign)
        # Adding the Signature to the certificate file
        text = (text + hex(self.signature.signature))
        # Calcultaing and adding the fingerprints
        text_to_sha1 = text_to_sign + hex(self.signature.signature) + "HuellasdigitalesSHA-1:"
        first_fingerprint_sha1.update(text_to_sha1.encode("utf-8"))
        text = text + "\nHuellas digitales\n SHA-1: " + first_fingerprint_sha1.hexdigest() + "\n SHA-256: "
        text_to_sha256 = text.replace(" ", "").replace("\n", "")
        second_fingerprint_sha256.update(text_to_sha256.encode("utf-8"))
        text = text + second_fingerprint_sha256.hexdigest()
        
        self.file = open("cert.txt", "w")
        self.file.write(text)
        self.file.close()
    
