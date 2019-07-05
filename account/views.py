from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.checks import messages
from django.core.mail.message import EmailMessage
from django.http.response import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import SignupForm
from .tokens import account_activation_token
from django.core.mail import send_mail
import logging



logger = logging.getLogger(__name__)


def logins(request):
    logger.error('this is log error')
    logger.debug('this is log debug')
    logger.info('this is log info')
    logger.critical('this is log critical')
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username=name,password=password)
        print(user)
        if user is None:
            return HttpResponse('logged in fail')
        else:
            login(request, user)
            return HttpResponse('you are loggin :)')


    return render(request, "login.html")


def signup(request):
    logger.error('this is log error')
    logger.debug('this is log debug')
    logger.info('this is log info')
    logger.critical('this is log critical')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'register.html', {'msg': 'Please confirm your email address to complete the registration' })

    else:
        form = SignupForm()
    return render(request, 'register.html', {'form': form})


def activate(request, uidb64, token):
    logger.error('this is log error')
    logger.debug('this is log debug')
    logger.info('this is log info')
    logger.critical('this is log critical')
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        # return render(request, 'slackapp/member.html')
        return redirect('/info')

    else:
        return HttpResponse('Activation link is invalid!')



