import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter.ttk import *
import Certificate as cert
from tkinter.filedialog import askopenfilename
import hashlib as h
import RSA as rsa

# Represents an Application
class MyApp:
    # Builder
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x180")
        self.root.resizable(0, 0)
        self.root.title("Certificate")
        # Call to place_items() and textvariables needed
        self.organization_name = StringVar()
        self.organization_country = StringVar()
        self.organization_location = StringVar()
        self.organization_domain = StringVar()
        self.tls_version = StringVar()
        self.tls_versions = ["TLS 1.2", "TLS 1.3"]
        self.tls_version.set(self.tls_versions[0])
        self.place_items()

    def place_items(self):
        # Name label and Entry
        self.label_name = tk.Label(self.root, text = "Organización: ").place(x = 10, y = 10)
        self.entry_name = tk.Entry(self.root, textvariable = self.organization_name).place(x = 95, y = 10)
        # Country label and Entry
        self.label_country = tk.Label(self.root, text = "País: ").place(x = 10, y = 35)
        self.entry_country = tk.Entry(self.root, textvariable = self.organization_country).place(x = 95, y = 35)
        # Location label and Entry
        self.label_location = tk.Label(self.root, text = "Localidad: ").place(x = 10, y = 60)
        self.entry_location = tk.Entry(self.root, textvariable = self.organization_location).place(x = 95, y = 60)
        # Domain label and Entry
        self.label_domain = tk.Label(self.root, text = "Dominio: ").place(x = 10, y = 85)
        self.entry_domain = tk.Entry(self.root, textvariable = self.organization_domain).place(x = 95, y = 85)
        # Choosing between TLS versions
        self.tls_menu = ttk.Combobox(self.root, textvariable = self.tls_version, values = self.tls_versions).place(x = 10, y = 110)
        # Buttons
        self.generate_button = tk.Button(self.root, text = "Generate certificate", command = self.generate).place(x = 10, y = 145)
        self.verify_button = tk.Button(self.root, text = "Verify certificate", command = self.verify).place(x = 130, y = 145)

    def generate(self):
        cert.Certificate(self.organization_name.get(), self.organization_country.get(), self.organization_location.get(), self.organization_domain.get(), self.tls_version.get())

    def verify(self):
        # Select the file and open it in read mode
        filename = askopenfilename()
        file = open(filename, "r")
        content = file.readlines()
        file.close()

        # This will be the text from which we are going to obtain the hash
        text_to_hash = ""

        # This will be the signature obtained from the file
        signature_to_verify = 0
        
        # Obtaining information from the certificate file
        for i in range(0, len(content)):
            # Obtaining the signature
            if("Firma:" in content[i]):
                signature_to_verify = int(content[i].replace("Firma: 0x", "").replace("\n", ""), 16)
                continue
            
            # Obtaining the public exponent
            if("Exponente:" in content[i]):
                e = int(content[i].replace("Exponente: ", "").replace("\n", ""))

            # Obtaining the public module
            if("Módulo:" in content[i]):
                n = int(content[i].replace("Módulo: 0x", "").replace("\n", ""), 16)

            if("Huellas digitales" in content[i]):
                continue

            if("SHA-1:" in content[i]):
                continue

            if("SHA-256" in content[i]):
                continue

            text_to_hash = text_to_hash + content[i].replace(" ", "").replace("\n", "")

        # Obtaining the hash of the text
        text_to_hash = text_to_hash + "Firma:"
        hash_text = h.sha256()
        hash_text.update(text_to_hash.encode('utf-8'))
        hash_text = int(hash_text.hexdigest().replace("0x", ""), 16)

        # Obtaining the hash from the signature
        start_text_hash = rsa.RSASignature.verify(signature_to_verify, e, n)
        
        print(hash_text == start_text_hash)
        return hash_text == start_text_hash

root = tk.Tk()
app = MyApp(root)
root.mainloop()
