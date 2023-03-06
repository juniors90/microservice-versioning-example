import os
import unittest

from flask import render_template_string

from application import create_app, db
from application.models.person import Person
from application.models.note import Note
from tests.build_database import mock_db


environment = os.getenv("APIREST_MODE", "development")

if environment == "development":
    from dotenv import load_dotenv
    load_dotenv()

if environment == "production":
    import sentry_sdk
    from sentry_sdk.integrations.flask import FlaskIntegration

    sentry_dsn = os.getenv("SENTRY_DSN", None)
    sentry_sdk.init(
        dsn=sentry_dsn,
        integrations=[
            FlaskIntegration(),
        ],
        traces_sample_rate=1.0,
        environment=environment,
    )

app = create_app(environment)

home_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>RP Flask REST API</title>
    </head>
    <body>
        <h1>Hello, People!</h1>
        {% for person in people %}
        <h2>{{ person.fname }} {{ person.lname }}</h2>
        <ul>
            {% for note in person.notes %}
            <li>{{ note.content }}</li>
            {% endfor %}
        </ul>
        {% endfor %}
    </body>
    </html>
    """


@app.route("/")
def home():
    people = Person.query.all()
    return render_template_string(home_html, people=people)


@app.before_first_request
def mock_database():
    if os.getenv("APIREST_MOCK"):
        with app.app_context():
            db.drop_all()
            db.create_all()
            mock_db()
    print("Done!")
    return "done!"


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover("tests", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 0


@app.cli.command()
def mock():
    db.drop_all()
    db.create_all()
    mock_db()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
