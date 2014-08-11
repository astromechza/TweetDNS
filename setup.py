from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='tweet_dns',
    version='0.1',
    author='Ben Meier',
    author_email='benmeier42@gmail.com',
    license='MIT',
    description='A simple, don\'t-trust-the-man, DNS system running from a Twitter account! Powered by Python.',
    long_description=read('README.md'),
    packages=find_packages(exclude=['tests']),
    scripts=[
        'scripts/tweet_dns_config',
        'scripts/tweet_dns_update'
    ],
    install_requires=[
        'Click',
        'Twitter'
    ],
    test_suite='nose.collector',
    tests_require='nose',
)
