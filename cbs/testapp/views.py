from django.views.generic import View,TemplateView
from django.http import HttpResponse

# Create your views here.

class HelloWorld(View):
    def get(self,request):
        return HttpResponse('<h1>This is from class based view</h1>')

class HelloWorldTem(TemplateView):
    template_name='testapp/result.html'
