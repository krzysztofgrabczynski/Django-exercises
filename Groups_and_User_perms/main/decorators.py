from django.shortcuts import redirect


def if_logged(func):
    def func_wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return func(request, *args, **kwargs)

    return func_wrapper