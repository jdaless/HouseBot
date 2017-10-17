from flask import Flask
from lib.telegram_wrapper import *

def apiThread(t, address):
	try:
		app = Flask(__name__)
		app.config['DEBUG'] = False
		app.config['SERVER_NAME'] = address + ":5000"

		@app.route("/doorbell")
		def doorbell():
			t.send_message("Ding-dong, somebody is at the door", t.HOUSE_CHAT_ID)
			return "Doorbell Rung"

		app.run(host='0.0.0.0')
	except Exception as e:
		print(e)
		apiThread(t, address)