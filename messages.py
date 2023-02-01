import discord

users = dict()


def add(user):
    global users
    users[user] = 1


def exists(user):
    global users
    return user in users.keys()


def update(user):
    global users
    users[user] = users[user] + 1


def read(user):
    global users
    if exists(user):
        return users[user]
    else:
        return 0


def report():
    global users
    for key in users.keys():
        print(key.name + ': ' + str(read(key)))
