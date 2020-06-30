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

from okta.okta_object import OktaObject


class PasswordPolicyRuleActions(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.password_change = config["passwordChange"]\
                if "passwordChange" in config else None
            self.self_service_password_reset = config["selfServicePasswordReset"]\
                if "selfServicePasswordReset" in config else None
            self.self_service_unlock = config["selfServiceUnlock"]\
                if "selfServiceUnlock" in config else None
        else:
            self.password_change = None
            self.self_service_password_reset = None
            self.self_service_unlock = None

# End of File Generation
