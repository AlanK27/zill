
from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='zill',
    version='0.1.0',
    description='Deplyoment of scraping Redfin and Node.js webserver',
    long_description=readme,
    author='Alan Tam',
    author_email='tam_kai@yahoo.com',
    url='https://github.com/AlanK27/zill',
    license=license
)