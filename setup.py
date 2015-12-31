# Ran 'python setup.py sdist' and you will find the pv-aws library as tarball in sdist/, you can use it for distribution. Simply run 'sudo pip install manatee-0.1.tar.gz' to install.
# OR
# If you just want to install it locally, simply run "sudo python setup.py install".

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='randomname',
      version='0.1.0',
      description='Random Name Generator',
      author='Gerad Coles',
      author_email='geradacoles@gmail.com',
      packages=['randomname'],
      scripts=["bin/random-name"],
      install_requires = [
            'docopt>=0.6',
            ],
      )
