# import db
# from zione import db

def authenticate(username, password):
    user = db.auth("users", {username: password})
    return user

def identity(payload):
    user_id = payload['identity']
    return db.auth_user(user_id, None)

