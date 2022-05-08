import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter.ttk import *

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
        # Button
        self.generate_button = tk.Button(self.root, text = "Generate certificate", command = self.generate).place(x = 10, y = 145)

    def generate(self):
        pass
        
        

root = tk.Tk()
app = MyApp(root)
root.mainloop()
