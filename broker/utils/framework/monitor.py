
# Copyright (c) 2017 UFCG-LSD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import requests


def _get_monitor_data(plugin, info_plugin, collect_period):
    start_monitor_dict = {
        'plugin': plugin,
        'info_plugin': info_plugin,
        'collect_period': collect_period
    }
    start_monitor_body = json.dumps(start_monitor_dict)

    return start_monitor_body


def start_monitor(monitor_url, app_id, plugin, info_plugin, collect_period):
    request_url = monitor_url + '/monitoring/' + app_id
    headers = {'Content-type': 'application/json'}
    data = _get_monitor_data(plugin, info_plugin, collect_period)
    requests.post(request_url, data=data, headers=headers)


def stop_monitor(monitor_url, app_id):
    request_url = monitor_url + '/monitoring/' + app_id + "/stop"
    headers = {'Content-type': 'application/json'}
    requests.post(request_url, headers=headers)
