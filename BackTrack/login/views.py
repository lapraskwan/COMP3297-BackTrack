from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import user, currentUser
from .forms import login_form

# Create your views here.


def login(request):
    incorrectPW = False
    incorrectUsername = False

    # Create form
    form = login_form(request.POST or None)

    if request.method == "POST": # If form has been submitted
        # Validate login information
        if form.is_valid():
            # Get the input username and input password
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            if user.objects.filter(username=username).exists():
                loginUser = user.objects.filter(username=username)[0]
                if loginUser.password == password:
                    # Clear data of the previous user
                    currentUser.objects.all().delete()
                    # Add the input user into currentUser
                    currentUser.objects.create(username=username, password=password, userType=loginUser.userType)
                    return redirect("../PBI")
                else:
                    incorrectPW = True
            else:
                incorrectUsername = True

    context = {
        "form": form,
        "incorrectPW": incorrectPW,
        "incorrectUsername": incorrectUsername
    }
    return render(request, "login_base.html", context)
