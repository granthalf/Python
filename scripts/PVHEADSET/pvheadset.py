#!/usr/bin/env python3
#Python Virtual Headset
import subprocess

#WINDOWS
audio_device = 'audio=Mixage stéréo (Realtek(R) Audio)'

cmd = [
    "ffmpeg",
    "-re",
    "-f", "dshow",
    "-rtbufsize", "1500M",
    "-i", audio_device,
    "-acodec", "aac",
    "-ar", "48000",
    "-ac", "2",
    "-f", "rtsp",
    "-rtsp_transport", "tcp",
    "rtsp://0.0.0.0:8554/audio"
]

print("LAUNCH A SERVER RTSP…")
print(" ".join(cmd))

try:
    subprocess.run(cmd)
except KeyboardInterrupt:
    print("Stop requested.")
