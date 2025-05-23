# Copyright 2025 QHAna plugin runner contributors.
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
# limitations under the Licens

from typing import Optional

from flask.app import Flask

from qhana_plugin_runner.api.util import SecurityBlueprint
from qhana_plugin_runner.util.plugins import QHAnaPluginBase, plugin_identifier

_plugin_name = "data-join"
__version__ = "v1.0.0"
_identifier = plugin_identifier(_plugin_name, __version__)


JOIN_BLP = SecurityBlueprint(
    _identifier,  # blueprint name
    __name__,  # module import name!
    description="Data Join plugin API.",
    template_folder="templates",
)


class DataJoin(QHAnaPluginBase):
    name = _plugin_name
    version = __version__
    description = "Join data from multiple entity files."
    tags = ["preprocessing", "join"]

    def __init__(self, app: Optional[Flask]) -> None:
        super().__init__(app)

    def get_api_blueprint(self):
        return JOIN_BLP


try:
    # It is important to import the routes **after** JOIN_BLP and DataJoin are
    # defined, because they are accessed as soon as the routes are imported.
    from . import routes  # noqa
except ImportError:
    # When running `poetry run flask install`, importing the routes will fail,
    # because the dependencies are not installed yet.
    pass
