from setuptools import setup

setup(name='WOLbyWEB',
      version='0.1',
      description='Wake up Machines with an python WEB interface.',
      url='http://github.com/x4x/WOLbyWEB',
      author='x4x',
      author_email='georg.la8585@gmx.at',
      license='GPL2',
      packages=['WOLbyWEB'],
      install_requires=[
	      'bottle',
	      'wakeonlan',
	      'xmltodict',
      ],
      include_package_data=True,
      zip_safe=False)
