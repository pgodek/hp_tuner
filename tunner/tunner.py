import typing
from common.config import BaseConfig, Config
from runner.runner import Runner


class Tuner(Runner):

    def tune(self, model: typing.Callable, config_factory: typing.Any, fit_function: typing.Callable) -> [(BaseConfig, typing.Callable)]:
        config = config_factory['config']
        data = config_factory['data']

        data_iterator = iter(data)
        results = list()

        while True:
            try:
                data_point = next(data_iterator)
                output_points = self.run(model=model, data=data_point, config=config)
                #executing fit_function twice: 1st for each of data point 2nd for best fit out of all data points
                outcome_value = fit_function(output_points, key= lambda d: d['value'])['value']
                results = results + [{'a': d['a'], 'b': d['b'], 'value': d['value']} for d in output_points if d['value'] == outcome_value]
            except StopIteration:
                break
        global_optimized_value = fit_function(results, key= lambda d: ['value'])['value']
        return [{'a': d['a'], 'b': d['b'], 'value': d['value']} for d in results if d['value'] == global_optimized_value]

    
    def run(self, model, data, config: Config) -> typing.Any:
        return model(config=config, data=data)