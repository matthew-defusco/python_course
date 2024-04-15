import os
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import lxml
import spotipy
from spotipy.oauth2 import SpotifyOAuth


get_year = True
soup = ""

### FOR TESTING ####
# response = requests.get("https://www.billboard.com/charts/hot-100/2023-08-30")
# soup = BeautifulSoup(response.text, "lxml")

# song_titles = [song.get_text(strip=True) for song in soup.select("li.o-chart-results-list__item > h3#title-of-a-story")]
# print(song_titles)
# song_artists = [artist.get_text(strip=True) for artist in soup.select("li.o-chart-results-list__item > h3#title-of-a-story + span")]
# print(song_artists)
#### END TESTING ####

# Get input from the user to find out what date they want to get the top 100.
while get_year:
  date = input("What year would you like to travel to? Type date in this format: YYYY-MM-DD: ")
  try:
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
    response.raise_for_status()
    get_year = False
    soup = BeautifulSoup(response.text, "lxml")
  except requests.exceptions.HTTPError as e:
    print("We weren't able to calculate the date. Please enter it in the following format: YYYY-MM-DD.")

# Organize the results into lists that can be used for searching with the Spotify API.
song_titles = [song.get_text(strip=True) for song in soup.select("li.o-chart-results-list__item > h3#title-of-a-story")]
song_artists = [artist.get_text(strip=True) for artist in soup.select("li.o-chart-results-list__item > h3#title-of-a-story + span")]

sp = spotipy.Spotify(
  auth_manager=SpotifyOAuth(
    scope="playlist-modify-private playlist-read-private",
    client_id=os.environ["SPOTIFY_CLIENT_ID"],
    client_secret=os.environ["SPOTIFY_CLIENT_SECRET"],
    redirect_uri=os.environ["SPOTIFY_REDIRECT_URI"],
    show_dialog=True,
    cache_path="token.txt"
  )
)

current_user_id = sp.current_user()["id"]

user_playlists = sp.user_playlists(user=current_user_id)["items"]

# Check to see if there's already a playlist with the date that the user picked and, if not, create one.
def check_for_existing_playlist(date):
  """
  Checks to see if there's already a playlist with a specific naming convention: "Billboard Top 100 ({date_input})"
  If there is a playlist, it will return False and you should not create a new one with the same name.
  If there is not an existing playlist, it will create the new playlist and return the playlist URI.
  """
  for playlist in user_playlists:
    if playlist["name"] == f"Billboard Top 100 ({date})":
      print(f"Sorry, that playlist was already created for the date {date}. Try running the program again and choosing a different date.")
      return False
    else:
      playlist = sp.user_playlist_create(user=current_user_id, name=f"Billboard Top 100 ({date})", public=False)
      return playlist

playlist = check_for_existing_playlist(date)

# Find all of the URIs for the tracks so that you can add them to the a new playlist.
year = date.split("-")[0]
# year = 2023
if playlist is not False:
  spotify_track_ids = []
  playlist_id = playlist["id"]

  for track in song_titles:
    track_index = song_titles.index(track)
    try:
      song = sp.search(q=f"track: {track.lower().strip()} year: {year} artist: {song_artists[track_index]}", limit=1)
      spotify_track_ids.append(song["tracks"]["items"][0]["uri"])
    except Exception as e:
      print(f"The track {track} by {song_artists[track_index]} was not able to be found.")

  sp.user_playlist_add_tracks(user=current_user_id, playlist_id=playlist_id, tracks=spotify_track_ids)

