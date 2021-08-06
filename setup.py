from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_desc = fh.read()

setup(
    name='sshepard',
    version="0.1",
    packages=["sshepard"],
    package_dir={'': "src"},
    scripts=['scripts/sshepard'],
    author="George",
    author_email="drpresq@gmail.com",
    description="Onboard-Py: Automated SSH User Management",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/drpresq/onboard-py",
    keywords="",
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
)
