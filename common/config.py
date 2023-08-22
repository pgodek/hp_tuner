from hyper_param import hyper_param


class BaseConfig:
    a: int
    b: int


class Config(BaseConfig):
    @hyper_param(min=10, max=100, step=2)
    @property
    def a(self) -> int:
        pass

    @hyper_param(min=-200000, max=1000000, step=7)
    @property
    def b(self) -> int:
        pass
