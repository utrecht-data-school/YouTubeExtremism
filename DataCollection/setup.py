from setuptools import setup, find_packages

with open("requirements.txt") as handle:
    project_requirements = [line.strip() for line in handle.readlines()]

test_requirements = ["pytest-runner", "pytest", "coverage"]

setup(name="youtubecollector",
      version="0.1.0",
      description="Module for getting data from youtube",
      url="https://github.com/CorrespondentData/YouTubeExtremism",
      author="De Correspondent",
      package_dir={'': 'youtubecollector'},
      packages=find_packages('youtubecollector'),
      install_requires=project_requirements,
      tests_require=test_requirements,
      extras_require={
          "dev": test_requirements
      },
      test_suite="tests",
      python_requires='>=3'
      )
