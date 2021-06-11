from django.urls import path

from . import views

urlpatterns = [
    path('base', views.base, name='base'),
    path("hrlogin", views.hrlogin, name="hrlogin"),
    path("hrdashboard", views.hrdashboard, name="hrdashboard"),
    path("employeeLogin", views.employeeLogin, name="employeeLogin"),
    path("empdashboard", views.empdashboard, name="empdashboard"),
    path("hrlogout", views.hrlogout, name="hrlogout"),
    path("employeeLogout", views.employeeLogout, name="employeeLogout"),
    path("team", views.team, name="team"),
    path("achievements", views.achievements, name="achievements"),
    path("adventures", views.adventures, name="adventures"),
    path("attendanceIn", views.attendanceIn, name="attendanceIn"),
    path("attendanceOut", views.attendanceOut, name="attendanceOut"),
    path("attendance", views.attendanceDetails, name="attendance"),
    path("HRattendance", views.HRAttendanceDetails, name="HRattendance")
]
