import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dbutils",
    version="0.0.2",
    author="Ismael Raya",
    author_email="phornee@gmail.com",
    description="DB management wrapper over mariaDB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Phornee/dbutils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'mariadb>=1.0.5'
    ],
    python_requires='>=3.6',
)