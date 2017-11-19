# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Question, DangerAlert
from django.db.models import Q
from django.contrib import messages

import urllib
import urllib2
from bs4 import BeautifulSoup


def home(request):
    return render(request, 'askApp/index.html')


def ajax_user_search(request):
    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None and q != '':
            results = Question.objects.filter(
                Q(answer__contains=q)
                )

            template = 'askApp/results.html'
            data = {
                'results': results,
            }
            if results.__len__() == 0:
                article = q
                article = urllib.quote(article)

                opener = urllib2.build_opener()
                opener.addheaders = [('User-agent', 'Mozilla/5.0')]

                resource = opener.open("http://en.wikipedia.org/wiki/" + article)
                data = resource.read()
                resource.close()
                soup = BeautifulSoup(data)
                soup = soup.find('div', id="bodyContent").p
                return render(request, template, {'soup': soup})
            return render(request, template, data)
        else:
            return render(request, 'askApp/results.html')


def danger_alert(request, address):
    DangerAlert.objects.update_or_create(
        alert_address=address
    )
    messages.success(request, 'Be Calm, A Rescue Team Would be with You')
    return render(request, 'askApp/index.html')