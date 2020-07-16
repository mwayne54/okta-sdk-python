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

from okta.models.policy\
    import Policy
from okta.models.policy_account_link\
    import PolicyAccountLink
from okta.models.provisioning\
    import Provisioning
from okta.models.policy_subject\
    import PolicySubject


class IdentityProviderPolicy(
    Policy
):
    """
    A class for IdentityProviderPolicy objects.
    """

    def __init__(self, config=None):
        if config:
            if "accountLink" in config:
                if isinstance(config["accountLink"],
                              PolicyAccountLink):
                    self.account_link = config["accountLink"]
                else:
                    self.account_link = PolicyAccountLink(
                        config["accountLink"]
                    )
            else:
                self.account_link = None
            self.max_clock_skew = config["maxClockSkew"]\
                if "maxClockSkew" in config else None
            if "provisioning" in config:
                if isinstance(config["provisioning"],
                              Provisioning):
                    self.provisioning = config["provisioning"]
                else:
                    self.provisioning = Provisioning(
                        config["provisioning"]
                    )
            else:
                self.provisioning = None
            if "subject" in config:
                if isinstance(config["subject"],
                              PolicySubject):
                    self.subject = config["subject"]
                else:
                    self.subject = PolicySubject(
                        config["subject"]
                    )
            else:
                self.subject = None
        else:
            self.account_link = None
            self.max_clock_skew = None
            self.provisioning = None
            self.subject = None
