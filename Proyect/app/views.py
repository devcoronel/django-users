from django.shortcuts import render, redirect
from .models import Users
from .forms import UserForm

# Create your views here.

def users(request):
	users = Users.objects.all()
	ctx = {
		'users': users
	}
	return render(request, 'index.html', ctx)

def adduser(request):
	if request.method == 'GET':
		form = UserForm()
		ctx = {
			'form': form,
			'title': "Add User",
			'button': "Create"
		}
		return render(request, 'adduser.html', ctx)

	if request.method == 'POST':
		form = UserForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('users')

def edit(request, id):
	user = Users.objects.get(id = id)

	if request.method == 'GET':
		form = UserForm(instance = user)
		ctx = {
			'form': form,
			'title': "Edit user",
			'button': "Save changes"
		}
		return render(request, 'adduser.html', ctx)

	if request.method =='POST':
		form = UserForm(request.POST, instance = user)
		if form.is_valid():
			form.save()
			return redirect('users')

def delete(request, id):
	user = Users.objects.get(id = id)
	user.delete()
	return redirect('users')