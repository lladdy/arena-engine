from django.http import HttpResponse
from django.views.generic import View


class TestView(View):

    def get(self, request):
        return HttpResponse("test view")