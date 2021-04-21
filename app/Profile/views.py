from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.html import strip_tags
from .tokens import account_activation_token
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from main.settings import EMAIL_HOST_USER
from Blog.models import ArticlesModel


def profile_view(request, username):
    return HttpResponse("<h1>Profile</h1>")


@login_required
def my_profile_view(request):
    user = request.user
    articles = ArticlesModel.objects.all().filter(author__exact=user)
    for article in articles:
        article.text = " ".join(strip_tags(article.text).split(" ")[:40]) + "..."

    context = {"user": user, "articles": articles}

    return render(request, "profile.html", context)


def logout_view(request):
    logout(request)
    return redirect("/profile/login")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            remember_me = form.cleaned_data["remember_me"]
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                if not remember_me:
                    request.session.set_expiry(0)
                return redirect("/profile/")
    else:
        form = LoginForm()

    context = {
        "form": form,
    }

    return render(request, "authentication/login.html", context)


def registration_view(request):
    if request.user.is_authenticated:

        return redirect("/profile/")

    if request.method == "POST":

        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            user = registration_form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = "Activate your account."
            message = render_to_string(
                "authentication/email_reg_temp.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user),
                },
            )
            to_email = registration_form.cleaned_data.get("email")
            send_mail(mail_subject, message, EMAIL_HOST_USER, [to_email])
            return render(request, "authentication/check_email_template.html", {})

    else:
        registration_form = RegistrationForm()

    context = {
        "form": registration_form,
    }

    return render(request, "authentication/reg.html", context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("/profile/")
    else:
        return HttpResponse("Activation link is invalid!")
