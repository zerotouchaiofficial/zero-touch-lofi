import numpy as np
import random
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import os

# -------------------------
# SETTINGS
# -------------------------
channel_name = "Zero Touch AI Lofi"
width, height = 1280, 720
fps = 30

# -------------------------
# RANDOM MOOD
# -------------------------
moods = ["Deep Focus", "Chill Study", "Coding Flow", "Night Relax"]
mood = random.choice(moods)

# -------------------------
# LOAD AUDIO (already generated)
# -------------------------
wav_file = "output.wav"
audio = AudioFileClip(wav_file)
duration = audio.duration

# -------------------------
# BACKGROUND
# -------------------------
background = ColorClip((width, height), color=(10, 10, 20), duration=duration)

# -------------------------
# FLOATING BALLS
# -------------------------
balls = []
for i in range(6):
    phase_x = random.uniform(0, 10)
    phase_y = random.uniform(0, 10)

    ball = (
        ColorClip((60, 60), color=(255, 255, 255))
        .set_opacity(0.2)
        .set_duration(duration)
        .set_position(lambda t, px=phase_x, py=phase_y:
            (width/2 + np.sin(t + px) * 350,
             height/2 + np.cos(t + py) * 200))
    )
    balls.append(ball)

# -------------------------
# TEXT OVERLAY
# -------------------------
img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

try:
    font_big = ImageFont.truetype("DejaVuSans-Bold.ttf", 90)
    font_small = ImageFont.truetype("DejaVuSans-Bold.ttf", 50)
except:
    font_big = ImageFont.load_default()
    font_small = ImageFont.load_default()

main_text = "AI LOFI"
sub_text = mood

w1, h1 = draw.textbbox((0, 0), main_text, font=font_big)[2:]
w2, h2 = draw.textbbox((0, 0), sub_text, font=font_small)[2:]

draw.text(((width-w1)/2, height/3), main_text, font=font_big, fill="white")
draw.text(((width-w2)/2, height/2), sub_text, font=font_small, fill="white")

text_clip = ImageClip(np.array(img)).set_duration(duration)

# -------------------------
# COMBINE VIDEO
# -------------------------
final = CompositeVideoClip([background] + balls + [text_clip])
final = final.set_audio(audio)

final.write_videofile(
    "final_video.mp4",
    fps=fps,
    codec="libx264",
    audio_codec="aac",
    preset="ultrafast"
)

# -------------------------
# GENERATE THUMBNAIL
# -------------------------
thumb = Image.new("RGB", (1280, 720), (15, 15, 30))
draw = ImageDraw.Draw(thumb)

draw.text((200, 250), "AI LOFI", font=font_big, fill="white")
draw.text((200, 400), mood, font=font_small, fill="white")

thumb.save("thumbnail.jpg")

# -------------------------
# SAVE METADATA
# -------------------------
title = f"AI Lofi Beats 🌧️ {mood} Mix | Rain Study Music"
description = f"""
🎧 AI Generated Lofi Music
🌧 Light Rain Ambience
🧠 Perfect for {mood}

New AI music uploaded daily.

#Lofi #AIMusic #RainSounds #StudyMusic #FocusMusic
"""

with open("meta.txt", "w") as f:
    f.write(title + "\n---\n" + description)

print("Video + Thumbnail + Metadata Created")
