#!/usr/bin/env python3
#Python Virtual Headset
import subprocess
import re

def detect_devices():
    print("Detecting DirectShow devices...")
    cmd = ["ffmpeg", "-list_devices", "true", "-f", "dshow", "-i", "dummy:"]
    proc = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    output = proc.stderr.read()

    video_devices = []
    audio_devices = []

    # Regex to extract device names
    video_pattern = r'"(.+?)"\s+\(video\)'
    audio_pattern = r'"(.+?)"\s+\(audio\)'

    video_devices = re.findall(video_pattern, output)
    audio_devices = re.findall(audio_pattern, output)

    return video_devices, audio_devices


def choose_best_audio(audio_devices):
    # Priority: Stereo Mix > Jabra > Realtek > anything else
    for dev in audio_devices:
        if "Stereo Mix" in dev or "Mixage stéréo" in dev:
            return dev
    for dev in audio_devices:
        if "Jabra" in dev:
            return dev
    for dev in audio_devices:
        if "Realtek" in dev:
            return dev
    return audio_devices[0] if audio_devices else None


def choose_best_video(video_devices):
    # Priority: integrated webcam
    for dev in video_devices:
        if "Integrated" in dev or "Webcam" in dev:
            return dev
    return video_devices[0] if video_devices else None


def start_rtsp(video_device, audio_device):
    print(f"Selected webcam: {video_device}")
    print(f"Selected microphone: {audio_device}")

    cmd = [
        "ffmpeg",
        "-f", "dshow",
        "-rtbufsize", "1500M",
        "-i", f"video={video_device}:audio={audio_device}",
        "-vcodec", "libx264",
        "-preset", "veryfast",
        "-tune", "zerolatency",
        "-acodec", "aac",
        "-ar", "48000",
        "-ac", "2",
        "-f", "rtsp",
        "-rtsp_transport", "tcp",
        "rtsp://0.0.0.0:8554/live"
    ]

    print("Starting RTSP stream…")
    print(" ".join(cmd))
    subprocess.run(cmd)


if __name__ == "__main__":
    video_devices, audio_devices = detect_devices()

    if not video_devices:
        print("No video devices detected.")
        exit()

    if not audio_devices:
        print("No audio devices detected.")
        exit()

    video = choose_best_video(video_devices)
    audio = choose_best_audio(audio_devices)

    start_rtsp(video, audio)
