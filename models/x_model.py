import typing

from common.config import Config
from model import model


@model(config=Config)
def model_x(*, config: Config, data: typing.Any):
    return config.a+data-config.b
