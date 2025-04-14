import threading
import speech_recognition as sr

def mic_thread(label):
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)

    while True:
        with mic as source:
            try:
                audio = r.listen(source, phrase_time_limit=5)
                text = r.recognize_google(audio)
                label.setText(f"🎤 {text}")
            except sr.UnknownValueError:
                continue
            except sr.RequestError as e:
                label.setText(f"[Mic Error] {e}")
                break

def start_transcription(label):
    threading.Thread(target=mic_thread, args=(label,), daemon=True).start()
