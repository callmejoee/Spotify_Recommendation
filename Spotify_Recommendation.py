import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up Spotify credentials
client_id = '70a9fb89662f4dac8d07321b259eaad7'
client_secret = '4d6710460d764fbbb8d8753dc094d131'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Streamlit app
st.title('Song Recommender by Artist')

artist_name = st.text_input('Enter the name of the artist:')
if artist_name:
    results = sp.search(q='artist:' + artist_name, limit=10)
    if results['tracks']['items']:
        st.subheader('Top 10 songs by ' + artist_name + ':')
        for idx, track in enumerate(results['tracks']['items']):
            st.write(f"{idx + 1}. {track['name']} - {', '.join([artist['name'] for artist in track['artists']])}")

        selected_song_index = st.number_input('Select a song index for recommendations:', min_value=1, max_value=10)
        if st.button('Get Recommendations'):
            selected_track_uri = results['tracks']['items'][selected_song_index - 1]['uri']
            recommended_tracks = sp.recommendations(seed_tracks=[selected_track_uri], limit=10)
            if recommended_tracks['tracks']:
                st.subheader('Recommended songs:')
                for idx, rec_track in enumerate(recommended_tracks['tracks']):
                    st.write(f"{idx + 1}. {rec_track['name']} - {', '.join([artist['name'] for artist in rec_track['artists']])}")
            else:
                st.write("No recommendations found.")
    else:
        st.write("No tracks found for the given artist.")
