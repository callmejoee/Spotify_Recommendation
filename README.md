# Song Recommender by Artist

## Overview
This Python application uses the Streamlit library along with Spotipy to create an interactive web app that allows users to input an artist's name and get song recommendations based on that artist's tracks using the Spotify API.

## Libraries Used
- **Streamlit**: A web application framework for creating interactive web apps using simple Python scripts.
- **Spotipy**: A lightweight Python library for the Spotify Web API.

## Project Structure
- **Main File**: The main Python file (`app.py`) contains the application's logic and user interface built using Streamlit.
- **Dependencies**: The app requires the installation of Streamlit and Spotipy libraries.

## Setup Instructions
1. **Installation**:
   - Install the required libraries:
     ```bash
     pip install streamlit spotipy
     ```

2. **Get Spotify API Credentials**:
   - Create an account on the Spotify Developer Dashboard.
   - Create a new application to obtain your Client ID and Client Secret.

3. **Replace Credentials**:
   - In the `app.py` file, replace `'YOUR_SPOTIFY_CLIENT_ID'` and `'YOUR_SPOTIFY_CLIENT_SECRET'` with your actual Spotify API credentials.

4. **Run the Application**:
   - Run the Streamlit app by executing:
     ```bash
     streamlit run app.py
     ```

## Usage
- **Input**: Enter the name of an artist into the text input field provided.
- **Output**:
  - The app displays the top 10 songs by the entered artist.
  - Select a song index to get recommendations based on that song.
  - Click the "Get Recommendations" button to fetch and display recommended songs similar to the selected track.

## Code Structure
- **Initialization**:
  - Imports necessary libraries (`streamlit`, `spotipy`) and sets up Spotify API credentials using Spotipy's `SpotifyClientCredentials`.
- **Streamlit App**:
  - Constructs the user interface using Streamlit's components.
  - Provides a text input field for the artist's name.
  - Upon input, retrieves the top 10 songs by the artist and displays them.
  - Allows the user to select a song for recommendations and fetches similar tracks based on the chosen song.

## Future Improvements
- **Enhanced UI**: Incorporate better styling and visual elements for a more engaging user experience.
- **Error Handling**: Implement error handling for cases where the artist or tracks are not found.
- **Additional Features**: Include options for choosing different recommendation parameters or genres.

## Security Note
- Ensure that your Spotify API credentials (`client_id` and `client_secret`) are kept secure and not exposed in public repositories.
- I just used a random guy's Credentials lol
