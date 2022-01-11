from setuptools import setup, find_packages

setup(
    name='test_ci_cd',
    version='0.1.0',
    license='proprietary',
    description='Test sample',

    author='Pablo Dalmasso',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=['requests'],

)
