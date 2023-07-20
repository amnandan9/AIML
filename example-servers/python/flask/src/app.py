from requests.exceptions import ConnectionError
from services.huggingFace import HuggingFace
from services.custom import Custom
from services.openAI import OpenAI
from services.cohere import Cohere
from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS

# ------------------ SETUP ------------------

load_dotenv()

app = Flask(__name__)

# this will need to be reconfigured before taking the app to production
cors = CORS(app)

# ------------------ EXCEPTION HANDLERS ------------------

# Sends response back to Deep Chat using the Result format:
# https://deepchat.dev/docs/connect/#Result
@app.errorhandler(Exception)
def handle_exception(e):
    print(e)
    return {'error': str(e)}, 500

@app.errorhandler(ConnectionError)
def handle_exception(e):
    print(e)
    return {'error': 'Internal service error'}, 500

# ------------------ CUSTOM API ------------------

custom = Custom()

@app.route("/chat", methods=["POST"])
def chat():
    body = request.json
    return custom.chat(body)

@app.route("/chat-stream", methods=["POST"])
def chat_stream():
    body = request.json
    return custom.chat_stream(body)

@app.route("/files", methods=["POST"])
def files():
    return custom.files(request)

# ------------------ OPENAI API ------------------

open_ai = OpenAI()

@app.route("/openai-chat", methods=["POST"])
def openai_chat():
    body = request.json
    return open_ai.chat(body)

@app.route("/openai-chat-stream", methods=["POST"])
def openai_chat_stream():
    body = request.json
    return open_ai.chat_stream(body)

@app.route("/openai-image", methods=["POST"])
def openai_image():
    files = request.files.getlist('files')
    return open_ai.image_variation(files)

# ------------------ HUGGING FACE API ------------------

huggingFace = HuggingFace()

@app.route("/huggingface-conversation", methods=["POST"])
def hugging_face_conversation():
    body = request.json
    return huggingFace.conversation(body)

@app.route("/huggingface-image", methods=["POST"])
def hugging_face_image_classification():
    files = request.files.getlist('files')
    return huggingFace.image_classification(files)

@app.route("/huggingface-speech", methods=["POST"])
def hugging_face_speech_recognition():
    files = request.files.getlist('files')
    return huggingFace.speech_recognition(files)

# ------------------ COHERE API ------------------

cohere = Cohere()

@app.route("/cohere-generate", methods=["POST"])
def cohere_generate_text():
    body = request.json
    return cohere.generate_text(body)

@app.route("/cohere-summarize", methods=["POST"])
def cohere_summarize_text():
    body = request.json
    return cohere.summarize_text(body)

# ------------------ START SERVER ------------------

if __name__ == "__main__":
    app.run(port=8080)