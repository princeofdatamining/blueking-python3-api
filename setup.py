from distutils.core import setup
from setuptools import find_packages


app_id = "bkapi"
app_name = "blueking-api"
app_description = "Blueking api package."
app_version = __import__(app_id).__version__
app_requires = [
]


setup(name=app_name,
      description=app_description,
      version=app_version,
      packages=find_packages(exclude=["tests"]),
      install_requires=app_requires)
