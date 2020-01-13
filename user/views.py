from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}! Now You can Login")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


class LoginView(auth_views.LoginView):
    template_name = "login.html"


class LogoutView(auth_views.LogoutView):
    template_name = "logout.html"


@login_required
def Profile(request):
    if request.method == 'POST':
        u_forms = UserUpdateForm(request.POST, instance=request.user)
        p_forms = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_forms.is_valid() and p_forms.is_valid():
            u_forms.save()
            p_forms.save()
            messages.success(request, f"Account is updated")
            return redirect('profile')
    else:
        u_forms = UserUpdateForm(instance=request.user)
        p_forms = ProfileUpdateForm()
    context = {
            'u_forms': u_forms,
            'p_forms': p_forms
    }
    return render(request, "profile.html", context)
