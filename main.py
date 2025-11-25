import streamlit as st
import openai
import tempfile
import os
import cv2
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip

# ------------------------------
# CONFIG
# ------------------------------
openai.api_key = "YOUR_OPENAI_API_KEY"

st.set_page_config(page_title="AI Marketing Video Generator", layout="wide")

# ------------------------------
# Title Section
# ------------------------------
st.title("🎥 AI Marketing Video Generator")
st.write("Generate marketing reels using AI – Script → Audio → Video → Final Reel")

# ------------------------------
# Step 1: User Input
# ------------------------------
st.subheader("📌 Step 1: Enter Company Details")

company_name = st.text_input("Company Name")
product_desc = st.text_area("Product Description")
target_audience = st.text_input("Target Audience")
promo_goal = st.text_input("Marketing Goal (ex: increase sales, get signups)")

generate_btn = st.button("Generate Script & Scenes")

# ------------------------------
# Step 2: Generate Script + Scenes
# ------------------------------
if generate_btn:
    if not all([company_name, product_desc, target_audience, promo_goal]):
        st.error("Please fill all fields.")
    else:
        with st.spinner("Generating script using AI..."):
            prompt = f"""
            Generate a 3-scene marketing video script.

            Company: {company_name}
            Product: {product_desc}
            Audience: {target_audience}
            Goal: {promo_goal}

            Output format:
            Scene 1 Description:
            Scene 1 Script:

            Scene 2 Description:
            Scene 2 Script:

            Scene 3 Description:
            Scene 3 Script:
            """

            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            ai_output = response["choices"][0]["message"]["content"]

        st.success("Script generated successfully!")
        st.write(ai_output)

        # Save the generated script
        with open("script.txt", "w") as f:
            f.write(ai_output)

        st.subheader("🎤 Step 3: Generate Voiceover (TTS)")
        if st.button("Generate Voice"):
            with st.spinner("Creating voiceover..."):
                tts = openai.audio.speech.create(
                    model="gpt-4o-mini-tts",
                    voice="alloy",
                    input=ai_output
                )
                audio_path = "audio.mp3"
                tts.stream_to_file(audio_path)

            st.audio(audio_path)
            st.success("Voiceover created!")

        st.subheader("🎬 Step 4: Generate Video Scenes")
        sample_videos = ["sample1.mp4", "sample2.mp4", "sample3.mp4"]  # you can replace with stock clips

        scene_clips = []
        for idx, vid in enumerate(sample_videos):
            if os.path.exists(vid):
                st.video(vid)
                scene_clips.append(VideoFileClip(vid))
            else:
                st.warning(f"Missing sample video: {vid}")

        st.subheader("🎞️ Step 5: Combine Video + Text + Audio")

        if st.button("Create Final Marketing Video"):
            with st.spinner("Processing..."):

                # Load voiceover audio
                audio = AudioFileClip("audio.mp3")

                # Process video
                clips_resized = [clip.resize(height=720) for clip in scene_clips]
                final_video = CompositeVideoClip(clips_resized)
                final_video = final_video.set_audio(audio)

                output_path = "final_marketing_video.mp4"
                final_video.write_videofile(output_path, fps=24)

            st.success("Your marketing video is ready!")
            st.video(output_path)

            st.download_button(
                label="⬇ Download Video",
                data=open(output_path, "rb").read(),
                file_name="marketing_video.mp4",
                mime="video/mp4"
            )