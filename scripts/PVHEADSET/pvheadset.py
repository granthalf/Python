# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#Python Virtual Headset
import cv2
import sounddevice as sd
import subprocess
import numpy as np

# --- VIDEO (Media Foundation) ---
cap = cv2.VideoCapture(0, cv2.CAP_MSMF)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# --- AUDIO (WASAPI) ---
audio_rate = 48000
audio_channels = 2

print("Server: rtsp://0.0.0.0:8554/live")

# --- FFmpeg ---
ffmpeg_cmd = [
    "ffmpeg",
    "-y",
    # VIDEO
    "-f", "rawvideo",
    "-pix_fmt", "bgr24",
    "-s", "1280x720",
    "-r", "30",
    "-i", "-",
    # AUDIO
    "-f", "f32le",
    "-ar", str(audio_rate),
    "-ac", str(audio_channels),
    "-i", "-",
    # ENCODING
    "-vcodec", "libx264",
    "-preset", "veryfast",
    "-tune", "zerolatency",
    "-acodec", "aac",
    "-f", "rtsp",
    "-rtsp_transport", "tcp",
    "rtsp://0.0.0.0:8554/live"
]

proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)

def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    proc.stdin.write(indata.tobytes())

stream = sd.InputStream(
    channels=audio_channels,
    samplerate=audio_rate,
    callback=audio_callback
)

with stream:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        proc.stdin.write(frame.tobytes())
