from flask import Flask

from config import Configuration # import our configuration data.

app = Flask(__name__)
app.config.from_object(Configuration) # user values from our configuration object


