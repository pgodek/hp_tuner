import common.config as cfg
import functools

def model(**kwargs):

    config = kwargs['config']
    def out_wrapper(fun):
        @functools.wraps(fun)
        def in_wrapper(**kwargs):
            data = kwargs['data']
            results = list()
            for x in config.a:
                for y in config.b:
                        c = cfg.Config()
                        c.a = x
                        c.b = y
                        results.append({"value":fun(config=c, data=data), "a": c.a, "b": c.b})

            return results
        return in_wrapper
    return out_wrapper