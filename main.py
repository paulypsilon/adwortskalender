import datetime
from atproto import Client
import os

# -------------------------------
# 1) Liste der Datums-Texte
# -------------------------------
posts = {
    "2025-11-19": "Ahoi. Ab heute wird getestet. Es wird daher immer mal Skeets geben, die auch wieder verschwinden.",
    "2025-11-20": "Testwort",
    "2025-11-21": "",
    "2025-11-22": "",
    "2025-11-23": "",
    "2025-11-24": "",
    "2025-11-25": "",
    "2025-11-26": "",
    "2025-11-27": "",
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

word = posts[today].strip()

if not word:
    print(f"Eintrag für {today} ist leer – kein Post wird gesendet.")
    exit(0)

# Datum formatiert: 2025-12-01 → 01.12.2025
day, month, year = today[8:], today[5:7], today[0:4]
formatted_date = f"{day}.{month}.{year}"

# -------------------------------
# 3) Finaler Posttext
# -------------------------------
text = (
    f"📅 {formatted_date}\n"
    f"\n"
    f"📖 {word}\n"
    f"\n"
    "#adwortskalender"
)

# -------------------------------
# 4) Bluesky-Login
# -------------------------------
USERNAME = os.getenv("BSKY_USERNAME")
PASSWORD = os.getenv("BSKY_PASSWORD")

print("USERNAME:", USERNAME)
print("PASSWORD gesetzt:", PASSWORD is not None)

try:
    client = Client()
    client.login(USERNAME, PASSWORD)
except Exception as e:
    print("LOGIN FEHLER:")
    print(type(e), e)
    raise

# -------------------------------
# 5) Post absenden
# -------------------------------
client.send_post(text)

print(f"Gesendet: {text}")
