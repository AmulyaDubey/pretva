from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Profile

def index(request):
        if request.method== 'POST':
                form=SignUpForm(request.POST)
                if form.is_valid:
                        username=request.POST.get('username','')
                        email=request.POST.get('email','')
                        city=request.POST.get('city','')
                        company=request.POST.get('company','')
                        category=request.POST.get('category','')
                        obj=Profile(username=username,email=email, city=city, company=company, category=category) 
                        obj.save()
                        print(obj.category)
                        return redirect('/demo/dashboard/'+ str(obj.user_id))
        else :
                form=SignUpForm()
        return render(request, 'demo/index.html', {'form':form})

def dashboard(request,pk):
        user=Profile.objects.get(user_id=pk)
        return render(request, 'demo/dashboard.html', {'user':user})
 