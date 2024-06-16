from .import views
from django.urls import path
from .views import (RegisterEmployeeView,JobListingsView, RegisterEmployerView, LoginView, LogoutView, UploadResumeView, EmployerDashboardView, ManageProfileView, ViewApplicationsView,)
from django.views.generic import TemplateView


app_name = 'accounts'

urlpatterns = [
    path('employee/register/', RegisterEmployeeView.as_view(), name='register_employee'),
    path('employer/register/', RegisterEmployerView.as_view(), name='register_employer'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('job_seeker/dashboard/', views.JobSeekerDashboardView.as_view(), name='job_seeker_dashboard'),
    path('employer/dashboard/', views.EmployerDashboardView.as_view(), name='employer_dashboard'),
    path('upload_resume/', UploadResumeView.as_view(), name='upload_resume'),
    path('job_listings/', JobListingsView.as_view(), name='job_listings'),
    path('manage_profile/', views.ManageProfileView.as_view(), name='manage_profile'),
    path('employer/view_job_listings/', JobListingsView.as_view(), name='view_job_listings'),
   #path('employer/post_job_opening/', TemplateView.as_view(template_name='post_job_opening.html'), name='post_job_opening'),
    path('employer/view_applications/', ViewApplicationsView.as_view(), name='view_applications'),
    path('employer/manage_company_profile/', TemplateView.as_view(template_name='coming_soon.html'), name='manage_company_profile'),
]


        