from twilio.rest import Client

# Your Twilio Account SID and Auth Token from https://console.twilio.com/


client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid=msg_service_sid,
    to="+818040832003",  # destination in E.164
    body="Hello from Twilio via Messaging Service 🚀"
)

print("SID:", message.sid)

