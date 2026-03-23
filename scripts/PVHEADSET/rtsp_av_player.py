import sys
import cv2
import subprocess
import numpy as np
import sounddevice as sd
import threading
import time

# -----------------------------
# PARAMETERS
# -----------------------------
if len(sys.argv) != 3:
    print("Usage: python rtsp_av_player.py <IP> <PORT>")
    sys.exit(1)

ip = sys.argv[1]
port = sys.argv[2]

RTSP_URL = f"rtsp://{ip}:{port}/live"
print(f"Reading RTSP stream from: {RTSP_URL}")

AUDIO_RATE = 48000
AUDIO_CHANNELS = 2
TARGET_FPS = 30.0
FRAME_INTERVAL = 1.0 / TARGET_FPS

# -----------------------------
# AUDIO THREAD (FFmpeg -> sounddevice)
# -----------------------------
def audio_thread():
    print("[AUDIO] Starting audio reader...")

    ffmpeg_cmd = [
        "ffmpeg",
        "-loglevel", "error",
        "-i", RTSP_URL,
        "-vn",                  # no video
        "-f", "f32le",          # raw PCM float32
        "-acodec", "pcm_f32le",
        "-ac", str(AUDIO_CHANNELS),
        "-ar", str(AUDIO_RATE),
        "-"
    ]

    proc = subprocess.Popen(
        ffmpeg_cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    def callback(outdata, frames, time_info, status):
        if status:
            print("[AUDIO] Status:", status)
        bytes_needed = frames * AUDIO_CHANNELS * 4  # float32 = 4 bytes
        raw = proc.stdout.read(bytes_needed)
        if not raw or len(raw) < bytes_needed:
            outdata[:] = np.zeros((frames, AUDIO_CHANNELS), dtype=np.float32)
            return
        audio = np.frombuffer(raw, dtype=np.float32)
        audio = audio.reshape(-1, AUDIO_CHANNELS)
        outdata[:] = audio

    with sd.OutputStream(
        samplerate=AUDIO_RATE,
        channels=AUDIO_CHANNELS,
        dtype="float32",
        callback=callback
    ):
        print("[AUDIO] Audio playback running.")
        while True:
            if proc.poll() is not None:
                print("[AUDIO] FFmpeg process ended.")
                break
            time.sleep(0.1)


# -----------------------------
# VIDEO THREAD (OpenCV)
# -----------------------------
def video_thread():
    print("[VIDEO] Opening RTSP video...")
    cap = cv2.VideoCapture(RTSP_URL)

    if not cap.isOpened():
        print("[VIDEO] Failed to open RTSP video.")
        return

    print("[VIDEO] Video stream opened.")
    last_frame_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[VIDEO] Lost video stream.")
            break

        cv2.imshow("RTSP Video", frame)

        now = time.time()
        elapsed = now - last_frame_time
        if elapsed < FRAME_INTERVAL:
            time.sleep(FRAME_INTERVAL - elapsed)
        last_frame_time = time.time()

        if cv2.waitKey(1) == 27:  # ESC to quit
            break

    cap.release()
    cv2.destroyAllWindows()
    print("[VIDEO] Video thread ended.")


# -----------------------------
# START THREADS
# -----------------------------
t_audio = threading.Thread(target=audio_thread, daemon=True)
t_video = threading.Thread(target=video_thread, daemon=True)

t_audio.start()
t_video.start()

t_video.join()
print("[MAIN] Exiting.")
