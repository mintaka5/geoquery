from setuptools import setup, find_packages

reqs = []

setup(
    name="geoquery",
    author="Chris Walsh",
    author_email="chris.is.rad@pm.me",
    description="a geo querier",
    license="MIT",
    version="0.0.1",
    packages=find_packages(),
    install_rquires=reqs,
    entry_points={
        'console_scripts': [
            'gregory = geoquery.main:boot_up'
        ]
    },
    python_requires='>=3.12',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent'
    ]
)