from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def uhome(request):
	if request.user.is_authenticated:
			return render(request, "home.html")
	else:
			return redirect("ulogin")


def ulogin(request):
		if request.user.is_authenticated:
					return redirect("uhome")
		elif request.method == "POST":
				un = request.POST.get("un")
				pw = request.POST.get("pw")
				usr = authenticate(username=un,password = pw)
				if usr is None:
					return render(request, "login.html", {"msg":"invalid login"})
				else:
					login(request, usr)
					return redirect("uhome")
		else:
				return render(request, "login.html")

def usignup(request):
		if request.user.is_authenticated:
				return redirect("uhome")
		elif request.method == "POST":
				un = request.POST.get("un")
				pw1 = request.POST.get("pw1")
				pw2 = request.POST.get("pw2")
				if pw1 == pw2:
					try:
						usr = User.objects.get(username=un)
						return render(request, "signup.html", {"msg":"user already exists"})
					except User.DoesNotExist:
						usr = User.objects.create_user(username=un, password=pw1)
						usr.save()
						return redirect("ulogin")
				else:
					return render(request, "signup.html", {"msg":"passwords didnot match"})
		else:
				return render(request, "signup.html")
def ulogout(request):
		logout(request)
		return redirect("ulogin")

def home(request):
	if request.GET.get("num"):
		try:
			num=int(request.GET.get("num"))
			if num%2==0:
				msg="num"+str(num)+"is even"
			else:
				msg="num"+str(num)+"is odd"
			return render(request,"home.html",{"msg":res})
		except ValueError:
			msg="u should enter intger only"
			return render(request,"home.html",{"msg":res})
	else:
		return render(request,"home.html")
							

