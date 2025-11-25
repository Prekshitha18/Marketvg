AI Marketing Video Generator

This Streamlit application automatically creates a short marketing video using AI. It takes inputs from the user, generates a script, converts it to voice, and finally combines sample video clips with audio to create a promotional reel.

1. Importing Required Libraries

The code imports necessary modules:

streamlit → for building the web interface

openai → for generating text and voice using AI

os, tempfile → for file handling

cv2 → optional, for video/image processing

moviepy → for editing videos, combining clips, adding audio, and exporting the final video

2. App Configuration
openai.api_key = "YOUR_OPENAI_API_KEY"
st.set_page_config(page_title="AI Marketing Video Generator", layout="wide")


Sets the OpenAI API key

Configures Streamlit page layout

3. Title Section
st.title("🎥 AI Marketing Video Generator")
st.write("Generate marketing reels using AI – Script → Audio → Video → Final Reel")


Displays title and short description of the app.

4. Step 1: User Inputs

The app asks the user to enter:

Company name

Product description

Target audience

Marketing goal

These inputs are used to generate a personalized marketing script.

5. Step 2: Script Generation Using AI

When the user clicks Generate Script, the app:

Validates inputs

Creates a prompt requesting AI to write a 3-scene marketing script

Sends the prompt to OpenAI using openai.ChatCompletion.create()

Displays the generated script to the user

Saves the script to script.txt

6. Step 3: Generate Voiceover (TTS)

When the user clicks Generate Voice:

The script text is passed to OpenAI’s text-to-speech model

A voiceover audio file audio.mp3 is generated

The audio is played in the Streamlit interface

7. Step 4: Load Sample Video Clips
sample_videos = ["sample1.mp4", "sample2.mp4", "sample3.mp4"]


The app:

Tries to load each sample video

Shows the videos in the UI

Stores valid clips to combine later

8. Step 5: Combine Video + Audio + Export

When the user clicks Create Final Marketing Video:

The generated audio is loaded using MoviePy

All video clips are resized to a uniform height

Clips are combined using CompositeVideoClip

Audio is attached to the video

The final video is rendered as final_marketing_video.mp4

The app then:

Shows the final video

Provides a Download Video button