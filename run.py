from app import create_app
from views.UserView import main

app = create_app()
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
