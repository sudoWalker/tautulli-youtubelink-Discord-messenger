import os
import sys
import requests
import time
from pytube import Search

def get_youtube_link(film_title):
    query = film_title + " Trailer German"
    search = Search(query)
    results = search.results
    if results:
        video_url = results[0].watch_url
        return video_url
    return None

def send_to_discord(webhook_url, content):
    data = {
        "content": content
    }
    result = requests.post(webhook_url, json=data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        print(f"Response content: {result.content}")
    else:
        print(f"Webhook delivered, returned {result.status_code}.")

# Abrufen des Filmtitels aus Umgebungsvariablen oder Kommandozeilenargumenten
film_title = os.getenv('title') or (sys.argv[1] if len(sys.argv) > 1 else None)
film_year = os.getenv('year') or (sys.argv[2] if len(sys.argv) > 2 else None)

# Überprüfung, ob ein Titel vorhanden ist
if not film_title:
    film_title = "Unbekannter Titel"

# Discord Webhook-URL
webhook_url = "https://discord.com/api/webhooks/yourWebhookURL"

time.sleep(5)  # Wartezeit

# Abrufen des YouTube-Links
youtube_link = get_youtube_link(film_title)

# Nachricht erstellen
if youtube_link:
    message = f"Hier ist der YouTube-Link für '{film_title}': {youtube_link}"
else:
    message = f"Es wurde kein YouTube-Link für '{film_title}' gefunden."

# Senden der Nachricht an den Discord-Webhook
send_to_discord(webhook_url, message)
