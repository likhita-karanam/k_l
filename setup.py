from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="TOPSIS-K.LIKHITA-101803143",
    version="1.0.1",
    description="A Python package to get weather reports for any location.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/likhita-karanam",
    author="K LIKHITA",
    author_email="karanamlikhita2000@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["folder_name"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "TOPSIS-K.LIKHITA-101803143=TOPSIS-K.LIKHITA-101803143.cli:main",
        ]
    },
)
