#!/usr/bin/env python2

from brainsquared.analytics.preprocessing_module import PreprocessingModule


_RMQ_ADDRESS = "rabbitmq.cloudbrain.rocks"
_RMQ_USER = "cloudbrain"
_RMQ_PWD = "cloudbrain"
_WEBSERVER_PORT = 8080
_API_VERSION = "v0.1"

user_id = 'brainsquared'
module_id = 'module1'
device_type = 'openbci'

preproc_module = PreprocessingModule(user_id,
                                     module_id,
                                     device_type,
                                     _RMQ_ADDRESS,
                                     _RMQ_USER,
                                     _RMQ_PWD)

preproc_module.initialize()
preproc_module.start()

