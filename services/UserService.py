from models.UserModel import db, User

def create_user(username):
    user = User(username=username)
    db.session.add(user)
    db.session.commit()