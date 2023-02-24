# -*- coding: utf-8 -*-
"""Wrapper for OpenAI API for Language Models"""
from flask import Flask, render_template, jsonify
import openai
import time
import threading
import sys
import webbrowser
import psutil

config = {
    "api_key": "place-your-api-key-here",
    "model": "text-davinci-003",  # check https://platform.openai.com/docs/models/ for other models
    "engine": None,
    "max_tokens": 32,  # maximum amount of returned tokens
    "temperature": 0.15,  # increases randomness
    "stream": True,  # stream response per token instead of a single string
    "echo": False,
    "session_spent": 0,
    "session_spent_text": "",
    "status": "N/A",
    "price_per_token": 0.1200 / 1000,  # estimation of cost, based on text-davinci-003 model
    "stop_after_one_request": False,
    "done": False,
    "completion_text": "",
    "input_prompt": ""
}
openai.api_key = config["api_key"]
app = Flask(__name__, template_folder=".")


@app.route('/')
def index():
    """Landing page; If app is called with arguments, server will shut down after first request"""

    global config

    if config["input_prompt"]:
        config["stop_after_one_request"] = True
        threading.Thread(target=openai_call_thread).start()

    return render_template('index.html')


def shutdown_flask():
    for p in psutil.process_iter():
        if p.name().startswith("python"):  # might need to exchange for sys.executable
            if len(p.cmdline()) > 2 and p.cmdline()[1] == "app.py":
                time.sleep(0.5)
                p.kill()


def openai_call_thread():
    """Worker thread for API call to OpenAI"""
    global config

    config["completion_text"] = ""
    config["done"] = False
    collected_events = []
    start_time = time.time()

    # check https://platform.openai.com/docs/api-reference/completions/create for arguments
    try:
        response = openai.Completion.create(model=config["model"],
                                            engine=config["engine"],
                                            prompt=config["input_prompt"],
                                            echo=config["echo"],
                                            temperature=config["temperature"],
                                            max_tokens=config["max_tokens"],
                                            stream=config["stream"])
    except Exception as exc:
        config["done"] = True
        config["status"] = f"<span class='error'>Error: {exc}</span>"
        shutdown_flask()

    if config["stream"]:
        for event in response:
            collected_events.append(event)
            config["completion_text"] += event["choices"][0]["text"]
        config["session_spent_text"] = "N/A when using stream=True"
        config["done"] = True

    else:
        config["completion_text"] = response["choices"][0]["text"]
        used_tokens = response.usage.total_tokens
        call_cost = used_tokens*config["price_per_token"]
        config["session_spent"] += call_cost
        config["session_spent_text"] = f"{used_tokens} tokens ({round(call_cost, 5)}$)"
        if not config["stop_after_one_request"]:
            config["session_spent_text"] += f" (session: {round(config['session_spent'], 5)}$)"
        config["done"] = True

    if config["stop_after_one_request"] and config["done"]:
        config["status"] = f"Finished in {round(time.time() - start_time, 3)} s"
        shutdown_flask()


@app.route("/openai_call/<string:prompt>")
def openai_call(prompt: str = None):
    """API endpoint if app is started without arguments; Could be implemented w. input + button """
    global config
    config["input_prompt"] = prompt
    threading.Thread(target=openai_call_thread).start()

    # hide API_KEY in returned config
    return jsonify(status="Started API call in thread",
                   config={key: val for key, val in config.items() if key != "api_key"})


@app.route('/update')
def update():
    """Routine to fetch data, started with setInterval(getResults, interval) in index.html"""
    return jsonify(config={key: val for key, val in config.items() if key != "api_key"})


if __name__ == "__main__":
    if len(sys.argv) > 1:
        config["input_prompt"] = " ".join(sys.argv[1:])

    webbrowser.open("http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=False)
