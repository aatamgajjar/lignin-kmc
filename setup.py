from setuptools import setup

setup(name='ligninkmc',
	version='0.1',
	description="Kinetic Monte Carlo implementation for creating realistic lignin topologies.",
	url='https://github.com/michaelorella/lignin-kmc',
	author='Michael Orella and Terry Gani',
	license='MIT',
	packages=['ligninkmc'],
    package_dir={'ligninkmc': 'ligninkmc'},
	python_requires=">3.6", #Required for f-strings support.
	test_suite='tests',
	install_requires=['scipy', 'numpy', 'matplotlib', 'joblib', 'ipython'], #rdkit isn't installable via pip.
	zip_safe=False)