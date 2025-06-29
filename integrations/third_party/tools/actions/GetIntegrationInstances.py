# Copyright 2025 Google LLC
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

from __future__ import annotations

from soar_sdk.SiemplifyAction import SiemplifyAction
from soar_sdk.SiemplifyUtils import output_handler

GET_INTEGRATIONS = "{}/external/v1/integrations/GetEnvironmentInstalledIntegrations"


@output_handler
def main():
    siemplify = SiemplifyAction()
    siemplify.script_name = "GetIntegrationInstances"

    env_search = [siemplify._environment, "*"]
    json_payload = {"name": "*"}
    instances = []
    for env in env_search:
        json_payload = {"name": env}
        siemplify_integrations = siemplify.session.post(
            GET_INTEGRATIONS.format(siemplify.API_ROOT),
            json=json_payload,
        )
        siemplify_integrations.raise_for_status()
        instances.extend(siemplify_integrations.json()["instances"])

    siemplify.result.add_result_json({"instances": instances})
    output_message = "Returned Instances."
    siemplify.end(output_message, True)


if __name__ == "__main__":
    main()
