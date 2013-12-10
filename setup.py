from setuptools import setup #, find_packages

with open('README.md') as file:
    long_description = file.read()

setup(name='atomgen',
      version='0.1.2',
      description='Creates Apple Newsstand Atom Feed',
      url='https://github.com/erasmose/atomgen',
      download_url='https://github.com/erasmose/atomgen/tarball/master',
      author='Erasmose',
      author_email='xpower3d@yahoo.com',
      license='MIT',
      packages=['atomgen'],
      zip_safe=False,
      long_description=long_description,
      classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
        ],
      )