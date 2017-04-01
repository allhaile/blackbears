from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

messages = []

@app.route("/send-message")
#http://127.0.0.1:5000/send-message?user=USERHERE&message=MESSAGEHERE
def send():
	msg = {"From" : request.args.get("user"), "Message": request.args.get("message") }
	messages.append(msg)
	rv = jsonify({"result" :"Your message was sent", "total messages": len(messages) })
	return rv

@app.route("/get-messages")
def all_messages():
	return jsonify(messages)

if __name__ == "__main__" : app.run()