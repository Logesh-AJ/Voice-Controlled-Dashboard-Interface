import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import numpy as np
import sounddevice as sd
import tempfile
import scipy.io.wavfile as wav
from faster_whisper import WhisperModel
import queue

# ========== SETTINGS ==========
SAMPLE_RATE = 16000
BUFFER_DURATION = 5
BUFFER_SIZE = int(SAMPLE_RATE * BUFFER_DURATION)
LANGUAGE = "en"
INPUT_DEVICE_INDEX = 2  # Set your mic index here

# ========== MODEL LOAD ==========
model = WhisperModel("tiny", device="cpu", compute_type="int8")

# ========== GLOBALS ==========
recording = False
audio_buffer = []
q = queue.Queue()

# ========== INTERFACE ==========
class VoiceControlUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🚘 Voice Command Interface")
        self.root.configure(bg="#1e1e1e")
        self.status = {
            "engine": tk.StringVar(value="OFF"),
            "wiper": tk.StringVar(value="OFF"),
            "beam": tk.StringVar(value="OFF"),
            "indicator_left": tk.StringVar(value="OFF"),
            "indicator_right": tk.StringVar(value="OFF")
        }

        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="Voice Dashboard", font=("Arial", 18, "bold"),
                 fg="#00ffcc", bg="#1e1e1e").pack(pady=10)

        for key, var in self.status.items():
            frame = tk.Frame(self.root, bg="#1e1e1e")
            frame.pack(pady=3)
            tk.Label(frame, text=f"{key.replace('_',' ').title()}:", font=("Arial", 12),
                     fg="white", bg="#1e1e1e").pack(side="left", padx=10)
            tk.Label(frame, textvariable=var, font=("Arial", 12, "bold"),
                     fg="#00ff00", bg="#1e1e1e").pack(side="left")

        self.transcript = scrolledtext.ScrolledText(self.root, height=8, bg="#121212",
                                                    fg="#00ffcc", insertbackground="white",
                                                    font=("Consolas", 11))
        self.transcript.pack(padx=10, pady=10, fill="both", expand=True)

        btn_frame = tk.Frame(self.root, bg="#1e1e1e")
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="🎙️ Start Recording", command=self.start_recording).pack(side="left", padx=10)
        ttk.Button(btn_frame, text="⏹️ Stop & Transcribe", command=self.stop_recording).pack(side="left", padx=10)

    def start_recording(self):
        global recording, audio_buffer
        recording = True
        audio_buffer = []
        sd.default.device = (INPUT_DEVICE_INDEX, None)

        def callback(indata, frames, time, status):
            if recording:
                q.put(indata.copy())

        threading.Thread(target=self.record_thread, args=(callback,), daemon=True).start()
        self.log("🎤 Recording started...")

    def stop_recording(self):
        global recording
        recording = False
        self.log("⏹️ Recording stopped. Transcribing...")
        threading.Thread(target=self.transcribe_audio, daemon=True).start()

    def record_thread(self, callback):
        with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype='float32', callback=callback):
            while recording:
                try:
                    chunk = q.get(timeout=1)
                    audio_buffer.append(chunk)
                except queue.Empty:
                    break

    def transcribe_audio(self):
        if not audio_buffer:
            self.log("⚠️ No audio recorded.")
            return

        audio_data = np.concatenate(audio_buffer, axis=0)
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            wav.write(f.name, SAMPLE_RATE, (audio_data * 32767).astype(np.int16))
            segments, _ = model.transcribe(f.name, language=LANGUAGE)
            for segment in segments:
                self.log(f"🧠 {segment.text}")
                self.execute_command(segment.text.lower())

    def log(self, text):
        self.transcript.insert(tk.END, text + "\n")
        self.transcript.see(tk.END)

    def execute_command(self, text):
        # Normalize
        text = text.lower()

        # Engine
        if "engine" in text:
            if "on" in text or "start" in text:
                self.status["engine"].set("ON")
            elif "off" in text or "stop" in text:
                self.status["engine"].set("OFF")

        # Wiper
        if "wiper" in text:
            if "on" in text or "start" in text:
                self.status["wiper"].set("ON")
            elif "off" in text or "stop" in text:
                self.status["wiper"].set("OFF")

        # Beam
        if "beam" in text:
            if "high" in text:
                self.status["beam"].set("HIGH")
            elif "low" in text:
                self.status["beam"].set("LOW")
            elif "off" in text:
                self.status["beam"].set("OFF")

        # Indicator Left
        if "indicator left" in text:
            if "on" in text:
                self.status["indicator_left"].set("ON")
            elif "off" in text:
                self.status["indicator_left"].set("OFF")

        # Indicator Right
        if "indicator right" in text:
            if "on" in text:
                self.status["indicator_right"].set("ON")
            elif "off" in text:
                self.status["indicator_right"].set("OFF")

# ========== LAUNCH ==========
if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use("clam")
    app = VoiceControlUI(root)
    root.mainloop()
