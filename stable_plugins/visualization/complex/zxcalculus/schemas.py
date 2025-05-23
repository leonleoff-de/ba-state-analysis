# Copyright 2023 QHAna plugin runner contributors.
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

from qhana_plugin_runner.api.util import (
    FileUrl,
    FrontendFormBaseSchema,
)
import marshmallow as ma


class ZXCalculusInputParametersSchema(FrontendFormBaseSchema):
    data = FileUrl(
        required=True,
        allow_none=False,
        data_input_type="executable/circuit",
        data_content_types=["text/x-qasm"],
        metadata={
            "label": "Qasm Circuit URL",
            "description": "URL to a QASM Circuit.",
        },
    )
    optimized = ma.fields.Boolean(
        required=False,
        allow_none=False,
        metadata={
            "label": "Optimize",
            "description": "Optimize Circuit as much as possible, by applying ZX-Calculus axioms."
            + " Will generate an additional image below the original one.",
        },
    )
