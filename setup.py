from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="foo",
    version="1.1.5",
    description="Foo package",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/RobertoPrevato/workflows",
    author="Roberto Prevato",
    author_email="roberto.prevato@gmail.com",
    keywords="foo",
    license="MIT",
    packages=["foo"],
    install_requires=[],
    include_package_data=True,
)
