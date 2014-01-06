from setuptools import setup #, find_packages

try:
    with open('README.md') as file:
        long_description = file.read()
except:
    long_description = "Apple Newsstand Atom feed generator"

setup(name='atomgen',
      version='0.1.9',
      description='Creates Apple Newsstand Atom Feed',
      url='https://github.com/erasmose/atomgen',
      download_url='https://github.com/erasmose/atomgen/tarball/master',
      author='Erasmose',
      author_email='sep@zepworks.com',
      license='MIT',
      packages=['atomgen'],
      zip_safe=False,
      long_description=long_description,
      classifiers=[
        'Environment :: Web Environment',
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        ],
      )