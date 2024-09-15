from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.String(20), nullable=False, default='pendiente')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)