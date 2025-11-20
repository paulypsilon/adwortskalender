import datetime
from atproto import Client, models
import os

# -------------------------------
# 1) Liste der Datums-Texte
# -------------------------------
posts = {
    "2025-11-19": "Ahoi. Ab heute wird getestet. Es wird daher immer mal Skeets geben, die auch wieder verschwinden.",
    "2025-11-20": "Testwort",
    "2025-11-21": "Knebelsrod",
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

# --------------------------------
# 2) Heutiges Datum
# --------------------------------
today = datetime.date.today().isoformat()
word = posts.get(today, "").strip()

if not word:
    print(f"Kein gültiger Eintrag für {today}.")
    exit(0)

formatted_date = datetime.datetime.strptime(today, "%Y-%m-%d").strftime("%d.%m.%Y")

# --------------------------------
# 3) Text zusammensetzen
# --------------------------------
text = (
    f"📅 {formatted_date} #adwortskalender\n"
    f"\n"
    f"📖 {word}"
)

# --------------------------------
# 4) Bluesky Login
# --------------------------------
USERNAME = os.getenv("BSKY_USERNAME")
PASSWORD = os.getenv("BSKY_PASSWORD")

if not USERNAME or not PASSWORD:
    raise ValueError("Umgebungsvariablen BSKY_USERNAME und BSKY_PASSWORD müssen gesetzt sein.")

client = Client()
client.login(USERNAME, PASSWORD)


# --------------------------------
# 5) Hashtag-Facets erzeugen
# --------------------------------
def make_post_with_hashtag(client, text, tag="adwortskalender"):
    facets = []
    hashtag = f"#{tag}"
    index = text.find(hashtag)

    if index != -1:
        facets.append(
            models.AppBskyRichtextFacet.Main(
                features=[
                    models.AppBskyRichtextFacet.Tag(tag=tag)
                ],
                index=models.AppBskyRichtextFacet.ByteSlice(
                    start=index,
                    end=index + len(hashtag),
                ),
            )
        )

    return client.app.bsky.feed.post.create(
        repo=client.me.did,
        record=models.AppBskyFeedPost.Record(
            text=text,
            created_at=datetime.datetime.utcnow().isoformat(),
            facets=facets,
        ),
    )


# --------------------------------
# 6) Post senden
# --------------------------------
make_post_with_hashtag(client, text)

print("Gesendet:")
print(text)
