from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
class TwilioClient:
    
    
    def __init__(self):
        self.account_sid = 'AC6e3a23d3d7761990ee62461548c8cb0b'
        self.auth_token = ''
       
        self.client = Client(self.account_sid, self.auth_token)

    def sendMessage(self):
        message = self.client.messages \
                        .create(
                            body="Let's grab lunch at Milliways tomorrow!",
                            from_='+15029121597',
                            to='+16306974762'
                        )

        print(message.sid)