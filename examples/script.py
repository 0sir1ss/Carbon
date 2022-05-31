def func(arg1, arg2, arg3='arg3', *arg4, arg5, **kwargs):
    print('arg1', arg1)
    print('arg2', arg2)
    print('arg3', arg3)
    print('arg4', arg4)
    print('arg5', arg5)
    print('kwargs', kwargs)

var = "hi"
func('a', f'b: {var}', arg3='c', arg4='d', arg5='e')