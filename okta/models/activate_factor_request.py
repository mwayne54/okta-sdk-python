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


class ActivateFactorRequest(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.attestation = config["attestation"]\
                if "attestation" in config else None
            self.client_data = config["clientData"]\
                if "clientData" in config else None
            self.pass_code = config["passCode"]\
                if "passCode" in config else None
            self.registration_data = config["registrationData"]\
                if "registrationData" in config else None
            self.state_token = config["stateToken"]\
                if "stateToken" in config else None
        else:
            self.attestation = None
            self.client_data = None
            self.pass_code = None
            self.registration_data = None
            self.state_token = None

# End of File Generation
