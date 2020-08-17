from setuptools import setup


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="nuvolos",
    version="0.3.22",
    description="The Nuvolos python library for database connectivity",
    long_description=readme(),
    url="https://github.com/nuvolos-cloud/python-connector",
    author="Alphacruncher",
    author_email="support@nuvolos.cloud",
    license="MIT",
    packages=["nuvolos"],
    install_requires=["pyodbc"],
    zip_safe=False,
)
