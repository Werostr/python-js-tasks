def foo(x, y, *args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)


foo(1, t=4, y=3, z=7)
