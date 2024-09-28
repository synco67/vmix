import tkinter as tk
from tkinter import simpledialog
import requests

# Vooraf ingesteld IP-adres van de vMix instance
VMIX_IP = "192.168.85.232"  # Verander dit naar het juiste IP-adres van je vMix instance
VMIX_PORT = 8088          # Standaard poort voor de vMix HTTP API

# Functie om een HTTP verzoek te sturen naar de vMix instance
def stuur_http_request(pad):
    url = f"http://{VMIX_IP}:{VMIX_PORT}/api/{pad}"
    
    try:
        # Verstuur een GET verzoek naar de volledige URL
        response = requests.get(url)
        print (url)

        
        # Controleer of de aanvraag succesvol was
        if response.status_code == 200:
            print(f"Topper: {response.status_code} - {response.text}")
        else:
            print(f"Fout: {response.status_code} - {response.text}")
    
    except requests.exceptions.RequestException as e:
        print(f"Er ging iets fout met het verzoek: {e}")

# Maak een dialoogvenster om de gebruiker om het pad of de querystring van het vMix HTTP verzoek te vragen
def vraag_vmix_request():
    root = tk.Tk()
    root.withdraw()  # Verberg het hoofdvenster

    # Vraag de gebruiker om het HTTP pad/querystring in te voeren
    pad = simpledialog.askstring("vMix HTTP Request", "Voer het pad of de querystring in (bijv. ?Function=Fade):")
    
    if pad:
        # Verstuur de HTTP aanvraag naar het vooraf ingestelde IP-adres
        stuur_http_request(pad)
    else:
        print("Geen pad of querystring ingevoerd")

# Voer het script uit
if __name__ == "__main__":
    vraag_vmix_request()