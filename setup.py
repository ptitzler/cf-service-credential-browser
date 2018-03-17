from setuptools import setup, find_packages
setup(name='cfservicecredentialbrowser',
	  version='0.1',
	  description='IBM Cloud services credentials explorer',
	  url='https://github.com/ptitzler/cf-service-credential-browser',
	  install_requires=['pixiedust'],
	  author='Patrick Titzler',
	  author_email='ptitzler@us.ibm.com',
	  license='Apache 2.0',
	  packages=find_packages(),
	  include_package_data=False,
	  zip_safe=False
)
