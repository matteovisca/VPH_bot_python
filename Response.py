from datetime import datetime

def sample_response(imput_text):
    user_message=str(imput_text).lower()

    if user_message in ('hello', 'hi'):
        return "Hi how it's going?"

    if user_message in ('who are you?', 'who are you'):
        return "I am a test bot!"

    if user_message in ('time', "what's time is it?"):
        now = datetime.now()
        date_time= now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    return "I don't understad you!!"