from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import (
    Course,
    CustomUser,
    Staff,
    Student,
    Subject,
    Student_Notification,
    Student_Feedback,
    Student_Leave,
    Attendance_Report,
    Student_Result
)
from django.contrib import messages

@login_required(login_url="/")
def HOME(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()

    student_gender_male = Student.objects.filter(gender="Male").count()
    student_gender_female = Student.objects.filter(gender="Female").count()
    context = {
        "student_count": student_count,
        "staff_count": staff_count,
        "course_count": course_count,
        "subject_count": subject_count,
        "student_gender_male": student_gender_male,
        "student_gender_female": student_gender_female,
    }

    return render(request, "Hod/home.html", context)

@login_required(login_url="/")
def STUDENT_NOTIFICATION(request):
    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id = i.id
        notification = Student_Notification.objects.filter(student_id=student_id)
        context = {
            'notification':notification,
        }
    return render(request, 'Student/notification.html', context)

@login_required(login_url="/")
def STUDENT_NOTIFICATION_MARK_AS_DONE(request, id):
    notification = Student_Notification.objects.get(id=id)
    notification.status = 1
    notification.save()
    return redirect('student_notification')

@login_required(login_url="/")
def STUDENT_LEAVE(request):
    student = Student.objects.get(admin=request.user.id)
    student_leave_history = Student_Leave.objects.filter(student_id=student.id)
    context = {"student_leave_history": student_leave_history}

    return render(request, "Student/apply_leave.html", context)

@login_required(login_url="/")
def SAVE_STUDENT_LEAVE(request):
    if request.method == "POST":
        message = request.POST.get("leave_message")
        date = request.POST.get("leave_date")
        student = Student.objects.get(admin=request.user.id)

        leave = Student_Leave(student_id=student, date=date, message=message)
        leave.save()
        messages.success(request, "Applicaton SuccessFully Sent!!")
        return redirect("student_leave")

@login_required(login_url="/")
def STUDENT_FEEDBACK(request):
    student = Student.objects.get(admin=request.user.id)
    student_feedback = Student_Feedback.objects.filter(student_id=student.id)
    context = {"student_feedback": student_feedback}
    return render(request, "Student/feedback.html", context)

@login_required(login_url="/")
def SAVE_STUDENT_FEEDBACK(request):
    if request.method == "POST":
        feedback = request.POST.get("feedback")
        student = Student.objects.get(admin=request.user.id)

        student_feedback = Student_Feedback(
            student_id=student, feedback=feedback, feedback_reply=""
        )
        student_feedback.save()
        messages.success(request, "Feedback SuccessFully Sent!!")
        return redirect("student_feedback")

@login_required(login_url="/")
def STUDENT_VIEW_ATTENDANCE(request):
    student = Student.objects.get(admin=request.user.id)
    subjects = Subject.objects.filter(course=student.course_id)
    action = request.GET.get("action")
    get_subject = None
    attendance_report = None

    if request.method == "POST":
        subject_id = request.POST.get("subject_id")
        get_subject = Subject.objects.get(id=subject_id)

        attendance_report = Attendance_Report.objects.filter(attendance_id__subject_id=subject_id,student_id=student)

    context = {
        "subjects": subjects,
        "get_subject": get_subject,
        "attendance_report": attendance_report,
        "action": action,
    }

    return render(request, "Student/view_attendance.html", context)

@login_required(login_url="/")
def STUDENT_VIEW_RESULT(request):
    student = Student.objects.get(admin=request.user.id)
    results = Student_Result.objects.filter(student_id = student)

    context = {
        "results":results
    }

    return render(request, "Student/view_result.html", context)
