
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views, Hod_views, Student_views, Staff_views

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    path("base/", views.BASE, name="base"),
    path("", views.LOGIN, name="login"),
    path("doLogin/", views.doLogin, name="doLogin"),
    path("doLogout/", views.doLogout, name="logout"),
    path("Hod/Home/", Hod_views.HOME, name="hod_home"),
    path("Profile/", views.PROFILE, name="profile"),
    path("Profile/update/", views.PROFILE_UPDATE, name="profile_update"),
    
    # HOD Student
    path("Hod/Student/Add/", Hod_views.ADD_STUDENT, name="add_student"),
    path("Hod/Student/View/", Hod_views.VIEW_STUDENT, name="view_student"),
    path("Hod/Student/Edit/<str:id>", Hod_views.EDIT_STUDENT, name="edit_student"),
    path("Hod/Student/Update/", Hod_views.UPDATE_STUDENT, name="update_student"),
    path("Hod/Student/Delete/<str:admin>",Hod_views.DELETE_STUDENT,name="delete_student"),
    path("Hod/Student/Send_Notification", Hod_views.STUDENT_SEND_NOTIFICATION, name="student_send_notification"),
    path("Hod/Student/Save_Notification", Hod_views.SAVE_STUDENT_NOTIFICATION, name="save_student_notification"),
    path("Hod/Student/View_Leave", Hod_views.STUDENT_LEAVE_VIEW, name="hod_student_leave"),
    path("Hod/Student/Approve_Leave/<str:id>", Hod_views.APPROVE_STUDENT_LEAVE, name="approve_student_leave"),
    path("Hod/Student/Disapprove_Leave/<str:id>", Hod_views.DISAPPROVE_STUDENT_LEAVE, name="disapprove_student_leave"),
    path("Hod/Student/Feedback", Hod_views.STUDENT_FEEDBACK, name="student_feedback_reply"),
    path("Hod/Student/Feedback/Save", Hod_views.STUDENT_FEEDBACK_SAVE, name="student_feedback_reply_save"),
    # HOD Course
    path("Hod/Course/Add", Hod_views.ADD_COURSE, name="add_course"),
    path("Hod/Course/View", Hod_views.VIEW_COURSE, name="view_course"),
    path("Hod/Course/Edit/<str:id>", Hod_views.EDIT_COURSE, name="edit_course"),
    path("Hod/Course/Update", Hod_views.UPDATE_COURSE, name="update_course"),
    path("Hod/Course/Delete/<str:id>", Hod_views.DELETE_COURSE, name="delete_course"),
    # HOD Staff
    path("Hod/Staff/Add", Hod_views.ADD_STAFF, name="add_staff"),
    path("Hod/Staff/View", Hod_views.VIEW_STAFF, name="view_staff"),
    path("Hod/Staff/Edit/<str:id>", Hod_views.EDIT_STAFF, name="edit_staff"),
    path("Hod/Staff/Update", Hod_views.UPDATE_STAFF, name="update_staff"),
    path("Hod/Staff/Delete/<str:admin>", Hod_views.DELETE_STAFF, name="delete_staff"),
    path("Hod/View_Attendance", Hod_views.HOD_VIEW_ATTENDANCE, name="hod_view_attendance"),
    path("Hod/Staff/Send_Notification",Hod_views.STAFF_SEND_NOTIFICATION,name="staff_send_notification"),
    path("Hod/Staff/Save_Notification", Hod_views.SAVE_STAFF_NOTIFICATION, name="save_staff_notification"),
    path("Hod/Staff/View_Leave", Hod_views.STAFF_LEAVE_VIEW, name="hod_staff_leave"),
    path("Hod/Staff/Approve_Leave/<str:id>", Hod_views.APPROVE_STAFF_LEAVE, name="approve_staff_leave"),
    path("Hod/Staff/Disapprove_Leave/<str:id>", Hod_views.DISAPPROVE_STAFF_LEAVE, name="disapprove_staff_leave"),
    path("Hod/Staff/Feedback", Hod_views.STAFF_FEEDBACK, name="staff_feedback_reply"),
    path("Hod/Staff/Feedback/Save", Hod_views.STAFF_FEEDBACK_SAVE, name="staff_feedback_reply_save"), 
    # HOD Subjects
    path("Hod/Subject/Add", Hod_views.ADD_SUBJECT, name="add_subject"),
    path("Hod/Subject/View", Hod_views.VIEW_SUBJECT, name="view_subject"),
    path("Hod/Subject/Edit/<str:id>", Hod_views.EDIT_SUBJECT, name="edit_subject"),
    path("Hod/Subject/Update>", Hod_views.UPDATE_SUBJECT, name="update_subject"),
    path("Hod/Subject/Delete/<str:id>", Hod_views.DELETE_SUBJECT, name="delete_subject"),
    # HOD Session
    path("Hod/Session/Add", Hod_views.ADD_SESSION, name="add_session"),
    path("Hod/Session/View", Hod_views.VIEW_SESSION, name="view_session"),
    path("Hod/Session/Edit/<str:id>", Hod_views.EDIT_SESSION, name="edit_session"),
    path("Hod/Session/Update>", Hod_views.UPDATE_SESSION, name="update_session"),
    path("Hod/Session/Delete/<str:id>", Hod_views.DELETE_SESSION, name="delete_session"),


    # STAFF urls
    path("Staff/Home", Staff_views.HOME, name="staff_home"),
    path("Staff/Notification", Staff_views.NOTIFICATION, name="staff_notification"),
    path("Staff/Mark_as_read<str:id>", Staff_views.MARK_AS_READ, name="mark_as_read"),
    path("Staff/Leave", Staff_views.STAFF_LEAVE, name="staff_leave"),
    path("Staff/Save_Leave", Staff_views.SAVE_STAFF_LEAVE, name="save_staff_leave"),
    path("Staff/Feedback", Staff_views.STAFF_FEEDBACK, name="staff_feedback"),
    path("Staff/Feedback/Save", Staff_views.SAVE_STAFF_FEEDBACK, name="save_staff_feedback"),
    path("Staff/Take_Attendance", Staff_views.STAFF_TAKE_ATTENDANCE, name="staff_take_attendance"),
    path("Staff/Save_Attendance", Staff_views.STAFF_SAVE_ATTENDANCE, name="staff_save_attendance"),
    path("Staff/View_Attendance", Staff_views.STAFF_VIEW_ATTENDANCE, name="staff_view_attendance"),
    path("Staff/Add/Result", Staff_views.STAFF_ADD_RESULT, name="staff_add_result"),
    path("Staff/Save/Result", Staff_views.STAFF_SAVE_RESULT, name="staff_save_result"),


    # STUDENT urls
    path("Student/Home", Student_views.HOME, name="student_home"),
    path("Student/Notifications", Student_views.STUDENT_NOTIFICATION, name="student_notification"),
    path("Student/Mark_As_done/<str:id>", Student_views.STUDENT_NOTIFICATION_MARK_AS_DONE, name="student_notification_mark_as_done"),
    path("Student/Feedback", Student_views.STUDENT_FEEDBACK, name="student_feedback"),
    path("Student/Leave", Student_views.STUDENT_LEAVE, name="student_leave"),
    path("Student/Save_Leave", Student_views.SAVE_STUDENT_LEAVE, name="save_student_leave"),
    path("Student/Feedback/Save", Student_views.SAVE_STUDENT_FEEDBACK, name="save_student_feedback"),
    path("Student/View_Attendance", Student_views.STUDENT_VIEW_ATTENDANCE, name="student_view_attendance"),
    path("Student/View_Result", Student_views.STUDENT_VIEW_RESULT, name="student_view_result"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
