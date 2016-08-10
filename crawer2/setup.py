from distutils.core import setup
import py2exe
setup(
	options = {'py2exe': {
        'bundle_files': 1
    }},
	console = [{'script': 'images_crawler2.py'}],
	zipfile = None
)