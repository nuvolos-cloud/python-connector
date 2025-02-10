from setuptools import setup, find_packages


def readme():
    with open("README.rst") as f:
        return f.read()


exec(open("nuvolos/version.py").read())
setup(
    name="nuvolos",
    version=__version__,
    description="The Nuvolos python library for database connectivity",
    long_description=readme(),
    url="https://github.com/nuvolos-cloud/python-connector",
    author="Alphacruncher",
    author_email="support@nuvolos.cloud",
    license="MIT",
    packages=find_packages(exclude=("tests", "venv")),
    include_package_data=True,
    install_requires=[
        "pyarrow>=10.0.1",
        "keyring>=24.1.0",
        "pandas<3.0.0",
        "snowflake-connector-python>=3.13.2",
        "snowflake-sqlalchemy>=1.7.3",
        "cryptography>=44.0.0"
    ],
    zip_safe=False,
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
