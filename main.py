import os
from atproto import Client

BLUESKY_USER = os.getenv("BLUESKY_USER")
BLUESKY_PASS = os.getenv("BLUESKY_PASS")

# 34 Einträge
WOERTER = {
    1: "21",
    2: "22",
    3: "23",
    4: "24",
    5: "25",
    6: "26",
    7: "27",
    8: "28",
    9: "29",
    10: "30",
    11: "florieren",
    12: "nassforsch",
    13: "Landesbauordnung",
    14: "jonglieren",
    15: "semipermeabel",
    16: "Wannenwunder",
    17: "brommseln",
    18: "heuristisch",
    19: "Quotenfrosch",
    20: "pesen",
    21: "xanthochrom",
    22: "Mangelinstrument",
    23: "verfranzen",
    24: "irrlichternd",
    25: "Zirbelnuss",
    26: "gratinieren",
    27: "raumgreifend",
    28: "Aspik",
    29: "treideln",
    30: "charmant",
    31: "erodieren",
    32: "dürftig",
    33: "Ypsilon",
    34: "Osterhase",
}

COUNTER_FILE = "counter.txt"

def load_counter():
    if not os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "w") as f:
            f.write("1")
        return 1

    with open(COUNTER_FILE, "r") as f:
        return int(f.read().strip())

def save_counter(value):
    with open(COUNTER_FILE, "w") as f:
        f.write(str(value))

def post_bluesky(text):
    client = Client()
    client.login(BLUESKY_USER, BLUESKY_PASS)
    client.send_post(text)

def main():
    counter = load_counter()

    wort = WOERTER[counter]

    text = f"✨ Wort des Tages ({counter}/34):\n{wort}"

    print("Posting:", text)
    post_bluesky(text)

    # Nächster Eintrag — nach 34 wieder bei 1
    next_counter = 1 if counter >= 34 else counter + 1
    save_counter(next_counter)

if __name__ == "__main__":
    main()
