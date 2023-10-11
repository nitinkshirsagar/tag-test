"""pip install setup method to define what is required for this module."""
import codecs
import os
from setuptools import setup, find_namespace_packages


REQUIREMENTS = []
with open("requirements.txt", encoding="utf-8") as f:
    for line in f.readlines():
        # the install_requires with setup does not accept --trusted-host and --extra-index-url
        # so this check skips those lines and creates the requirements without those
        # when someone does a pip install if their pypi config is setup correctly it should still work.
        if not line.startswith("--"):
            REQUIREMENTS.append(line)


def load_readme(fname: str) -> str:
    """Read and decode a file's contents.

    Args:
        fname: the path of the file to open

    Returns:
        The contents of the file, decoded via utf-8
    """
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


setup(
    name="tag-test",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="tag test cases",
    long_description=load_readme("README.rst"),
    python_requires=">=3.7",
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    package_data={"": ["*.json"]},
    author="test",
    author_email="nitinkshirsagar@agiliad.com",
    license="BSD",
    include_package_data=True,
)
