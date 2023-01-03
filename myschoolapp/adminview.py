from django.shortcuts import render, redirect
from django.contrib import messages

import myschool
from myschoolapp.forms import courseform, syllabusform, timetableform, examtableform, dutyform, examresultform, \
    staffmeetingform, parentsmeetingform, communitygroupform
from myschoolapp.models import TeacherLogin, Course, Syllabus, TimeTable, ExamTable, Duty, ExamResult, StaffMeeting, \
    ParentsMeeting, CommunityGroup,Appointment


def teacherview(request):
    data=TeacherLogin.objects.all()
    return render(request,'admin/teacherview.html',{'data':data})

def dele(request,id):
    TeacherLogin.objects.get(id=id).delete()
    return redirect('teacherview')

def addcourse(request):
    form = courseform()
    if request.method == 'POST':
        form = courseform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courseview')
    return render(request,'admin/addcourse.html',{'form':form})



def courseview(request):
    data=Course.objects.all()
    return render(request,'admin/courseview.html',{'data':data})

def upcourse(request,id):
    a=Course.objects.get(id=id)
    form=courseform(instance=a)
    if request.method=='POST':
        form=courseform(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('courseview')
    return render(request,'admin/upcourse.html',{'form':form})


def delecourse(request,id):
    Course.objects.get(id=id).delete()
    return redirect('courseview')

def addsyllabus(request):
    form=syllabusform()
    if request.method=='POST':
        form=syllabusform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('syllabusview')
    return render(request,'admin/addsyllabus.html',{'form':form})

def syllabusview(request):
    data=Syllabus.objects.all()
    return render(request,'admin/syllabusview.html',{'data':data})

def upsyllabus(request,id):
    a=Syllabus.objects.get(id=id)
    form=syllabusform(instance=a)
    if request.method=='POST':
        form=syllabusform(request.POST,request.FILES,instance=a)
        if form.is_valid():
            form.save()
            return redirect('syllabusview')
    return render(request,'admin/upsyllabus.html',{'form':form})

def delesyllabus(request,id):
    Syllabus.objects.get(id=id).delete()
    return redirect('syllabusview')

def addtimetable(request):
    form=timetableform()
    if request.method=='POST':
        form=timetableform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timetableview')
    return render(request,'admin/addtimetable.html',{'form':form})

def timetableview(request):
    data=TimeTable.objects.all()
    return render(request,'admin/timetableview.html',{'data':data})


def uptimetable(request,id):
    a=TimeTable.objects.get(id=id)
    form=timetableform(instance=a)
    if request.method=='POST':
        form=timetableform(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('timetableview')
    return render(request,'admin/uptimetable.html',{'form':form})


def deletimetable(request,id):
    TimeTable.objects.get(id=id).delete()
    return redirect('timetableview')


def addexamtable(request):
    form = examtableform()
    if request.method == 'POST':
        form = examtableform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('examtableview')
    return render(request, 'admin/addexamtable.html', {'form': form})

def examtableview(request):
    data=ExamTable.objects.all()
    return render(request,'admin/examtableview.html',{'data':data})

def upexamtable(request,id):
    a=ExamTable.objects.get(id=id)
    form=examtableform(instance=a)
    if request.method=='POST':
        form=examtableform(request.POST,request.FILES,instance=a)
        if form.is_valid():
            form.save()
            return redirect('examtableview')
    return render(request,'admin/upexamtable.html',{'form':form})

def deleexamtable(request,id):
    ExamTable.objects.get(id=id).delete()
    return redirect('examtableview')

def addduty(request):
    form=dutyform()
    if request.method=='POST':
        form=dutyform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dutyview')
    return render(request,'admin/addduty.html',{'form':form})

def dutyview(request):
    data=Duty.objects.all()
    return render(request,'admin/dutyview.html',{'data':data})

def upduty(request,id):
    a=Duty.objects.get(id=id)
    form=dutyform(instance=a)
    if request.method=='POST':
        form=dutyform(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('dutyview')
    return render(request,'admin/upduty.html',{'form':form})

def deleduty(request,id):
    Duty.objects.get(id=id).delete()
    return redirect('dutyview')

def addexamresult(request):
    form =examresultform()
    if request.method == 'POST':
        form = examresultform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('examresultview')
    return render(request, 'admin/addexamresult.html', {'form': form})


def examresultview(request):
    data=ExamResult.objects.all()
    return render(request,'admin/examresultview.html',{'data':data})


def upexamresult(request,id):
    a=ExamResult.objects.get(id=id)
    form=examresultform(instance=a)
    if request.method=='POST':
        form=examresultform(request.POST,request.FILES,instance=a)
        if form.is_valid():
            form.save()
            return redirect('examresultview')
    return render(request,'admin/upexamresult.html',{'form':form})

def deleexamresult(request,id):
    ExamResult.objects.get(id=id).delete()
    return redirect('examresultview')



def addstaffmeeting(request):
    form = staffmeetingform()
    if request.method == 'POST':
        form = staffmeetingform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staffmeetingview')
    return render(request, 'admin/addstaffmeeting.html', {'form': form})


def staffmeetingview(request):
    data=StaffMeeting.objects.all()
    return render(request,'admin/staffmeetingview.html',{'data':data})

def upstaffmeeting(request,id):
    a=StaffMeeting.objects.get(id=id)
    form=staffmeetingform(instance=a)
    if request.method=='POST':
        form=staffmeetingform(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('staffmeetingview')
    return render(request,'admin/upstaffmeeting.html',{'form':form})

def delestaffmeeting(request,id):
    StaffMeeting.objects.get(id=id).delete()
    return redirect('staffmeetingview')


def addparentsmeeting(request):
    form = parentsmeetingform()
    if request.method == 'POST':
        form = parentsmeetingform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parentsmeetingview')
    return render(request, 'admin/addparentsmeeting.html', {'form': form})



def parentsmeetingview(request):
    data=ParentsMeeting.objects.all()
    return render(request,'admin/parentsmeetingview.html',{'data':data})

def upparentsmeeting(request,id):
    a=ParentsMeeting.objects.get(id=id)
    form=parentsmeetingform(instance=a)
    if request.method=='POST':
        form=parentsmeetingform(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('parentsmeetingview')
    return render(request,'admin/upparentsmeeting.html',{'form':form})

def deleparentsmeeting(request,id):
    ParentsMeeting.objects.get(id=id).delete()
    return redirect('parentsmeetingview')


def addcommunitygroup(request):
    form = communitygroupform()
    if request.method == 'POST':
        form = communitygroupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admincommunitygroupview')
    return render(request, 'admin/addcommunitygroup.html', {'form': form})

def admincommunitygroupview(request):
    data=CommunityGroup.objects.all()
    return render(request,'admin/communitygroupview.html',{'data':data})



def upcommunitygroup(request,id):
    a=CommunityGroup.objects.get(id=id)
    form=communitygroupform(instance=a)
    if request.method=='POST':
        form=communitygroupform(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('admincommunitygroupview')
    return render(request,'admin/upcommunitygroup.html',{'form':form})

def delecommunitygroup(request,id):
    CommunityGroup.objects.get(id=id).delete()
    return redirect('admincommunitygroupview')

def managecommunitygroup(request):
    data=CommunityGroup.objects.all()
    return render(request,'admin/managecommunitygroup.html',{'data':data})

def appointment_admin(request):
    a = Appointment.objects.all()
    context = {
        'appointment': a,
    }
    return render(request, 'admin/appointments.html', context)

def approve_appointment(request, id):
    a = Appointment.objects.get(id=id)
    a.status = 1
    a.save()
    messages.info(request, 'Appointment  Confirmed')
    return redirect('appointment_admin')

def reject_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request, 'Appointment Rejected')
    return redirect('appointment_admin')
