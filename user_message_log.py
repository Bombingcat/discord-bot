import pickle
message_counts = {}


def load():
    global message_counts
    try:
        with open('messagecount.pickle','rb') as f:
            message_counts = pickle.load(f)
    except:
        pass
    
def save():
    with open('messagecount.pickle','wb') as f:
        pickle.dump(message_counts,f)

def inc_user_msg(userid):
    global message_counts
    message_counts.setdefault(userid,0)
    message_counts[userid] = message_counts[userid] + 1
    save()
# inc_user_msg('cyriel')
# inc_user_msg('arne')
# inc_user_msg('ruy')
# inc_user_msg('cyriel')
# print (message_counts)