# flake8: noqa
"""
Copyright 2020 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from okta.okta_enum import OktaEnum


class UserStatus(
    str,
    OktaEnum
):
    """
    An enumeration class for UserStatus.
    """

    ACTIVE = "ACTIVE"
    DEPROVISIONED = "DEPROVISIONED"
    LOCKED_OUT = "LOCKED_OUT"
    PASSWORD_EXPIRED = "PASSWORD_EXPIRED"
    PROVISIONED = "PROVISIONED"
    RECOVERY = "RECOVERY"
    STAGED = "STAGED"
    SUSPENDED = "SUSPENDED"
