"""SDRF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from SDRFAPP import views
from rest_framework.routers import DefaultRouter
router =DefaultRouter()

#regsiter studentvieset with routre

#router.register('studenapi',views.StudentViewSet,basename='student'),
#router.register('studenapi',views.StudenModeltViewSet,basename='student'),
router.register('studenapi',views.StudenReadOnlyModeltViewSet,basename='student'),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studinfo/<int:pk>',views.StudentDetails),#this url helps to get single data
    path('studinfo/',views.StudentDetailsList),#this one by all data
    path('studcreate/', views.StudentCreate),
    path('studapi/', views.student_api),
    path('staffapi/', views.StaffAPI.as_view()),
    path('empapi/', views.EmployeeCreate),
    path('EmployeeAPI/', views.EmployeeAPI),
    path('EmployeeAPI/<int:pk>', views.EmployeeAPI),
    path('EmployeeAPIView/', views.EmployeeAPIView.as_view()),
    path('EmployeeAPIView/<int:pk>', views.EmployeeAPIView.as_view()),
    # path('studentapi/',views.StudentList.as_view()),
    # path('studentapi/',views.StudentCreate.as_view()),
    # path('studentapi/<int:pk>',views.StudentRetrieve.as_view()),
    # path('studentapi/<int:pk>',views.StudentUpdate.as_view()),
    # path('studentapi/<int:pk>',views.StudentDestroy.as_view()),
    # path('studentapi/',views.StudentListCreateAPIVIEW.as_view()),
    # path('studentapi/<int:pk>',views.StudentUDRAPIVIEW.as_view()),
    # path('studentapi/',views.studList.as_view()),
    # path('studentapi/',views.studCreateList.as_view()),
    # path('studentapi/<int:pk>',views.studRetrieveList.as_view()),
    # path('studentapi/<int:pk>',views.studUpdateList.as_view()),
    path('studentapi/<int:pk>', views.studDestroyList.as_view()),
    path('api/',include(router.urls)),

]
