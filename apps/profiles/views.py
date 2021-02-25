from django.shortcuts import render


def my_profile(request):
    return render(request, "profiles/my_profile.html")
