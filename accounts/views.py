from django.shortcuts import redirect, render
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()


def login_excluded(redirect_to):
    """ This decorator kicks authenticated users out of a view """
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to)
            return view_method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper


@login_excluded('studentdata:students')
def login_view(request):
    form = LoginForm(None)
    error_msg = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            print(f'\n\nGET:\n\n{user}\n\n')

            if user != None:
                login(request, user)
                return redirect('studentdata:home')
            else:
                form.add_error(field='password',
                               error='Invalid Username or Password')
                request.session['invalid_user'] = 1  # 1==True
                attempt = request.session.get('attempt') or 0
                request.session['attempt'] = attempt + 1
                values = form.errors
                print(f'\n\nGET:\n\n{ values }\n\n')
    context = {
        'title': 'Login',
        'form': form,
    }
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('accounts:login')
