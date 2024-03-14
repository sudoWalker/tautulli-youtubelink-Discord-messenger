import os
import sys
import requests
import json
import time

def get_youtube_link(film_title, api_key):
    query = film_title + " Trailer German" # change for different search results
    url = f"https://www.googleapis.com/youtube/v3/search"
    params = {
        'part': 'snippet',
        'maxResults': 1,
        'q': query,
        'key': api_key,
        'type': 'video'
    }
    response = requests.get(url, params=params)
    data = response.json()
    video_id = data['items'][0]['id']['videoId']
    return 'https://www.youtube.com/watch?v=' + video_id

def send_to_discord(webhook_url, content):
    if content is None:
        print("No YouTube link found, not sending a message.")
        return
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
        print("Webhook delivered, returned {}.".format(result.status_code))

film_title = os.getenv('title') if os.getenv('title') else sys.argv[1]  # The movie title is retrieved from the environment variables or from the command line arguments
film_year = os.getenv('year') if os.getenv('year') else sys.argv[2] 
api_key = 'Your_Youtube_API'  # Enter your YouTube API key here
webhook_url = "https://discord.com/api/webhooks/YourWebhookURL"  # Setzen Sie hier Ihre Webhook-URL ein
time.sleep(5)  # Warten Sie 5 Sekunden
youtube_link = get_youtube_link(film_title, api_key)
send_to_discord(webhook_url, youtube_link)
