from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

from travelbuddy import settings

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()


def create_app():
    app = Flask(__name__)

    config = settings.get_config()
    db_conf = config.database

    app.config.from_object(config)

    app.config.update(
        {
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
            "SQLALCHEMY_DATABASE_URI": f"mysql+pymysql://"
            f"{db_conf.user}:{db_conf.password}@{db_conf.host}:{db_conf.port}/{db_conf.name}"
            f"?charset=utf8mb4",
        }
    )

    db.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)
    return app


app = create_app()
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()


@app.route("/")
def hello_world():
    return "Hello World!"
