import setuptools

with open('README.md','r') as file:
	long_description = file.read()

setuptools.setup(
	name = 'preprocess_kgptalkie',
	version ='0.0.2',
	author ='mohamedbayomy',
	author_email='udemy@kgptalkie.com',
	description ='This is preprocessing package',
	long_description = long_description,
	long_description_content_type ='text/markdown',
	packages = setuptools.find_packages(),
	clssifiers = [
	'Programming Language :: Python :: 3',
	'License :: OSI Aproved :: MIT License',
	'Operating System :: OS Independent'],
	python_requires = '>=3.5'
	)	