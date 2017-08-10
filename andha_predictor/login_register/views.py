from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.models import User
from .registerform import registerForm

def index(request):
	# return HttpResponse("<h1> Login Page </h1>")
	template = loader.get_template('login_register/index.html')
	context = {}
	# return HttpResponse(template.render(context,request))
	return render(request, 'login_register/index.html',context)

def createUser(request):
	new_user_form = registerForm(request.POST, request.FILES)
	# print(new_user_form.errors)
	if not new_user_form.is_valid():
		return render(request, 'login_register/index.html', {'message': 'Error! '})
	else:
		try:
			new_user = User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['password'])
			new_user.first_name = request.POST['first_name']			
			new_user.last_name = request.POST['last_name']
			new_user.save()
		except:
			return render(request, 'login_register/index.html', {'message': 'Error! '})
		return render( request, 'login_register/index.html', {'message': 'Done!'})

