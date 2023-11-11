def validate_args(func):
    def wrapper(*args, **kwargs):
        if len(args) + len(kwargs) < 1:
            return 'Not enough arguments'
        if len(args) + len(kwargs) > 1:
            return 'Too many arguments'

        if args:
            num = args[0]
        else:
            num = kwargs[[*kwargs][0]]

        if int(num) != num:
            return 'Wrong types'
        if num < 0:
            return 'Negative argument'

        return func(*args, **kwargs)

    return wrapper
