from django.shortcuts import render,render_to_response

# Create your views here.
from blog.models import Artical,Author,Tag,Classification
from django.template import RequestContext
def blog_list(request):
	blogs=Artical.objects.all().order_by('-publishTime')
	return render_to_response('index.html',{"blogs":blogs},context_instance=RequestContext(request))