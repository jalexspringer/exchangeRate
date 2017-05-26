from setuptools import setup

setup(name='pyopenex',
      version='0.1.2',
      description='API wrapper for the openexchangerates.org currency exchange rate API and ipinfo.io IP information API.',
      url='https://github.com/jalexspringer/pyopenex',
      author='Alex Springer',
      author_email='jalexspringer@gmail.com',
      license='MIT',
      packages=['pyopenex'],
      install_requires=[
          'requests'
      ],
      zip_safe=False)
