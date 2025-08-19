from twilio.rest import Client

# Your Twilio Account SID and Auth Token from https://console.twilio.com/
account_sid = "AC125ace9e8e3ce141287e642f4c51ee1d"
# account_sid = "SKbc128a74a621822aca0ef082361f1d62"
# auth_token = "w6Kj7fJhprztwy5bFVDyAFEXTPVx28z2"
auth_token = "18e88ceda6268a85a96853d861898409"
msg_service_sid = "MGd16e77736a10b4a36af553508ed1ba70"  # starts with "MG"

client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid=msg_service_sid,
    to="+818040832003",  # destination in E.164
    body="Hello from Twilio via Messaging Service 🚀"
)

print("SID:", message.sid)

