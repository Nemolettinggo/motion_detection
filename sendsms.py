from twilio.rest import Client

#This is the function which automaticially send the msg ,if a motion is detected. it will only send msg once as you can
#see the flag. check the motion_detection for detail


#I use a twilio service 2 do this, the only thing you need to do is get your own twilio account. and fullfil the info
#below, which is the following:

# target number : the number your want to send the msg to
# your msg: the msg you want to send
# your twilio number, when you finished registration you will get a number from twilio


def sendsms():

    auth_token = 'your token'
    account_sid = "account sid"
    client = Client(account_sid, auth_token[0][0])
    message = client.messages.create(
        "target number",
        body= 'your msg',
        from_= 'your twilio number',
    )
    flag = 0
