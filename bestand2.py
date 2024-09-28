import tkinter as tk
from tkinter import simpledialog, messagebox
import requests

# Vooraf ingesteld IP-adres van de vMix instance
VMIX_IP = "192.168.85.218"  # Verander dit naar het juiste IP-adres van je vMix instance
VMIX_PORT = 8088          # Standaard poort voor de vMix HTTP API

# Functie om een bestand te lezen en de regel te vinden die overeenkomt met het opgegeven nummer
def lees_regel_uit_bestand():
    # Vraag de gebruiker om een cijfer in te voeren
    regelnummer = simpledialog.askinteger("Scene", "Voer een cijfer in:")

    # Bestandsnaam (zorg ervoor dat het bestand bestaat)
    bestandspad = "bestand.txt"

    try:
        # Lees het bestand regel voor regel
        with open(bestandspad, "r") as bestand:
            lijnen = bestand.readlines()

            # Controleer of het ingevoerde nummer geldig is
            if 1 <= regelnummer <= len(lijnen):
                # Haal de regel op die overeenkomt met het ingevoerde nummer
                geselecteerde_regel = lijnen[regelnummer - 1]  # -1 omdat lijsten bij 0 beginnen

                # Toon de geselecteerde regel in een dialoogvenster
                messagebox.showinfo("Geselecteerde regel", f"Regel {regelnummer}: {geselecteerde_regel}")
                print (geselecteerde_regel)
                return geselecteerde_regel
            else:
                messagebox.showerror("Fout", f"Geen regel {regelnummer} in het bestand. Het bestand heeft {len(lijnen)} regels.")
    
    except FileNotFoundError:
        messagebox.showerror("Fout", f"Het bestand '{bestandspad}' is niet gevonden.")
    except Exception as e:
        messagebox.showerror("Fout", f"Er is een fout opgetreden: {e}")

def stuur_http_request(geselecteerde_regel):
    print(f"geselecteerde regel is: {geselecteerde_regel}")
    url = f"http://{VMIX_IP}:{VMIX_PORT}/api/{geselecteerde_regel}"
    
    try:
        # Verstuur een GET verzoek naar de volledige URL
        response = requests.get(url)
        print (url)
        print(response.content)
        # Controleer of de aanvraag succesvol was
        if response.status_code == 200:
            print(f"Topper: {response.status_code} - {response.text}")
        else:
            print(f"Fout: {response.status_code} - {response.text}")
    
    except requests.exceptions.RequestException as e:
        print(f"Er ging iets fout met het verzoek: {e}")



# Hoofdvenster maken
root = tk.Tk()
root.withdraw()  # Verberg het hoofdvenster

# Start de functie om een regel uit het bestand te lezen
func_name=lees_regel_uit_bestand()
print(f"regel is: {func_name}")
stuur_http_request(func_name)

# Start de GUI-loop
root.mainloop()
