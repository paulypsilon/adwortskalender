import datetime
from atproto import Client
import os

# -------------------------------
# 1) Liste der Datums-Texte
# -------------------------------
posts = {
    "2025-11-21": "Ahoi. Ab heute testen wir die Automatisierung ein wenig. Es wird daher immer mal Skeets geben, die auch wieder verschwinden.",
    "2025-11-22": "Die Idee stammt übrigens von meiner Frau. Die hat mir vor Jahren so einen Adventskalender auf Papier geschenkt.",
    "2025-11-23": "",
    "2025-11-24": "",
    "2025-11-25": "",
    "2025-11-26": "",
    "2025-11-27": "Ab morgen gibt es bis zum 1. Dezember ein Beispiel aus meinem damaligen Kalender mit dem damals von mir verwendeten Satz und dem Kontext.",
    "2025-11-28": "",
    "2025-11-29": "",
    "2025-11-30": "",
    "2025-12-01": "florieren",
    "2025-12-02": "nassforsch",
    "2025-12-03": "Landesbauordnung",
    "2025-12-04": "jonglieren",
    "2025-12-05": "semipermeabel",
    "2025-12-06": "Wannenwunder",
    "2025-12-07": "brommseln",
    "2025-12-08": "heuristisch",
    "2025-12-09": "Quotenfrosch",
    "2025-12-10": "pesen",
    "2025-12-11": "xanthochrom",
    "2025-12-12": "Mangelinstrument",
    "2025-12-13": "verfranzen",
    "2025-12-14": "irrlichternd",
    "2025-12-15": "Zirbelnuss",
    "2025-12-16": "gratinieren",
    "2025-12-17": "raumgreifend",
    "2025-12-18": "Aspik",
    "2025-12-19": "treideln",
    "2025-12-20": "charmant",
    "2025-12-21": "erodieren",
    "2025-12-22": "dürftig",
    "2025-12-23": "Ypsilon",
    "2025-12-24": "Osterhase",
}

# -------------------------------
# 2) Bestimme heutiges Datum
# -------------------------------
today = datetime.date.today().isoformat()

if today not in posts:
    print(f"Kein Eintrag für {today}.")
    exit(0)

text = posts[today].strip()

if not text:
    print(f"Eintrag für {today} ist leer – kein Post wird gesendet.")
    exit(0)

# -------------------------------
# 3) Bluesky-Login
# -------------------------------
USERNAME = os.getenv("BSKY_USERNAME")
PASSWORD = os.getenv("BSKY_PASSWORD")

if not USERNAME or not PASSWORD:
    raise ValueError("Umgebungsvariablen BSKY_USERNAME und BSKY_PASSWORD müssen gesetzt sein.")

client = Client()
client.login(USERNAME, PASSWORD)

# -------------------------------
# 4) Post absenden
# -------------------------------
client.send_post(text)

print(f"Gesendet: {text}")
