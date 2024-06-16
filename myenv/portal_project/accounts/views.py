from django.db import IntegrityError
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages, auth
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView,TemplateView,ListView ,FormView, RedirectView
from .models import User,Application, Job, JobSeekerProfile
from .forms import YourProfileForm, UserLoginForm,EmployeeRegistrationForm, EmployerRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here
class RegisterEmployeeView(CreateView):
   
   model = User
   form_class = EmployeeRegistrationForm
   template_name = 'accounts/employee/register.html'
   success_url = reverse_lazy('accounts:login') #redirect to accounts login on been successful

   extra_context = {
        'title':'Register'
    }
   
   def get_queryset(self):
       return User.objects.none()
   
   def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            print('User is authenticated, redirecting to success URL')
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)
   
   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context
   
   def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            try:   
                user = form.save(commit=False)
                password = form.cleaned_data.get("password1")
                user.set_password(password)
                user.save()
                messages.success(request, 'Registration successful.Please log in.')           
                return redirect('accounts:login')
            except IntegrityError:
                form.add_error('username', 'Username already exists.')
        
        else:
            print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

           # return render(request, 'accounts/employee/register.html', {'form': form})
   def get_success_url(self):
       return self.success_url

class RegisterEmployerView(CreateView):
    model = User
    form_class = EmployerRegistrationForm
    template_name = 'accounts/employer/register.html'
    success_url = reverse_lazy('accounts:login')

    extra_context = {
        'title':'Register'
    }
    def get_queryset(self):
        return User.objects.none()
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                password = form.cleaned_data.get("password1")
                user.set_password(password)
                user.save()
                messages.success(request, 'Registration successful.Please log in.')
                return redirect('accounts:login')
            except IntegrityError:
                form.add_error('username', 'Username already exists.')
        
        else:
            print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

        
            #return render(request, 'accounts/employer/register.html', {'form': form})
        
    def get_success_url(self):
            return self.success_url
        
class LoginView(FormView):
    """provides the ability to login as a user with an email and a password"""
    success_url = '/'
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    extra_content = {
        'title': 'Login'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            print('User is authenticated, redirecting to success URL')
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)
    
    def get_success_url(self):
        if 'next' in self.request.GET and self.request.GET['next'] != '':
            print('Redirecting to next URL:', self.request.GET['next'])
            return self.request.GET['next']
        else:
            print('Redirecting to default success URL:', self.success_url)
            return self.success_url

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        if self.request.user.is_job_seeker:
            return HttpResponseRedirect(reverse('accounts:job_seeker_dashboard'))
        elif self.request.user.is_employer:
            return HttpResponseRedirect(reverse('accounts:employer_dashboard'))
        else:
            return HttpResponseRedirect(reverse('default_dashboard'))

    def form_invalid(self, form):
        """if the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))
    
    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        print("Login POST requested received")
        form = self.form_class(request.POST)
        print("Form instantiated")
        if form.is_valid():
            print("Form is valid")
            return self.form_valid(form)
        else:
            print("Form is invalid")
            return self.form_invalid(form)


class LogoutView(RedirectView):
    """provides users tyhe ability to logout"""
    url = reverse_lazy('accounts:login')

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)
    
class JobSeekerDashboardView(TemplateView):
    template_name = 'accounts/job_seeker_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class EmployerDashboardView(TemplateView):
    template_name = 'accounts/employer_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dashboard_url'] = reverse('accounts:employer_dashboard')
        return context
    
class UploadResumeView(CreateView):
    model = JobSeekerProfile
    fields = ['resume']
    template_name = 'accounts/upload_resume.html'
    success_url = reverse_lazy('accounts:job_seeker_dashboard')
    
    def form_valid(self, form):
        job_seeker_profile = JobSeekerProfile.objects.get(user=self.request.user)
        job_seeker_profile.resume = form.cleaned_data['resume']
        job_seeker_profile.save()
        messages.success(self.request, 'Resume uploaded successfully.')

        return super().form_valid(form)
    
    def get_object(self):
        return JobSeekerProfile.objects.get(user=self.request.user)
    
class JobListingsView(ListView):
    model = Job
    template_name = 'accounts/job_listings.html'
    context_object_name = 'jobs'

class ManageProfileView(TemplateView):
    template_name = 'accounts/manage_profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            form = YourProfileForm(self.request.POST)
            if form.is_valid():
                user = self.request.user
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.email = form.cleaned_data['email']
                user.save()

                # Assuming you have a UserProfile model to store additional details
                user_profile, _ = JobSeekerProfile.objects.get_or_create(user=user)
                user_profile.id_number = form.cleaned_data['id_number']
                user_profile.passport_picture = form.cleaned_data['passport_picture']
                user_profile.save()

                # Redirect to some success URL or render a success message
                return redirect('success_url')
                pass
            else:
                context['form'] = form
                return context
        else:
            form = YourProfileForm()
            context['form'] = form
            return context

class ViewApplicationsView(LoginRequiredMixin, ListView):
    model = Application 
    template_name = 'accounts/view_applications.html'
    context_object_name = 'applications'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Application.objects.filter(applicant=self.request.user)
        else:
            return Application.objects.none()
    