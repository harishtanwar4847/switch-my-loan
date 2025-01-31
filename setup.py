from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in switch_my_loan/__init__.py
from switch_my_loan import __version__ as version

setup(
	name='switch_my_loan',
	version=version,
	description='Switch My Loan',
	author='Atrina Technologies Pvt Ltd',
	author_email='developers@atriina.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
