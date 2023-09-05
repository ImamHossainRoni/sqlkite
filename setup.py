from setuptools import setup, find_packages

__author__ = 'Imam Hossain Roni'

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="sqlkite",
    version="0.1.0",
    description="A research and development initiative for crafting a Python based ORM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Imam Hossain Roni",
    author_email="imamhossainroni95@gmail.com",
    url="https://github.com/imamhossainroni/sqlkite",
    packages=find_packages(),
    install_requires=[

    ],
    entry_points={
        "console_scripts": [
            "sqlkite = sqlkite.__main__:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=[
        "sqlkite",
        "orm",
        "sql"

    ],
    project_urls={
        "Bug Tracker": "https://github.com/imamhossainroni/sqlkite/issues",
        "Source Code": "https://github.com/imamhossainroni/sqlkite",
        "Documentation": "https://github.com/imamhossainroni/sqlkite/blob/main/README.md",
        # "Icon Image": "https://raw.githubusercontent.com/ImamHossainRoni/sqlkite/main/extras/yellow-kite.png",
    },
)
