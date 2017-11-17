from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "VERSION"), encoding="utf-8") as f:
    VERSION = f.read().strip()

setup(author="Andrew Michaud",
      author_email="bots+tree@mail.andrewmichaud.com",

      entry_points={
          "console_scripts": ["tree_bot = tree_bot.__main__:main"]
      },

      install_requires=["botskeleton>=1.2.2", "treegen"],

      license="BSD3",

      name="tree_bot",

      packages=find_packages(),
      python_requires=">=3.6",

      # Project"s main homepage
      url="https://github.com/andrewmichaud/tree_bot",

      version=VERSION)
