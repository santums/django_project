from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages 
from .forms import SignUpForm, EditProfileForm
from search.models import *
from search.forms import *

@cache_control(no_cache=True, must_revalidate=True, no_store=True)

# Create your views here.

def home(request):
	return render(request, 'search/home.html', {})

#Shift Roster Module
#Viewing image
def shift_img(request):
	if request.method=="POST":
		month=request.POST.get('month')
		year=request.POST.get('year')
		level=request.POST.get('level')
		month=month+'%'
		shift_search=shift.objects.raw('select * from shift where year="'+year+'"and level="'+level+'" and month like "'+month+'"')
		return render(request,'search/shift.html',{"shift":shift_search})
	else:
		shift_obj=shift.objects.raw('select * from shift ORDER BY ID DESC LIMIT 4')
		return render(request,'search/shift.html',{"shift":shift_obj})


def shift_edit(request):
	if request.method=="POST":
		month=request.POST.get('month')
		year=request.POST.get('year')
		level=request.POST.get('level')
		month=month+'%'
		shift_search=shift.objects.raw('select * from shift where year="'+year+'"and level="'+level+'" and month like "'+month+'"')
		return render(request,'search/shift_edit.html',{"shift":shift_search})
	else:
		shift_obj=shift.objects.raw('select * from shift')
		return render(request,'search/shift_edit.html',{"shift":shift_obj})

def upload_shift(request):
	if request.method == "POST":
		form = shift_form(request.POST, request.FILES)
		if form.is_valid():
			try:
				form.save()
				messages.success(request, ('Uploaded successfully...!'))
				return redirect('/shift_upload')
			except:
				pass
	else:
		form = shift_form()
	return render(request,"search/upload_shift.html",{'form':form})

def editshift(request,id):
	shift_det = shift.objects.get(id=id)
	return render(request,'search/edit_shift.html',{'shift':shift_det})
	
def updateshift(request,id):
	shift_det = shift.objects.get(id=id)
	form = shift_form(request.POST, request.FILES, instance = shift_det)
	if form.is_valid():
		form.save()
		messages.success(request, ('Updated successfully...!'))
		return redirect('/shift_edit')
	return render(request,'search/edit_shift.html',{'shift':shift_det})

def destroyshift(request,id):
	shift_det = shift.objects.get(id=id)
	shift_det.delete()
	return redirect("/shift_edit")
	
#Training documents Module
#Viewing Document
def train_doc(request):
	docs=train.objects.all()
	return render(request, 'search/train.html', {'train': docs})

def train_edit(request):
	docs=train.objects.all()
	return render(request, 'search/trainedit.html', {'train': docs})

def upload_train(request):
	if request.method == "POST":
		form = train_form(request.POST, request.FILES)
		if form.is_valid():
			try:
				form.save()
				messages.success(request, ('Uploaded successfully...!'))
				return redirect('/train_upload')
			except:
				pass
	else:
		form = train_form()
	return render(request,"search/upload_train.html",{'form':form})

def destroytrain(request,id):
	train_det = train.objects.get(id=id)
	train_det.delete()
	return redirect("/train_edit")
	
#SOP Module
#Searching SOP
def sop_list(request):
	if request.method=="POST":
		region=request.POST.get('region')
		operator=request.POST.get('operator')
		topic=request.POST.get('topic')
		operator=operator+'%'
		topic=topic+'%'
		sop_search=sop.objects.raw('select * from sop where (operator like "'+operator+'" or operator = "Common") and topic like "'+topic+'" and (region= "'+region+'" or region = "Common") order by doc ASC')
		return render(request,'search/sop.html',{"sop":sop_search})
	else:
		sopobj=sop.objects.raw('select * from sop order by doc ASC')
		return render(request,'search/sop.html',{"sop":sopobj})

def show(request):
	if request.method=="POST":
		region=request.POST.get('region')
		operator=request.POST.get('operator')
		topic=request.POST.get('topic')
		operator=operator+'%'
		topic=topic+'%'
		sop_search=sop.objects.raw('select * from sop where (operator like "'+operator+'" or operator = "Common") and topic like "'+topic+'" and (region= "'+region+'" or region = "Common") order by doc ASC')
		return render(request,'search/sopedit.html',{"sop":sop_search})
	else:
		sopobj=sop.objects.raw('select * from sop order by doc ASC')
		return render(request,'search/sopedit.html',{"sop":sopobj})

#Upload SOP		
def upload_sop(request):
	if request.method == "POST":
		form = sop_form(request.POST, request.FILES)
		if form.is_valid():
			try:
				form.save()
				messages.success(request, ('Uploaded successfully...!'))
				return redirect('/sop_upload')
			except:
				pass
	else:
		form = sop_form()
	#return render(request,"search/index.html",{'form':form})
	return render(request,"search/upload_sop.html",{'form':form})

def editsop(request,id):
	sop_det = sop.objects.get(id=id)
	return render(request,'search/editsop.html',{'sop':sop_det})
	
def updatesop(request,id):
	sop_det = sop.objects.get(id=id)
	form = sop_form(request.POST, request.FILES, instance = sop_det)
	if form.is_valid():
		form.save()
		messages.success(request, ('Updated successfully...!'))
		return redirect('/sopedit')
	return render(request,'search/editsop.html',{'sop':sop_det})
	
def destroysop(request,id):
	sop_det = sop.objects.get(id=id)
	sop_det.delete()
	return redirect("/sopedit")

#Escalation matrix Module	
#Searching EM
def searchesc(request):
	if request.method=="POST":
		oper=request.POST.get('oper')
		app=request.POST.get('ari')
		oper=oper+'%'
		esc_search=EscMat.objects.raw('select * from escalation where oper like "'+oper+'" and ari = "'+app+'"')
		return render(request,'search/escmat.html',{"EscMat":esc_search})
	else:
		escobj=EscMat.objects.raw('select * from escalation')
		return render(request,'search/escmat.html',{"EscMat":escobj})

#editing Module
def show1(request):
	if request.method=="POST":
		oper=request.POST.get('oper')
		app=request.POST.get('ari')
		oper=oper+'%'
		esc_search=EscMat.objects.raw('select * from escalation where oper like "'+oper+'" and ari = "'+app+'"')
		return render(request,'search/escedit.html',{"EscMat":esc_search})
	else:
		escobj=EscMat.objects.raw('select * from escalation')
		return render(request,'search/escedit.html',{"EscMat":escobj})
	
def editesc(request,id):
	esc_det = EscMat.objects.get(id=id)
	return render(request,'search/editesc.html',{'EscMat':esc_det})
	
def update(request,id):
	esc_det = EscMat.objects.get(id=id)
	form = esc_form(request.POST, instance = esc_det)
	if form.is_valid():
		form.save()
		messages.success(request, ('Updated successfully...!'))
		return redirect('/escedit')
	return render(request,'search/editesc.html',{'EscMat':esc_det})
	
def destroy(request,id):
	esc_det = EscMat.objects.get(id=id)
	esc_det.delete()
	return redirect("/escedit")
	
#Upload Module
def esc_upload(request):
	if request.method == "POST":
		form = esc_form(request.POST)
		if form.is_valid():
			try:
				form.save()
				messages.success(request, ('Uploaded successfully...!'))
				return redirect('/escadd')
			except:
				pass
	else:
		form = esc_form()
	#return render(request,"search/index.html",{'form':form})
	return render(request,"search/escadd.html",{'form':form})


#Authentication Module
#Login Module

#@login_required(login_url='login')	
def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('Logged in successfully...!'))
			return redirect('home')

		else:
			messages.success(request, ('Error Logging In - Please Try Again...'))
			return redirect('login')
	else:
		return render(request, 'search/login.html', {})

def logout_user(request):
	logout(request)
	#messages.success(request, ('You Have Been Logged Out...'))
	return redirect('login')
	
def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('You Have Edited Your Profile...'))
			return redirect('home')
	else:
		form = EditProfileForm(instance=request.user)
	
	context = {'form': form}
	return render(request, 'search/edit_profile.html', context)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('You Have Edited Your Password...'))
			return redirect('home')
	else:
		form = PasswordChangeForm(user=request.user)
	
	context = {'form': form}
	return render(request, 'search/change_password.html', context)
	

        
