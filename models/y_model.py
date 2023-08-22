import typing

from common.config import BaseConfig, Config
from model import model


@model(config=Config)
def model_y(*, config: BaseConfig, data: typing.Any):
    return config.a*data/config.b




