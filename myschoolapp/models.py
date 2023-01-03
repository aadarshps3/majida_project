from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_teacher=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)
    is_parent=models.BooleanField(default=False)

class TeacherLogin(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name='teacher')

    name=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=30)
    location=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone_no=models.IntegerField()
    email=models.EmailField()
    qualification=models.CharField(max_length=100)
    department=models.CharField(max_length=100)

    def __str__(self):
        return self.name







class StudentLogin(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name='student')

    name=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=30)
    location=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone_no=models.IntegerField()
    email=models.EmailField()
    parent_name=models.CharField(max_length=100)
    parent_phn_no=models.IntegerField()
    department=models.CharField(max_length=100)

    def __str__(self):
        return self.name





class ParentLogin(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name='parent')
    name=models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    email = models.EmailField()

    s_name = models.CharField(max_length=10)
    department = models.CharField(max_length=10)




class Course(models.Model):
    course_name=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    explanation=models.CharField(max_length=200)
    course_duration=models.CharField(max_length=200)

    def __str__(self):
        return self.course_name



class Syllabus(models.Model):
    date=models.DateField(auto_now=True)
    add_syllabus=models.FileField(upload_to='syllabus')

    def __str__(self):
        return self.add_syllabus



class TimeTable(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    department=models.CharField(max_length=200)
    mon=models.CharField(max_length=200)
    tue=models.CharField(max_length=200)
    wed=models.CharField(max_length=200)
    thu=models.CharField(max_length=200)
    fri=models.CharField(max_length=200)



class ExamTable(models.Model):
    date=models.DateField(auto_now=True)
    add_timetable=models.FileField(upload_to='timetable')


class Duty(models.Model):
    teacher=models.ForeignKey(TeacherLogin,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    department=models.CharField(max_length=200)


class ExamResult(models.Model):
    student=models.ForeignKey(StudentLogin,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    department=models.CharField(max_length=200)
    result=models.FileField(upload_to='result')

class StaffMeeting(models.Model):
    date=models.DateField()
    time=models.TimeField()
    content=models.CharField(max_length=200)

class ParentsMeeting(models.Model):
    date=models.DateField()
    time=models.TimeField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    department=models.CharField(max_length=200)
    content=models.CharField(max_length=200)


class CommunityGroup(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    status = models.IntegerField(default=0)


class TeacherAttendance(models.Model):
    teacher = models.ForeignKey(TeacherLogin, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    attendance=models.BooleanField(default=True)

    def __str__(self):
        return str(self.teacher)

class StudyMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    studymaterial = models.FileField(upload_to='studymaterial')


class Mark(models.Model):
    student=models.ForeignKey(StudentLogin,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    department=models.CharField(max_length=200)
    s1=models.CharField(max_length=200)
    s2=models.CharField(max_length=200)
    s3=models.CharField(max_length=200)
    s4=models.CharField(max_length=200)
    s5=models.CharField(max_length=200)
    s6=models.CharField(max_length=200)

class Note(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    subject=models.CharField(max_length=200)
    note = models.FileField(upload_to='studymaterial')


class Complaint(models.Model):
    student = models.ForeignKey(StudentLogin, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    complaint=models.TextField(max_length=10000)

class Appointment(models.Model):
    user = models.ForeignKey(TeacherLogin, on_delete=models.CASCADE, related_name='appointment')
    schedule = models.ForeignKey(CommunityGroup, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)



