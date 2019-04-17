# Copyright (c) 2017 UPV-GryCAP & UFCG-LSD.
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

import threading
import uuid

from broker.plugins import base
from broker.plugins.base import GenericApplicationExecutor
from broker.utils.ids import ID_Generator
from broker.utils.logger import Log
from broker.utils.plugins import k8s

KUBERNETESSTREAM_LOG = Log("KubernetesStreamPlugin", "logs/kubernetes_stream.log")
application_time_log = Log("Application_time", "logs/application_time.log")

class KubernetesStreamExecutor(GenericApplicationExecutor):
    def __init__(self, app_id):
        self.id = ID_Generator().get_ID()
        self.app_id = app_id
        self.terminated = False
        self.status = "created"
    
    def start_application(self, data):
        # If the cluster name is informed in data, active the cluster
        if('cluster_name' in data.keys()):
            v10.activate_cluster(data['cluster_name'], data)

        redis_ip, redis_port = k8s.provision_redis_or_die(self.app_id)
        data['env_vars']['REDIS_HOST'] = 'redis-%s' % self.app_id
        KUBERNETESSTREAM_LOG.log("Created redis, deploying")
        k8s.create_deployment(
            self.app_id,
            data['cmd'],
            data['img'],
            data['init_size'],
            data['env_vars'],
            config_id=data["config_id"])

class KubernetesStreamProvider(base.PluginInterface):
    def __init__(self):
        self.id_generator = ID_Generator()

    def get_title(self):
        return 'Kubernetes Stream Processing Plugin'

    def get_description(self):
        return ('Plugin that allows utilization of '
                'stream processing over a k8s cluster')

    def to_dict(self):
        return {
            'name': self.name,
            'title': self.get_title(),
            'description': self.get_description(),
        }

    def execute(self, data):
        app_id = 'kj-' + str(uuid.uuid4())[0:7]
        executor = KubernetesStreamExecutor(app_id)

        handling_thread = threading.Thread(target=executor.start_application,
                                           args=(data,))
        handling_thread.start()
        return app_id, executor
