from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

messages = []

@app.route("/send-message", methods =['POST', 'GET'])
#http://127.0.0.1:5000/send-message?user=USERHERE&message=MESSAGEHERE
def send():

	# message_box = """<form>
	# 	Message: <br>
	# <input type="text" name="message"><br>
	# <input type="button" onclick="alert("message sent")>Send<br>
	# <form>
	# """

	nearbyStuff = []
	if request.method =='POST':
		sent_message = request.form['message']
		if sent_message:
			print("Message")
			msg = {"From" : request.form['user'], "Message": request.form['message'] }
			messages.append(msg)
		elif request.form['findNearby']:
			nearbyStuff.append('Food')

#	if request.method =='GET':
	if request.form['user']:
		return print_page(request.form['user'], nearbyStuff)
	else:
		return print_page('', nearbyStuff)


	#rv = jsonify({"result" :"Your message was sent", "total messages": len(messages) })
	#return rv

@app.route("/get-messages")
def all_messages():
	return jsonify(messages)


def print_page(user, nearbyStuff):
	message_box = f"""<form action="/send-message" method="post" id="mform">
 	User Name: <input type= "text" name="user" value="{user}"><br>
 	Message: <input type="text" name="message"><br>
	<button type="submit" form="mform" value="Submit">Submit</button>
	<input type="submit" value="Find Nearby Stuff" name="findNearby">	</form>"""
	# todo make a frm to submit lcatin to get nearby stuff

	message_box = message_box + '<ul>'
	for message in messages:
		print(jsonify(message))
		message_box = message_box + '<li>' + message['Message']
	message_box = message_box + '</ul>'

	if nearbyStuff:
		message_box = message_box + str(nearbyStuff)
		
	return message_box

if __name__ == "__main__" : app.run()