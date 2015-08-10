from email.mime.multipart import MIMEMultipart
import urlparse
from django.conf import settings

from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse
from django.forms.utils import ErrorList
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages

from login.forms import *

from login.models import *

from settings import REDIRECT_FIELD_NAME, INDEX_URL, ALTERNATE_INDEX_URL



# Login.
def log_in(request, template_name='login/login.html', default_redirect=INDEX_URL, alternate_redirect=ALTERNATE_INDEX_URL,
           current_app=None, extra_context=None):
    redirect_to = request.REQUEST.get(REDIRECT_FIELD_NAME, '')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            try:
                user = User.objects.get(username=username, is_active=True)
                user_type = UserExtended.objects.get(user=user).user_type

                if user is not None and user.is_active:
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(request, user)

                    # Check redirection
                    netloc = urlparse.urlparse(redirect_to)[1]
                    if (not redirect_to) or (netloc and netloc != request.get_host()):
                        if user_type.user_type == 'Doctor':
                            redirect_to = alternate_redirect
                        else:
                            redirect_to = default_redirect
                    return HttpResponseRedirect(redirect_to)
            except:
                form._errors.setdefault('username', ErrorList())
    else:
        form = LoginForm()

    return render_to_response(
        'login/login.html',
        {'form': form, REDIRECT_FIELD_NAME: redirect_to}
    )

# Logout.
def log_out(request):
    logout(request)
    return render_to_response(
        'login/logout_done.html',
        {'log_in': '/login/'}
    )


# Sign up.
def signup(request):

    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            obj = User()
            obj.username = form.cleaned_data['username']
            obj.email = form.cleaned_data['email']
            obj.first_name = form.cleaned_data['first_name']
            obj.last_name = form.cleaned_data['last_name']
            obj.password = form.cleaned_data['password']
            obj.password2 = form.cleaned_data['password2']
            obj.is_active = False
            obj.save()

            type_obj = UserExtended()
            type_obj.user = obj
            type_obj.user_type = form.cleaned_data['user_type']
            type_obj.save()
            if str(form.cleaned_data['user_type']) == 'Patient':
                send_email(obj.first_name, obj.email, obj.id)
            return render_to_response('login/logout_done.html',  {'log_in': '/login/'})

    context = {
        'active_tab':'home',
        'form':form,
        }
    return render_to_response('login/signup.html', context, context_instance=RequestContext(request))

def socialAuth(request):
   context = RequestContext(request, {'request': request, 'user': request.user})
   return render_to_response('login/socialAuth.html', context_instance=context)

def welcome_page(request):
   context = RequestContext(request, {'request': request})
   return render_to_response('login/welcome_page.html', context_instance=context)

def user_approval(request,id):
    try:
        obj = User.objects.get(id=id)
        obj.is_active = True
        obj.save()
        return render_to_response('login/logout_done.html',  {'log_in': '/login/'})
    except User.DoesNotExist:
        pass

#Send Email
def send_email(name, email_to, id):

    html = """\
        <html>
        <head></head>
        <body>
        <p> """
    html = html

    try:
        user_name = settings.ORGANISER_EMAIL
        password = settings.ORGANISER_PASS
        approval_link = settings.APPROVAL_LINK+str(id)
        from email.mime.text import MIMEText

        msg = MIMEMultipart()
        msg['Subject'] = "TalkDoc"
        msg['From'] = user_name
        msg['To'] = email_to

        html += """Hi """ +name+""",<br><br>You have been registered to TalkDoc.<br>"""
        html += """For approval <a href="""+approval_link+""">Click Here</a>.<br><br>Thanks,<br>TalkDoc Team</body></html>"""

        msg.attach(MIMEText(html, 'html'))
        import smtplib

        session = smtplib.SMTP('smtp.live.com', 587)
        session.ehlo()
        session.starttls()
        session.login(user_name, password)
        session.sendmail(user_name, email_to, msg.as_string())
        session.quit()
        return True
    except:
        return False
