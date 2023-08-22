# Hyperparameter Tuner

You will work towards implementation of simple **Hyperparameter Tuning Framework** and this is your high level goal.
Your need to produce optimal `common.BaseConfig` object for each model in `models` package.
To decide if the combination of parameters is optimal please use `min` and `max` as fitness function

### Framework needs to:
- identify all available models
- determine optimal parameters using each fit function ( `min`, `max` )
- return tuning results ( example below )


#### context:
- It is expected to preserve API of models which can be run using `runner.Runner`
- Config` object and model functions are externally provided
- Number of models to tune can vary in time
- for purpose of this exercise Model argument `data` should be considered as `Iterable` provided to `runner.Runner`.
- Framework is expected to produce list of optimal sets of parameters for each registered model according
  to its configuration for each of the fit function ( `min` and `max` in this case ).
  If more than one set of hyperparameters have optimal result of fit function, all of them should be returned.
  Result can look like:
```
    - model: x
      results:
      - fit: min
        hyperparameters:
        - a: XXX
          b: YYY
        - a: XXX'
          b: YYY'
      - fit: max
        hyperparameters:
          a: WWW
          b: ZZZ
    - model: y
        results:
      - fit: min
        hyperparameters:
          a: CCC
          b: DDD
      - fit: max
        hyperparameters:
        - a: AAA
          b: BBB
        - a: AAA'
          b: BBB'
```

#### **constrain**: 
No modification in `common`, `models` and `runner` should be done in final implementation
