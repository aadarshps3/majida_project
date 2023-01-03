from django import forms
from django.contrib.auth.forms import UserCreationForm


from myschoolapp.models import Login, TeacherLogin, StudentLogin, ParentLogin, Course, Syllabus, TimeTable, ExamTable, \
    Duty, ExamResult, StaffMeeting, ParentsMeeting, CommunityGroup, TeacherAttendance, StudyMaterial, Mark, Note, \
    Complaint


class LoginReg(UserCreationForm):
    class Meta:
        model=Login
        fields=('username','password1','password2')

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class TeacherReg(forms.ModelForm):
    class Meta:
        model=TeacherLogin
        exclude=('user',)


class StudentReg(forms.ModelForm):
    class Meta:
        model=StudentLogin
        exclude=('user',)


class ParentReg(forms.ModelForm):
    class Meta:
        model=ParentLogin
        exclude=('user',)


class courseform(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'

dep_choice=(
    ('..','..'),
    ('bca','bca'),
    ('mca','mca')
)
class timetableform(forms.ModelForm):
    department=forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=TimeTable
        fields='__all__'

class syllabusform(forms.ModelForm):
    class Meta:
        model=Syllabus
        fields='__all__'


class examtableform(forms.ModelForm):
    class Meta:
        model=ExamTable
        fields='__all__'

class dutyform(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    time=forms.TimeField(widget=TimeInput)
    department=forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=Duty
        fields='__all__'


class examresultform(forms.ModelForm):
    department=forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=ExamResult
        fields='__all__'


class staffmeetingform(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    time=forms.TimeField(widget=TimeInput)
    class Meta:
        model=StaffMeeting
        fields='__all__'

class parentsmeetingform(forms.ModelForm):
    department=forms.ChoiceField(choices=dep_choice)
    date=forms.DateField(widget=DateInput)
    time=forms.TimeField(widget=TimeInput)
    class Meta:
        model=ParentsMeeting
        fields='__all__'


class communitygroupform(forms.ModelForm):
    department=forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=CommunityGroup
        exclude=('status',)

class teacherattendanceform(forms.ModelForm):

    class Meta:
        model =TeacherAttendance
        fields = '__all__'

class studymaterial(forms.ModelForm):
    department = forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=StudyMaterial
        fields='__all__'

class markform(forms.ModelForm):
    department=forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=Mark
        fields='__all__'

class noteform(forms.ModelForm):
    department = forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=Note
        fields='__all__'

class complaintform(forms.ModelForm):
    department = forms.ChoiceField(choices=dep_choice)
    class Meta:
        model=Complaint
        fields='__all__'