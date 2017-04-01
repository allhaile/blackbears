from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

messages = []

@app.route("/outdoor-message-board", methods =['GET'])

#initial message should go to this route, then after messages are put in it 
#will redirect to the /send-message route

#error occurs if we go directly to send-message route

def test():
	return print_page("User", [])

@app.route("/send-message", methods =['POST', 'GET'])
#http://127.0.0.1:5000/send-message?user=USERHERE&message=MESSAGEHERE
def send():
	print("got to send")

	# message_box = """<form>
	# 	Message: <br>
	# <input type="text" name="message"><br>
	# <input type="button" onclick="alert("message sent")>Send<br>
	# <form>
	# """


	nearbyStuff = []
	if request.method =='POST':
		if request.form['message']:
	 		sent_message = request.form['message']
 			print("Message")
 			msg = {"From" : request.form['user'], "Message": request.form['message'] }
 			messages.append(msg)
 			return print_page(request.form['user'], nearbyStuff)
# 		elif request.form['findNearby']:
# 			nearbyStuff.append('Food')

	elif request.method =='GET':
		print("made it to GET")
		if request.form['user']:
 			return print_page(request.form['user'], nearbyStuff)
		else:
 			prrint_page('', nearbyStuff)



# 	rv = jsonify({"result" :"Your message was sent", "total messages": len(messages) })
# 	return rv

@app.route("/get-messages")
def all_messages():
	return jsonify(messages)


def print_page(user, nearbyStuff):
	message_box = """<form action="/send-message" method="post" id="mform">
	<h1 style="font-family:verdana;">Meet travelers in the area interested in exploring the Outdoors</h1>

	<body style="background-color:powderblue;">

	User Name: <input type= "text" name="user" value="{user}"><br>
	Message: <input type="text" name="message" value="message"><br>
	<button type="submit" form="mform" value="Submit">Submit</button> </form>"""
	# todo make a frm to submit lcatin to get nearby stuff

	message_box = message_box + '<ul>'
	for message in messages:
		#print(jsonify(message))
		message_box = message_box + '<li>' + message['From'] + ": "+ message['Message']
	message_box = message_box + '</ul>'

	if nearbyStuff:
		message_box = message_box + str(nearbyStuff)

	return message_box

if __name__ == "__main__" : app.run()