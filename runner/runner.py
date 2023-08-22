import abc
import typing
from common.config import BaseConfig, Config


class Runner(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run(self, model: typing.Callable,  config: Config) -> typing.Any:
        pass
