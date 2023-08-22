from tunner.hyper_param import hyper_param


class BaseConfig:
    a: int
    b: int


class Config(BaseConfig):
    @property
    @hyper_param(min=10, max=100, step=2)
    def a(self) -> int:
        pass

    @property
    @hyper_param(min=-200000, max=1000000, step=7)
    def b(self) -> int:
        pass

