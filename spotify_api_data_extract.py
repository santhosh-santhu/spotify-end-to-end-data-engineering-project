import json
import os
import spotipy
import boto3
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime

def lambda_handler(event, context):
    
    client_id = os.environ.get('client_id')
    client_secret=os.environ.get('client_secret')
    
    client_credentials_manager=SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
    sp=spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    playlists = sp.user_playlists('spotify')
    playlist_link="https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF"
    
    playlist_URL =playlist_link.split('/')[-1] 
    spotify_data = sp.playlist_tracks(playlist_URL)
    
    client = boto3.client('s3')#to dump enter file in s3 
    
    filename = "spotify_raw_"+str(datetime.now())+'.json'
    
    client.put_object(
        Bucket='spotifyetlproject',                 #bucket name
        Key='raw_data/to_processed/'+ filename,      #where the data should store
        Body=json.dumps(spotify_data)               #it is used to convert into json string and dumps the data
        )
    
    