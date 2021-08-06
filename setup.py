from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_desc = fh.read()

setup(
    name='sshepherd',
    version="0.1",
    packages=["sshepherd"],
    package_dir={'': "src"},
    scripts=['scripts/sshepherd'],
    author="George",
    author_email="drpresq@gmail.com",
    description="SSHepherd: Automated SSH User Management",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/drpresq/sshepherd",
    keywords="",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Utilities'
    ],
)
