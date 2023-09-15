import sys
import importlib
import inspect

sys.path.append('/Users/mciurej/Workspace/hp_tuner/common')
sys.path.append('/Users/mciurej/Workspace/hp_tuner/models')
sys.path.append('/Users/mciurej/Workspace/hp_tuner/tunner')
import models
from models import *

from common.config import Config
from tunner.tunner import Tuner

if __name__ == "__main__":
    t = Tuner()
    c = Config()

    #example iterable input data
    data = [5]
    result = None

    #find all the models and run tunner for each
    for mod_name in models.__all__:
        mod = importlib.import_module(mod_name)

        for name, obj in inspect.getmembers(mod):
            if callable(obj) and hasattr(obj, '__wrapped__'):
                for fit_function in ['min','max']:
                    print("- model: {}".format(name))
                    print("  results:")
                    print("  -fit: {}".format(fit_function))
                    print("   hyperparameters:")
                    result = t.tune(model=obj, config_factory={'config': c, 'data':data}, fit_function=eval(fit_function))
                    for i in result:
                        print("   -a: {}".format(i['a']))
                        print("    b: {}".format(i['b']))