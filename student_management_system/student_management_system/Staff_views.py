from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import (
    Course,
    Session_Year,
    CustomUser,
    Student,
    Staff,
    Subject,
    Staff_Notification,
    Staff_Leave,
    Staff_Feedback,
    Attendance,
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
def NOTIFICATION(request):
    staff = Staff.objects.get(admin=request.user.id)
    notification = Staff_Notification.objects.filter(staff_id=staff.id)
    context = {"notification": notification}
    return render(request, "Staff/Notification.html", context)


@login_required(login_url="/")
def MARK_AS_READ(request, id):
    notification = Staff_Notification.objects.get(id=id)
    notification.status = 1
    notification.save()
    return redirect("notification")


@login_required(login_url="/")
def STAFF_LEAVE(request):
    staff = Staff.objects.get(admin=request.user.id)
    staff_leave_history = Staff_Leave.objects.filter(staff_id=staff.id)
    context = {"staff_leave_history": staff_leave_history}

    return render(request, "Staff/apply_leave.html", context)


@login_required(login_url="/")
def SAVE_STAFF_LEAVE(request):
    if request.method == "POST":
        message = request.POST.get("leave_message")
        date = request.POST.get("leave_date")
        staff = Staff.objects.get(admin=request.user.id)

        leave = Staff_Leave(staff_id=staff, date=date, message=message)
        leave.save()
        messages.success(request, "Applicaton SuccessFully Sent!!")
        return redirect("staff_leave")


@login_required(login_url="/")
def STAFF_FEEDBACK(request):
    staff = Staff.objects.get(admin=request.user.id)
    staff_feedback = Staff_Feedback.objects.filter(staff_id=staff.id)
    context = {"staff_feedback": staff_feedback}
    return render(request, "Staff/feedback.html", context)


@login_required(login_url="/")
def SAVE_STAFF_FEEDBACK(request):
    if request.method == "POST":
        feedback = request.POST.get("feedback")
        staff = Staff.objects.get(admin=request.user.id)

        staff_feedback = Staff_Feedback(
            staff_id=staff, feedback=feedback, feedback_reply=""
        )
        staff_feedback.save()
        messages.success(request, "Feedback SuccessFully Sent!!")
        return redirect("staff_feedback")


@login_required(login_url="/")
def STAFF_TAKE_ATTENDANCE(request):
    staff = Staff.objects.get(admin=request.user.id)
    subjects = Subject.objects.filter(staff=staff)
    session_year = Session_Year.objects.all()
    action = request.GET.get("action")
    get_subject = None
    get_session_year = None
    students = None

    if request.method == "POST":
        session_year_id = request.POST.get("session_year_id")
        subject_id = request.POST.get("subject_id")

        get_subject = Subject.objects.get(id=subject_id)
        get_session_year = Session_Year.objects.get(id=session_year_id)

        course_id = get_subject.course.id
        students = Student.objects.filter(course_id=course_id, session_year_id = session_year_id)

    context = {
        "subjects": subjects,
        "students": students,
        "session_year": session_year,
        "get_subject": get_subject,
        "get_session_year": get_session_year,
        "action": action,
    }

    return render(request, "Staff/take_attendance.html", context)


@login_required(login_url="/")
def STAFF_SAVE_ATTENDANCE(request):
    if request.method == "POST":
        session_year_id = request.POST.get("session_year_id")
        subject_id = request.POST.get("subject_id")
        attendance_date = request.POST.get("attendance_date")
        get_subject = Subject.objects.get(id=subject_id)
        get_session_year = Session_Year.objects.get(id=session_year_id)
        student_id = request.POST.getlist("student_id")

        if len(Attendance.objects.filter(subject_id=get_subject,
            attendance_date=attendance_date,
            session_year_id=get_session_year)) == 0:
        
            attendance = Attendance(
                subject_id=get_subject,
                attendance_date=attendance_date,
                session_year_id=get_session_year,
            )
            attendance.save()
            messages.success(request, "Attendance Successfully Marked!!")
        
        else:
            attendance = Attendance.objects.get(subject_id=get_subject,
            attendance_date=attendance_date,
            session_year_id=get_session_year)
            messages.success(request, "Attendance Successfully Updated!!")
        
        if len(Attendance_Report.objects.filter(attendance_id=attendance)) != 0:
            Attendance_Report.objects.filter(attendance_id=attendance).delete()

        for i in student_id:
            stud = Student.objects.get(id=int(i))
            attendance_report = Attendance_Report(
                student_id=stud, attendance_id=attendance
            )
            attendance_report.save()

    return redirect("staff_take_attendance")

@login_required(login_url="/")
def STAFF_VIEW_ATTENDANCE(request):
    staff = Staff.objects.get(admin=request.user.id)
    subjects = Subject.objects.filter(staff=staff)
    session_year = Session_Year.objects.all()
    action = request.GET.get("action")
    get_subject = None
    get_session_year = None
    attendance_report = None
    attendance_date = None

    if request.method == "POST":
        session_year_id = request.POST.get("session_year_id")
        subject_id = request.POST.get("subject_id")
        attendance_date = request.POST.get("attendance_date")

        get_subject = Subject.objects.get(id=subject_id)
        get_session_year = Session_Year.objects.get(id=session_year_id)

        attendance = Attendance.objects.filter(
            session_year_id=session_year_id,
            subject_id=subject_id,
            attendance_date=attendance_date,
        )
        for i in attendance:
            attendance_report = Attendance_Report.objects.filter(attendance_id = i.id)

    context = {
        "subjects": subjects,
        "session_year": session_year,
        "get_subject": get_subject,
        "get_session_year": get_session_year,
        "attendance_date":attendance_date,
        "attendance_report": attendance_report,
        "action": action,
    }

    return render(request, "Staff/view_attendance.html", context)

@login_required(login_url="/")
def STAFF_ADD_RESULT(request):
    staff = Staff.objects.get(admin=request.user.id)
    subjects = Subject.objects.filter(staff=staff)
    session_year = Session_Year.objects.all()
    action = request.GET.get("action")

    get_subject = None
    get_session_year = None
    students = None

    if request.method == "POST":
        session_year_id = request.POST.get("session_year_id")
        subject_id = request.POST.get("subject_id")

        get_subject = Subject.objects.get(id = subject_id)
        get_session_year = Session_Year.objects.get(id=session_year_id)

        students = Student.objects.filter(course_id = get_subject.course, session_year_id = session_year_id)

    context = {
        "subjects": subjects,
        "students": students,
        "session_year": session_year,
        "get_subject": get_subject,
        "get_session_year": get_session_year,
        "action": action,
    }

    return render(request, "Staff/add_result.html", context)

@login_required(login_url="/")
def STAFF_SAVE_RESULT(request):
    if request.method == "POST":
        subject_id = request.POST.get("subject_id")
        practical_marks = request.POST.get("practical_marks")
        theory_marks = request.POST.get("theory_marks")
        student_id = request.POST.get("student_id")
        get_student = Student.objects.get(id = student_id)        
        get_subject = Subject.objects.get(id = subject_id)

        if len(Student_Result.objects.filter(subject_id=get_subject,
            student_id=student_id)) == 0:
        
            result = Student_Result(
                student_id=get_student,
                subject_id=get_subject,
                practical_marks=practical_marks,
                theory_marks=theory_marks
            )
            result.save()
            messages.success(request, "Marks Successfully Added!!")
        
        else:
            result = Student_Result.objects.get(subject_id=get_subject,
            student_id=student_id)
            result.practical_marks = practical_marks
            result.theory_marks = theory_marks
            result.save()
            messages.success(request, "Marks Successfully Updated!!")
  
    return redirect("staff_add_result")
