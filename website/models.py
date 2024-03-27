from flask import Blueprint, render_template, request, send_from_directory
import os
import openai

UPLOAD_FOLDER = "website/static/uploads"  
models = Blueprint("models", __name__)

openai.api_key = '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'

# Function to transcribe audio using OpenAI API
def transcribe_audio(audio_file_path):
    try:
        response = openai.Audio.transcriptions.create(model="whisper-1", file=audio_file_path)
        return response['text']
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        return None

# Function to transcribe video using OpenAI API
def transcribe_video(video_file_path):
    try:
        response = openai.Video.transcriptions.create(model="whisper-1", file=video_file_path)
        return response['text']
    except Exception as e:
        print(f"Error transcribing video: {e}")
        return None

# Function to detect profanity in text
def detect_profanity(text):
    profane_words = set(["profane_word_1", "profane_word_2", "profane_word_3"])  # Add profane words here
    words = text.lower().split()
    profane_count = sum(word in profane_words for word in words)
    return profane_count > 0

# Route for the home page and file upload
@models.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'audio' in request.files:
            audio_file = request.files['audio']
            if audio_file:
                audio_filename = audio_file.filename
                audio_file_path = os.path.join(UPLOAD_FOLDER, audio_filename)
                audio_file.save(audio_file_path)
                transcribed_text = transcribe_audio(audio_file_path)
                if transcribed_text:
                    profanity_detected = detect_profanity(transcribed_text)
                    return render_template('result.html', text=transcribed_text, profanity_detected=profanity_detected)
                else:
                    return "Error transcribing audio file"
        elif 'video' in request.files:
            video_file = request.files['video']
            if video_file:
                video_filename = video_file.filename
                video_file_path = os.path.join(UPLOAD_FOLDER, video_filename)
                video_file.save(video_file_path)
                transcribed_text = transcribe_video(video_file_path)
                if transcribed_text:
                    profanity_detected = detect_profanity(transcribed_text)
                    return render_template('result.html', text=transcribed_text, profanity_detected=profanity_detected)
                else:
                    return "Error transcribing video file"
    return render_template('index.html')

@models.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
