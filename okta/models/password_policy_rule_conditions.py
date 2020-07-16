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
from okta.models.policy_network_condition\
    import PolicyNetworkCondition
from okta.models.policy_people_condition\
    import PolicyPeopleCondition


class PasswordPolicyRuleConditions(
    OktaObject
):
    """
    A class for PasswordPolicyRuleConditions objects.
    """

    def __init__(self, config=None):
        if config:
            if "network" in config:
                if isinstance(config["network"],
                              PolicyNetworkCondition):
                    self.network = config["network"]
                else:
                    self.network = PolicyNetworkCondition(
                        config["network"]
                    )
            else:
                self.network = None
            if "people" in config:
                if isinstance(config["people"],
                              PolicyPeopleCondition):
                    self.people = config["people"]
                else:
                    self.people = PolicyPeopleCondition(
                        config["people"]
                    )
            else:
                self.people = None
        else:
            self.network = None
            self.people = None
