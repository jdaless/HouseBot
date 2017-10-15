from flask import Flask
from lib.telegram_wrapper import *

def apiThread(t):
	app = Flask(__name__)
	app.config['DEBUG'] = False
	app.config['SERVER_NAME'] = "24.29.28.245:5000"

	@app.route("/doorbell")
	def doorbell():
		t.send_message("Ding-dong, somebody is at the door", t.HOUSE_CHAT_ID)
		return "Doorbell Rung"

	app.run(host='0.0.0.0')