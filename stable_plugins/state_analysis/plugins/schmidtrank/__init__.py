# Copyright 2022 QHAna plugin runner contributors.
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

from typing import Optional

from flask import Flask
from qhana_plugin_runner.api.util import SecurityBlueprint
from qhana_plugin_runner.util.plugins import QHAnaPluginBase, plugin_identifier

_plugin_name = "schmidt_rank_classical"
__version__ = "v0.0.1"
__description__ = "Computes the Schmidt rank of a given bipartite quantum state vector, which quantifies the amount of entanglement in the system."
__template_folder__ = "classical_state_templates"
__tags__ = ["classical-state-analysis", "schmidt-rank", "qasm"]


_identifier = plugin_identifier(_plugin_name, __version__)

BLP = SecurityBlueprint(
    _identifier,
    __name__,
    description=__description__,
    template_folder=__template_folder__,
)


class Plugin(QHAnaPluginBase):
    name = _plugin_name
    version = __version__
    description = __description__
    tags = __tags__

    def __init__(self, app: Optional[Flask]) -> None:
        super().__init__(app)

    def get_api_blueprint(self):
        return BLP


try:
    from . import routes
except ImportError:
    pass
