from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(
        {
            "status": "ok",
            "message": "Vercel deployment is working.",
            "note": "This repository contains a terminal game (game.py). "
            "Interactive terminal input is not supported on Vercel.",
            "run_locally": "python3 game.py",
        }
    )


@app.get("/health")
def health():
    return jsonify({"healthy": True})
