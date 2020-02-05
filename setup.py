from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='jellyfin-apiclient-python',
    version='1.4.0',
    author="Ian Walton",
    author_email="iwalton3@gmail.com",
    description="Python API client for Jellyfin",
    license='GPLv3',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/iwalton3/jellyfin-apiclient-python",
    packages=['jellyfin_apiclient_python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['requests', 'urllib3', 'websocket_client']
)
