from django.shortcuts import render, get_list_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

import requests
import json


from .models import RequestForsto
from .forms import RequestForstoForm


def index(request):
    """Home page application reqs"""
    return render(request, 'reqs/index.html')


def about(request):
    """About page application reqs"""
    return render(request, 'reqs/about.html')


@login_required
def res_req(request):
    """Page with result request"""
    req_s = RequestForsto.objects.last()
    context = {'req_last': req_s}
    return render(request, 'reqs/res_req.html', context)


@login_required
def work_page(request):
    """Blank page for input data about client"""
    if request.method != 'POST':
        form = RequestForstoForm()
    else:
        form = RequestForstoForm(request.POST)
        args_forsto = {}
        if form.is_valid():
            new_request_forsto = form.save(commit=False)
            new_request_forsto.owner = request.user
            url_req = "https://forsto.ru/ajax/offer/"
            args_forsto['ACTION'] = 'ajaxPostExternalOrder'
            args_forsto['_TOKEN'] = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
            args_forsto['VIN'] = new_request_forsto.vin
            args_forsto['CAR_MODEL'] = new_request_forsto.car_model
            args_forsto['DESCRIPTION'] = new_request_forsto.description
            args_forsto['CLIENT_NAME'] = new_request_forsto.client_name
            args_forsto['ORDER_ID'] = 0
            args_forsto['PHONE'] = new_request_forsto.phone

            r = requests.get(url_req, args_forsto)
            req_result = r.json()

            if req_result["code"] == 200:
                str_req = "Номер заявки - " + str(req_result["response"])
            else:
                str_req = "Ошибка размещения - " + str(req_result["response"])

            new_request_forsto.res_code = req_result["code"]
            new_request_forsto.res_response = str_req
            new_request_forsto.save()
            return HttpResponseRedirect(reverse('reqs:res_req'))

    context = {'form': form}
    return render(request, 'reqs/work_page.html', context)

