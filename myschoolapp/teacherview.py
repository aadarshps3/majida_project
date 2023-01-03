from django.shortcuts import render, redirect
from django.contrib import messages

from myschoolapp.forms import teacherattendanceform, communitygroupform, studymaterial, markform
from myschoolapp.models import StudentLogin, ParentLogin, StaffMeeting, Duty, TeacherAttendance, TeacherLogin, \
    CommunityGroup, Syllabus, ExamTable, TimeTable, ParentsMeeting, StudyMaterial, Mark, ExamResult,Appointment


def studentview(request):
    data=StudentLogin.objects.all()
    return render(request,'teacher/studentview.html',{'data':data})

def delestudent(request,id):
    StudentLogin.objects.get(id=id).delete()
    return redirect('studentview')


def parentview(request):
    data=ParentLogin.objects.all()
    return render(request,'teacher/parentview.html',{'data':data})

def deleparent(request,id):
    ParentLogin.objects.get(id=id).delete()
    return redirect('parentview')

def staffmeetingview(request):
    data=StaffMeeting.objects.all()
    return render(request,'teacher/staffmeetingview.html',{'data':data})

def dutyview(request):
    u=TeacherLogin.objects.get(user=request.user)
    data=Duty.objects.filter(teacher=u)
    return render(request,'teacher/dutyview.html',{'data':data})

def addteacherattendance(request):
    form=teacherattendanceform()
    if request.method=='POST':
        form=teacherattendanceform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacherattendanceview')
    return render(request,'teacher/addteacherattendance.html',{'form':form})

def teacherattendanceview(request):
    data=TeacherAttendance.objects.all()
    return render(request,'teacher/teacherattendanceview.html',{'data':data})

def upteacherattendance(request,id):
    a=TeacherAttendance.objects.get(id=id)
    form=teacherattendanceform(instance=a)
    if request.method=='POST':
        form=teacherattendanceform(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('teacherattendanceview')
    return render(request,'teacher/upteacherattendance.html',{'form':form})

def deleteacherattendance(request,id):
    TeacherAttendance.objects.get(id=id).delete()
    return redirect('teacherattendanceview')





def communitygroupview(request):
    data=CommunityGroup.objects.all()
    return render(request,'teacher/communitygroupview.html',{'data':data})

def tsyllabusview(request):
    data=Syllabus.objects.all()
    return render(request,'teacher/tsyllabusview.html',{'data':data})

def texamtableview(request):
    data=ExamTable.objects.all()
    return render(request,'teacher/texamtableview.html',{'data':data})

def ttimetableview(request):
    data=TimeTable.objects.all()
    return render(request,'teacher/ttimetableview.html',{'data':data})


def tparentsmeetingview(request):
    data=ParentsMeeting.objects.all()
    return render(request,'teacher/tparentsmeetingview.html',{'data':data})

def addstudymaterial(request):
    form=studymaterial()
    if request.method=='POST':
        form=studymaterial(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('studymaterialview')
    return render(request,'teacher/addstudymaterial.html',{'form':form})

def studymaterialview(request):
    data=StudyMaterial.objects.all()
    return render(request,'teacher/studymaterialview.html',{'data':data})

def upstudymaterial(request,id):
    a=StudyMaterial.objects.get(id=id)
    form=studymaterial(instance=a)
    if request.method=='POST':
        form=studymaterial(request.POST,request.FILES,instance=a)
        if form.is_valid():
            form.save()
            return redirect('studymaterialview')
    return render(request,'teacher/upstudymaterial.html',{'form':form})

def delestudymaterial(request,id):
    StudyMaterial.objects.get(id=id).delete()
    return redirect('studymaterialview')


def addmark(request):
    form=markform()
    if request.method=='POST':
        form=markform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('markview')
    return render(request,'teacher/addmark.html',{'form':form})

def markview(request):
    data=Mark.objects.all()
    return render(request,'teacher/markview.html',{'data':data})

def upmark(request,id):
    a=Mark.objects.get(id=id)
    form=markform(instance=a)
    if request.method=='POST':
        form=markform(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('markview')
    return render(request,'teacher/upmark.html',{'form':form})

def delemark(request,id):
    Mark.objects.get(id=id).delete()
    return redirect('markview')

def texamresultview(request):
    data=ExamResult.objects.all()
    return render(request,'teacher/texamresultview.html',{'data':data})

def join_community(request, id):
    s = CommunityGroup.objects.get(id=id)
    c = TeacherLogin.objects.get(user=request.user)
    print(c)
    appointment = Appointment.objects.filter(user=c, schedule=s)
    if appointment.exists():
        messages.info(request, 'You Have Already Requested Appointment for this Schedule')
        return redirect('communitygroupview')
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.user = c
            obj.schedule = s
            obj.save()
            messages.info(request, 'Appointment Booked Successfully')
            return redirect('appointment_view')
    return render(request, 'teacher/take_appointment.html', {'schedule': s})



def appointment_view(request):
    c = TeacherLogin.objects.get(user=request.user)
    a = Appointment.objects.filter(user=c)
    return render(request, 'teacher/appointment_view.html', {'appointment': a})


