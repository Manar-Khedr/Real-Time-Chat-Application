from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

#Front page
def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == "POST": #form has ben clicked
        form=SignUpForm(request.POST) #create a new instance
        
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('frontpage')
        
    else:
            form=SignUpForm()
            
    return render(request, 'core/signup.html',{'form': form}) #, {'form':form}       
            
        
        
