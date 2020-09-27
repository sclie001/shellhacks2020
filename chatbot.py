from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from icebreaker import choose_icebreaker
from profanity_filter import ProfanityFilter

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
	incoming_msg = request.values.get('Body', '')
	resp = MessagingResponse()
	msg = resp.message()
	msg.body("")
	if "!start" in incoming_msg:
		msg.body("Greetings! I am ModBot, here to watch over this chat. \n\nNow that you're all here, feel free to introduce yourselves. To break the ice, answer the following question: " + choose_icebreaker())
	elif "!icebreaker" in incoming_msg:
		msg.body("Answer the question: " + choose_icebreaker())
	else:
		pf = ProfanityFilter()
		if not pf.is_clean(incoming_msg):
			msg.body("Please refrain from using inappropriate language. This is meant to be a safe space.")
	return str(resp)

if __name__ == "__main__":
	app.run()