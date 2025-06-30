from flask import Flask, render_template, jsonify
from threading import Thread

app = Flask(__name__)

assistant_state = {
    "user_input": "",
    "intent": "",
    "response": ""
}

@app.route('/')
def index():
    return render_template("index.html", state=assistant_state)

@app.route('/api/state')
def get_state():
    return jsonify(assistant_state)

def update_state(user_input, intent, response):
    assistant_state["user_input"] = user_input
    assistant_state["intent"] = intent
    assistant_state["response"] = response

def start_dashboard():
    thread = Thread(target=app.run, kwargs={"debug": False, "use_reloader": False})
    thread.daemon = True
    thread.start()
