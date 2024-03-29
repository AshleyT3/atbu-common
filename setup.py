# Copyright 2022 Ashley R. Thomas
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pathlib import Path
import setuptools

# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="atbu-common-pkg",
    version="0.0.11",
    author="Ashley R. Thomas",
    author_email="ashley.r.thomas.701@gmail.com",
    description= (
        "ATBU common package, common modules used by atbu.backup and atbu.mp_pipeline."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AshleyT3/atbu-common",
    project_urls={
        "Bug Tracker": "https://github.com/AshleyT3/atbu-common/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_namespace_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[
        "cryptography >= 36.0.2",
    ]
)
