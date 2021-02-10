from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from enroll.forms import StudentRegistration
from enroll.models import User

# this function add and show the student informations
def add_show(request):
    if request.method =="POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            register = User(name=name,email=email,password=password)
            register.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
    stud= User.objects.all()
    return render(request,'addandshow.html', {'form': fm, 'stu': stud})
# this funstion remove the student from the database
def delete_data(request,id):
    if request.method=="POST":
        de = User.objects.get(pk=id)
        de.delete()
        return HttpResponseRedirect('/')

# this function will edit the information of the student

def edit_data(request, id):
    if request.method == 'POST':
        ei = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=ei)
        if fm.is_valid():
            fm.save()
            return redirect('addandshow')
    else:
        ei = User.objects.get(pk=id)
        fm = StudentRegistration(instance=ei)
    return render(request, 'updatestudent.html', {'form': fm })