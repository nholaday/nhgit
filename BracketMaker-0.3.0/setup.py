from distutils.core import setup

setup(
    name='BracketMaker',
    version='0.3.0',
    author='Dylan Richardson',
    author_email='dylanrichardson1996@gmail.com',
    packages=['bracket'],
    scripts=['bin/main.py'],
    url='http://pypi.python.org/pypi/BracketMaker/',
    license='LICENSE.txt',
    description='Create and store readable brackets.',
    long_description=open('README.txt').read(),
    install_requires=[],
)