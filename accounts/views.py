from django.shortcuts import redirect, render
from accounts.forms import LoginForm
from django.contrib.auth import authenticate, login


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                login(request, user)
                return redirect("list_projects")
    else:
        form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, "login.html", context)
