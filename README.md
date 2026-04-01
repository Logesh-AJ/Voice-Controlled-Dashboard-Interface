# 🎙️ Voice-Controlled Dashboard Interface

Real-time voice-controlled dashboard simulation using Faster-Whisper and Python, enabling dynamic UI updates based on spoken commands.

---

## 🧠 Tech Stack

* Python
* Faster-Whisper (Speech-to-Text)
* OpenCV
* Tkinter (GUI)
* NumPy

---

## 🚀 Key Features

* 🎤 Real-time voice command recognition
* ⚡ Fast transcription using Faster-Whisper
* 🖥️ Interactive dashboard UI updates
* 🔄 Live status control (engine, wiper, lights, etc.)
* 🧠 Multiple model support (tiny → large)

---

## 🎥 Demo Video

[▶ Watch Demo](https://youtu.be/VKOTKlumzl4)

---

## ⚙️ How It Works

1. Microphone captures voice input
2. Audio is processed using Faster-Whisper
3. Text is interpreted as commands
4. Dashboard UI updates in real-time

---

## ⚡ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Logesh-AJ/Voice-Controlled-Dashboard-Interface.git
```

### 2. Navigate to project folder

```bash
cd Voice-Controlled-Dashboard-Interface
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python src/main.py
```

---

## ⚙️ System Requirements

* Python >= 3.11
* Microphone (for voice input)
* Internet connection (required for model download)
* OS: Windows / Linux / macOS

---

## 📦 Dependencies

* faster-whisper
* opencv-python
* numpy
* pillow

---

## 🧠 Whisper Model Selection

The system supports multiple Faster-Whisper models.
You can change the model by editing the model name in the code.

Example:

```python
model = WhisperModel("small")
```

---

## 📊 Available Models

Based on Faster-Whisper capabilities :

| Model         | Size    | Speed      | Accuracy | RAM     |
| ------------- | ------- | ---------- | -------- | ------- |
| tiny          | ~39 MB  | 🚀 Fastest | Low      | ~1.5 GB |
| base          | ~74 MB  | ⚡ Fast     | Fair     | ~2 GB   |
| small         | ~244 MB | Moderate   | Good     | ~4 GB   |
| medium        | ~769 MB | Slow       | Great    | ~8 GB   |
| large-v1 / v2 | ~1.5 GB | Slower     | Best     | 16+ GB  |

---

## ⚠️ Important Notes

* 🔌 Internet connection is required **on first run**

  * The selected model will be downloaded automatically

* 🧠 Model selection affects:

  * Speed
  * Accuracy
  * System performance

* ⚠️ `large-v3` is NOT supported in Faster-Whisper (OpenAI only)

---

## 📁 Project Structure

```bash
Voice-Controlled-Dashboard-Interface/
 ├── src/
 ├── dashboard_image/
 ├── other_models/
 ├── Demo_video
 ├── README.md
 └── requirements.txt
```

---

## 📌 Applications

* Smart vehicle dashboard systems
* Voice-controlled automation
* Human-machine interaction
* Assistive technologies

---

## 🚧 Future Improvements

* Offline command mapping optimization
* Noise filtering and speech enhancement
* Multi-language support
* Integration with real hardware (IoT / vehicle systems)

---

## 👤 Author

**Logesh A J**

---
