import typing
from common.config import BaseConfig
from runner.runner import Runner


class Tuner(Runner):

    def tune(self, model: typing.Callable, config_factory: typing.Any, fit_function: typing.Callable) -> [(BaseConfig, typing.Callable)]:
        raise Exception("Not Implemented")
