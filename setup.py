import setuptools

with open("README.md","r",encoding = "utf-8") as f:
    long_description = f.read()
    
    
__version__ = "0.0.0"

REPO_NAME = "MLOps-CNNClassifier"
AUTHOR_USER_NAME = "tysonbarretto"
SRC_REPO = "MLOps-CNNClassifier"
AUTHOR_EMAIL = "tysonbarrett01991@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls ={
        "Bugs Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
