from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.player import player as player_blueprint
    app.register_blueprint(player_blueprint)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='192.168.86.4',port='5002')
