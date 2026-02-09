def checking_var_db(fun):
    def wrapper(*args, **kwargs):
        if args[0].is_empty():
            print('Var is empty')
            return args[0].get_postgres_url_default
        return fun(*args, **kwargs)
    return wrapper