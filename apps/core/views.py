from django.shortcuts import redirect, render


from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages

User = get_user_model()


class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")


def index(request):
    return render(request, "index.html")


def info(request):
    return render(request, "info.html")


def edit_user_details(request):
    user = request.user
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.save()
            messages.success(request, f"{user} saved succesfully!")
            return redirect("profile")

    form = UserForm(instance=user)
    return render(request, "account/edit_user.html", {"form": form})
