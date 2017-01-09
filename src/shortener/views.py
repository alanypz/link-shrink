from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
	return HttpResponse("Hello, {sc}".format(sc=shortcode))

class KirrCBView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		return HttpResponse("Hello again, {sc}.".format(sc=shortcode))