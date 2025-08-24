from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '')
    resp = MessagingResponse()
    msg = resp.message()
    resposta = f"Olá! Recebi sua mensagem: {incoming_msg}"
    msg.body(resposta)
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)