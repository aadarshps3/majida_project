from django.urls import path

from myschoolapp import views, adminview, teacherview, studentview

urlpatterns = [
    path('',views.index,name='index'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('treg',views.treg,name='treg'),
    path('sreg',views.sreg,name='sreg'),
    path('preg',views.preg,name='preg'),
    path('adindex',views.adindex,name='adindex'),
    path('tindex',views.tindex,name='tindex'),
    path('sindex',views.sindex,name='sindex'),
    path('pindex',views.pindex,name='pindex'),
    path('tcgindex',views.tcgindex,name='tcgindex'),
    path('scgindex',views.scgindex,name='scgindex'),
    path('pcgindex',views.pcgindex,name='pcgindex'),
    path('teacherview',adminview.teacherview,name='teacherview'),
    path('dele/<int:id>/',adminview.dele,name='dele'),


    path('addteacherattendance',teacherview.addteacherattendance,name='addteacherattendance'),
    path('teacherattendanceview',teacherview.teacherattendanceview,name='teacherattendanceview'),
    path('upteacherattendance/<int:id>/',teacherview.upteacherattendance,name='upteacherattendance'),
    path('deleteacherattendance/<int:id>/',teacherview.deleteacherattendance,name='deleteacherattendance'),





    path('studentview',teacherview.studentview,name='studentview'),
    path('delestudent/<int:id>/',teacherview.delestudent,name='delestudent'),
    path('deleparent/<int:id>/',teacherview.deleparent,name='deleparent'),


    path('parentview',teacherview.parentview,name='parentview'),

    path('staffmeetingview',teacherview.staffmeetingview,name='staffmeetingview'),
    path('dutyview',teacherview.dutyview,name='dutyview'),
    path('communitygroupview',teacherview.communitygroupview,name='communitygroupview'),


    path('addcourse',adminview.addcourse,name='addcourse'),
    path('upcourse/<int:id>/',adminview.upcourse,name='upcourse'),
    path('delecourse/<int:id>/',adminview.delecourse,name='delecourse'),

    path('courseview',adminview.courseview,name='courseview'),
    path('addsyllabus',adminview.addsyllabus,name='addsyllabus'),
    path('syllabusview',adminview.syllabusview,name='syllabusview'),
    path('upsyllabus/<int:id>/',adminview.upsyllabus,name='upsyllabus'),
    path('delesyllabus/<int:id>/',adminview.delesyllabus,name='delesyllabus'),



    path('addtimetable',adminview.addtimetable,name='addtimetable'),
    path('timetableview',adminview.timetableview,name='timetableview'),
    path('uptimetable/<int:id>/',adminview.uptimetable,name='uptimetable'),
    path('deletimetable/<int:id>/',adminview.deletimetable,name='deletimetable'),



    path('addexamtable',adminview.addexamtable,name='addexamtable'),
    path('examtableview',adminview.examtableview,name='examtableview'),
    path('upexamtable/<int:id>/',adminview.upexamtable,name='upexamtable'),
    path('deleexamtable/<int:id>/',adminview.deleexamtable,name='deleexamtable'),




    path('addduty',adminview.addduty,name='addduty'),
    path('dutyview',adminview.dutyview,name='dutyview'),
    path('upduty/<int:id>/',adminview.upduty,name='upduty'),
    path('deleduty/<int:id>/',adminview.deleduty,name='deleduty'),


    path('addexamresult',adminview.addexamresult,name='addexamresult'),
    path('examresultview',adminview.examresultview,name='examresultview'),
    path('upexamresult/<int:id>/',adminview.upexamresult,name='upexamresult'),
    path('deleexamresult/<int:id>/',adminview.deleexamresult,name='deleexamresult'),



    path('addstaffmeeting',adminview.addstaffmeeting,name='addstaffmeeting'),
    path('staffmeetingview',adminview.staffmeetingview,name='staffmeetingview'),
    path('upstaffmeeting/<int:id>/',adminview.upstaffmeeting,name='upstaffmeeting'),
    path('delestaffmeeting/<int:id>/',adminview.delestaffmeeting,name='delestaffmeeting'),


    path('addparentsmeeting',adminview.addparentsmeeting,name='addparentsmeeting'),
    path('parentsmeetingview',adminview.parentsmeetingview,name='parentsmeetingview'),
    path('upparentsmeeting/<int:id>/',adminview.upparentsmeeting,name='upparentsmeeting'),
    path('deleparentsmeeting/<int:id>/',adminview.deleparentsmeeting,name='deleparentsmeeting'),

    path('addcommunitygroup',adminview.addcommunitygroup,name='addcommunitygroup'),
    path('admincommunitygroupview',adminview.admincommunitygroupview,name='admincommunitygroupview'),
    path('upcommunitygroup/<int:id>/',adminview.upcommunitygroup,name='upcommunitygroup'),
    path('delecommunitygroup/<int:id>/',adminview.delecommunitygroup,name='delecommunitygroup'),
    path('managecommunitygroup',adminview.managecommunitygroup,name='managecommunitygroup'),
    path('appointment_admin',adminview.appointment_admin,name='appointment_admin'),
    path('approve_appointment/<int:id>/',adminview.approve_appointment,name='approve_appointment'),
    path('reject_appointment/<int:id>/',adminview.reject_appointment,name='reject_appointment'),


    path('tsyllabusview',teacherview.tsyllabusview,name='tsyllabusview'),
    path('texamtableview',teacherview.texamtableview,name='texamtableview'),
    path('ttimetableview',teacherview.ttimetableview,name='ttimetableview'),
    path('tparentsmeetingview',teacherview.tparentsmeetingview,name='tparentsmeetingview'),


    path('addstudymaterial',teacherview.addstudymaterial,name='addstudymaterial'),
    path('studymaterialview',teacherview.studymaterialview,name='studymaterialview'),
    path('upstudymaterial/<int:id>/',teacherview.upstudymaterial,name='upstudymaterial'),
    path('delestudymaterial/<int:id>/',teacherview.delestudymaterial,name='delestudymaterial'),


    path('addmark',teacherview.addmark,name='addmark'),
    path('markview',teacherview.markview,name='markview'),
    path('upmark/<int:id>/',teacherview.upmark,name='upmark'),
    path('delemark/<int:id>/',teacherview.delemark,name='delemark'),

    path('texamresultview',teacherview.texamresultview,name='texamresultview'),
    path('join_community/<int:id>/',teacherview.join_community,name='join_community'),
    path('appointment_view',teacherview.appointment_view,name='appointment_view'),


    path('ssyllabusview',studentview.ssyllabusview,name='ssyllabusview'),
    path('sexamtableview',studentview.sexamtableview,name='sexamtableview'),
    path('stimetableview',studentview.stimetableview,name='stimetableview'),
    path('sstudymaterialview',studentview.sstudymaterialview,name='sstudymaterialview'),
    path('smarkview',studentview.smarkview,name='smarkview'),
    path('sexamresultview',studentview.sexamresultview,name='sexamresultview'),

    path('addnote',studentview.addnote,name='addnote'),
    path('noteview',studentview.noteview,name='noteview'),
    path('upnote/<int:id>/',studentview.upnote,name='upnote'),
    path('delenote/<int:id>/',studentview.delenote,name='delenote'),


    path('addcomplaint',studentview.addcomplaint,name='addcomplaint'),
    path('complaintview',studentview.complaintview,name='complaintview'),
    path('upcomplaint/<int:id>/',studentview.upcomplaint,name='upcomplaint'),
    path('delecomplaint/<int:id>/',studentview.delecomplaint,name='delecomplaint'),


]