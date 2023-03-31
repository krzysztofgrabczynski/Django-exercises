from django.shortcuts import redirect
from django.http import HttpResponse


def if_logged(func):
    def func_wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return func(request, *args, **kwargs)

    return func_wrapper

def allow_by_group(roles = []):
    def decorator(func):
        def func_wrapper(request, *args, **kwargs):
                try:
                    user_group = request.user.groups.first().name
                except:
                     user_group = None
                if user_group in roles:
                    return func(request, *args, **kwargs)
                
                return HttpResponse('You cannot access this page')
        
        return func_wrapper
    return decorator