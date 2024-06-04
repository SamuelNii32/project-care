import imp
import os
import sys

from server.wsgi import application

from whitenoise import WhiteNoise


sys.path.insert(0, os.path.dirname(__file__))

application = WhiteNoise(application, root="pyapps/project-care/staticfiles")
