from setuptools import setup, find_packages

setup(
    name="geoquery",
    author="Chris Walsh",
    author_email="chris.is.rad@pm.me",
    classifiers=[],
    description="a geo querier",
    license="MIT",
    version="0.0.1",
    url="",
    packages=find_packages(),
    install_rquires=[],
    entry_points={
        'console_scripts': [
            'gregory = geoquery.main:boot_up'
        ]
    }
)