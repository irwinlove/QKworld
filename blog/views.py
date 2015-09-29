from django.shortcuts import render,render_to_response

# Create your views here.
from blog.models import Artical,Author,Tag,Classification
from django.template import RequestContext
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import Userform,UserProfileForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
def blog_list(request):
	artical_list=Artical.objects.all().order_by('-publishTime')
	paginator=Paginator(artical_list, 5)#show 5 artical per page
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
	return render(request,'blog/index.html',{"blogs":artical_list})



def blog_detail(request,blog_id):
	try:
		blog=Artical.objects.get(id=blog_id)
	except Artical.DoesNotExist:
		pass
	return render(request,'blog/detail.html',{"blog":blog})
	
def register(request):
	register=False
	if request.method =='POST':
		user_form=Userform(data=request.POST)
		profile_form=UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			user.save()
			profile=profile_form.save(commit=False)
			profile.user=user
			if 'picture' in request.FILES:
				profile.picture=request.FILES['picture']
			profile.save()
			register=True
		else:
			print user_form.errors,profile_form.errors
	else:
		user_form=Userform()
		profile_form=UserProfileForm()
	return render(request,'blog/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':register})
def user_login(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(username=username,password=password)
		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/blog/')
			else:
				return HttpResponse("The password is valid, but the account has been disabled!")
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request,'blog/login.html',{})
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/blog/')
@login_required
def restricted(request):
	return HttpResponseRedirect('/login/')