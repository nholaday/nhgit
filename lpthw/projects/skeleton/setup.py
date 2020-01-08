try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup


config = {
	'description': 'New Project',
	'author': 'Nic Holaday',
	'url': '',
	'download_url': "Where to download it.",
	'author_email': "nic.holaday@comfyapp.com",
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ["MainSkel"]
	'scripts': [],
	'name': 'projectname'
}

setup(**config)
