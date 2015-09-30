# coding=utf8
from django.shortcuts import render,render_to_response
from django.conf import settings

# Create your views here.
from blog.models import Artical,Author,Tag,Classification,UserProfile
from django.template import RequestContext
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import Userform,UserProfileForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
import jwt
# @login_required
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
def user_login1(request):
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
def user_logout1(request):
	logout(request)
	return HttpResponseRedirect('/blog/')
@login_required
def restricted(request):
	return HttpResponseRedirect('/accounts/login/')

def set_jwt_and_response(user, response):
    # For duoshuo jwt login
    if user is not None and user.is_authenticated() and user.is_active:
    	user_profile = UserProfile.objects.filter(user=user)
        if not user_profile:
        	# if no local user
        	# use jwt to create user
        	# For duoshuo jwt login
            duoshuo_jwt_token = None
            username = user.get_full_name()
            if not username:
                username = user.username
            token = {
                "short_name": settings.DUOSHUO_SHORT_NAME,
                "user_key": user.id,
                "name": username
            }
            duoshuo_jwt_token = jwt.encode(token, settings.DUOSHUO_SECRET)
            response.set_cookie('duoshuo_token', duoshuo_jwt_token)
    return response
def user_logout(request):
    auth.logout(request)
    response = HttpResponseRedirect(reverse('blog:user_login'))
    response.delete_cookie('duoshuo_token')
    return response
def user_login(request):
	code = request.GET.get('code', '')
	next_url = decide_next_url(request.GET.get('next', ''))
	if len(code) > 0: # 多说登录
		api = DuoshuoAPI(settings.DUOSHUO_SHORT_NAME, settings.DUOSHUO_SECRET)
		response = api.get_token(code=code)
		if response.has_key('user_key'): # 这个多说账号已经绑定过本地账户了
			user = User.objects.get(pk=int(response['user_key']))
        	user.backend = 'django.contrib.auth.backends.ModelBackend'
        	auth.login(request, user)
        	user_profile = UserProfile.objects.filter(user=user)
        	if not user_profile: # 手动绑定了多说账号和本地账号, 但是本地没有对应的 user_profile
        		user_profile = User_Profile(user=user,duoshuo_id=int(response['user_id']), avatar=response['avatar_url'])
            	user_profile.save()
    	else: # 这个多说账户还没有绑定
        	access_token = response['access_token']
        	user_profile = UserProfile.objects.filter(duoshuo_id=int(response['user_id']))
        	if user_profile: #此多说账号在本站已经注册过了, 但是没有绑定, 则先绑定, 然后直接登录
        		user = user_profile.first().user
        		user.backend = 'django.contrib.auth.backends.ModelBackend'
        		auth.login(request, user)
            	else:
            		print 'api.users.profile user_id %s' % response['user_id']
            	response = api.users.profile(user_id=response['user_id'])['response']
            	print response
            	username = 'duoshuo_%s' % response['user_id']
            	while User.objects.filter(username=username).count():
                	username = username + str(random.randrange(1,9)) #如果多说账号用户名和本站用户名重复，就加上随机数字
            	tmp_password = ''.join([random.choice('abcdefg&#%^*f') for i in range(8)]) #随机长度8字符做密码
            	new_user = User.objects.create_user(username=username, email='user@example.com', password=tmp_password, first_name=response['name']) #默认密码和邮箱，之后让用户修改
            	user_profile = UserProfile.objects.get_or_create(user=new_user)[0]
            	user_profile.duoshuo_id = int(response['user_id']) #把返回的多说ID存到profile
            	user_profile.avatar = response['avatar_url']
            	user_profile.save()
            	user = auth.authenticate(username=username, password=tmp_password)
            	auth.login(request, user)
        	# SSO 同步多说账户
        	sync_sso_duoshuo(access_token, request.user)
    	response = HttpResponseRedirect(next_url)
    	return set_jwt_and_response(request.user, response)
def sync_sso_duoshuo(access_token, user):
    '''将SSO本地用户同步到已有多说账户中
    '''
    url = 'http://api.duoshuo.com/sites/join.json'
    username = user.get_full_name()
    if not username:
        username = user.username
    email = user.email
    if not email:
        email = 'user@example.com'
    params = {
        'short_name': settings.DUOSHUO_SHORT_NAME,
        'secret': settings.DUOSHUO_SECRET,
        'access_token': access_token,
        'user[user_key]': user.id,
        'user[name]': username,
        'user[email]': user.email,
    }
    data = urllib.urlencode(params)
    request = urllib2.Request(url, data=data)
    response = urllib2.urlopen(request)
    result = response.read()
