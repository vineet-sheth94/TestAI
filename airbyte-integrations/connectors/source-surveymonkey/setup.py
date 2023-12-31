#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


from setuptools import find_packages, setup

MAIN_REQUIREMENTS = ["airbyte-cdk", "vcrpy==4.1.1", "urllib3<2.0"]

TEST_REQUIREMENTS = ["requests-mock~=1.9.3", "pytest-mock~=3.6.1", "pytest~=6.1", "requests_mock"]

setup(
    name="source_surveymonkey",
    description="Source implementation for Surveymonkey.",
    author="Airbyte",
    author_email="contact@airbyte.io",
    packages=find_packages(),
    install_requires=MAIN_REQUIREMENTS,
    package_data={"": ["*.json", "schemas/*.json", "schemas/shared/*.json"]},
    extras_require={
        "tests": TEST_REQUIREMENTS,
    },
)
