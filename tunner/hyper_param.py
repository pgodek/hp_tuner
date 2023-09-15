def hyper_param(**kwargs):

    min = kwargs['min']
    step = kwargs['step']
    max = kwargs['max']

    def out_wrapper(value):

        output_list = list()
        v = min

        while v <= max:
            output_list.append(v)
            v = v + step
        value = output_list
        
        return value
    return out_wrapper