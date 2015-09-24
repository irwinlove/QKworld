from django.shortcuts import render,render_to_response

# Create your views here.
from blog.models import Artical,Author,Tag,Classification
from django.template import RequestContext
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
def blog_list(request):
	artical_list=Artical.objects.all().order_by('-publishTime')
	items=len(artical_list)
	itemsOnpage=5
	paginator=Paginator(artical_list, itemsOnpage)#show 5 artical per page
	page=request.GET.get('page') 
	try:
		artical_list=paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		artical_list=paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		artical_list=paginator.page(paginator.num_pages)
	# return render_to_response('blog/index.html',{"blogs":blogs},context_instance=RequestContext(request))
	return render(request,'blog/index.html',{"blogs":artical_list,"items":items,"itemsOnpage":itemsOnpage,})



def blog_detail(request,blog_id):
	try:
		blog=Artical.objects.get(id=blog_id)
	except Artical.DoesNotExist:
		pass
	return render(request,'blog/detail.html',{"blog":blog})
	
