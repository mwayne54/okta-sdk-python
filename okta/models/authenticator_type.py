# flake8: noqa
"""
Copyright 2021 - Present Okta, Inc.

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

from aenum import MultiValueEnum


class AuthenticatorType(
    str,
    MultiValueEnum
):
    """
    An enumeration class for AuthenticatorType.
    """

    APP = "app", "APP"
    PASSWORD = "password", "PASSWORD"
    SECURITY_QUESTION = "security_question", "SECURITY_QUESTION"
    PHONE = "phone", "PHONE"
    EMAIL = "email", "EMAIL"
    SECURITY_KEY = "security_key", "SECURITY_KEY"
    FEDERATED = "federated", "FEDERATED"
