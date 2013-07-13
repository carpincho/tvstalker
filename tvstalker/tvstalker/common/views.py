# -*- coding: utf-8 -*-

from utils import render_response
from django.http import HttpResponse
from django.utils import simplejson
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


@login_required
def home(request):
    """Home Page."""
    return render_response(request, 'index.html')


def about(request):
    """About Page."""
    return render_response(request, 'about.html')


def report(request):
    """Report Page."""
    return render_response(request, 'report.html')


@login_required
def profile(request):
    """Profile Page."""
    return render_response(request, 'profile.html')


def sign_up(request):
    """Sign Up Page."""
    return render_response(request, 'sign-up.html')


@require_POST
def rpc(request):
    print('\n\ndiegoooooooooooooooo\n\n')
    some_data = {
       'some_var_1': 'foo',
       'some_var_2': 'bar',
    }
    data = simplejson.dumps(some_data)

    return HttpResponse(data, mimetype='application/json')