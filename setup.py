from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = "SURYAA NT"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ["pandas","numpy","scikit-learn","ipykernel","nltk","streamlit"]

setup (
    name = SRC_REPO,
    version = "0.0.1",
    author = AUTHOR_NAME,
    author_email = "ntsuryaa17@gmail.com",
    description = "Movie Recommendation System",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    package = [SRC_REPO],
    python_requires = ">=3.8",
    install_requires = [LIST_OF_REQUIREMENTS]
)