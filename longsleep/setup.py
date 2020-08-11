# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Cloud Profiler Python agent packaging script."""

import glob
from setuptools import Extension
from setuptools import setup


ext_module = [
    Extension(
        'longsleep.longsleep',
        sources=glob.glob('longsleep/src/*.cc'),
        include_dirs=['longsleep/src/'],
        language='c++',
        extra_compile_args=['-std=c++11'],
        extra_link_args=[
            '-std=c++11',
            '-static-libstdc++',
        ])
]

setup(
    name='longsleep',
    version='1.0.0',
    setup_requires=['wheel'],
    packages=['longsleep'],
    ext_modules=ext_module,
    license='Apache License, Version 2.0',
    )
