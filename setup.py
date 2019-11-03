from setuptools import setup, find_packages
setup(
	name='file-classifier',
	version='0.1.0',
	keywords=['File Management', 'Classification'],
	packages=find_packages(),
	description='A simple classifier to manage your messy desktop files.',
	author='Tony Xiang',
	author_email='tonyxfy@qq.com',
	url='https://github.com/T0nyX1ang/Classifier',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Environment :: Console',
		'License :: OSI Approved :: MIT License',
		"Operating System :: OS Independent"
	],
	platforms='all',
	entry_points={
		'console_scripts': [
			'config=Classifier:config',
			'classify=Classifier:classify',
			'merge=Classifier:merge',
		]
	}
)