# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from platformio import exception, util
from platformio.managers.platform import PlatformBase


class Linux_arm_odroidPlatform(PlatformBase):

    @property
    def packages(self):
        packages = PlatformBase.packages.fget(self)
        if ("linux_arm" in util.get_systype() and
                "toolchain-gccarmlinuxgnueabi" in packages):
            del packages['toolchain-gccarmlinuxgnueabi']
        return packages

    def configure_default_packages(self, variables, targets):
        if (variables.get("pioframework") == "wiringpi-odroid" and
                "linux_arm" not in util.get_systype()):
            raise exception.PlatformioException(
                "PlatformIO does not support temporary cross-compilation "
                "for WiringPi framework. Please run PlatformIO directly on "
                "Raspberry Pi"
            )

        return PlatformBase.configure_default_packages(
            self, variables, targets)
