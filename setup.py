from setuptools import setup

setup(name='package',
      version='0.1',
      packages=['package'],
      package_data={'package': ['moduledata.txt']},
      entry_points={
          'console_scripts': [
              'mycommand = package.module:main',
          ]
      },
    setup_requires=['pytest'],
    tests_require=['pytest'],      
)
