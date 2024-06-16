# Job Portal Project

This is a web application built with Django.it is designed to serve a job portal for both job seekers and employers

## Features
- User Registration: Allows users to Register as either job seekers or employers
-User Authentication: Provide secure login and logout functionality for registered users
-Dashboard: Offers personalized dashboards for job seekers and employers ,displaying relevant information and actions
-Job Listings: Displays a list of job openings available for application.its a feature that is both on the employers and job seeker dashboard
- Upload resume: Here the job seekers are allowed to upload their resumes for the job they want to apply
- Manage profile: Its a feature on the job seekers dashboard that allows the job seekers to manage their profile 
- View application: Here the employer is in a position to view who applied for the job at at what has been apllied and by who, they can even view the resumes uploaded.

### Installation
- Clone the repository:Clone the repository to your local machine using 'git clone'

-Install Dependencies: Navigate to the project directory and install the required dependencies using pip install -r requirements.txt.

- Database Setup: Configure your database settings in settings.py and run database migrations using python manage.py migrate.

- Run the Development Server: Start the Django development server using python manage.py runserver.

- Access the Application: Open your web browser and go to http://localhost:8000 to access the application.

## Usage

### User Registration
- **Job Seekers:** Register at `/accounts/employee/register/`
- **Employers:** Register at `/accounts/employer/register/`

### Login

- Login at `/accounts/login/`

### Dashboard

- **Job Seekers:** After login, navigate to `/accounts/job_seeker/dashboard/`
- **Employers:** After login, navigate to `/accounts/employer/dashboard/`

### Job Listings

- View job listings at `/accounts/job_listings/`

### Manage Profile

- Manage your profile at `/accounts/manage_profile/`

### Upload Resume

- Job seekers can upload their resume at `/accounts/upload_resume/`

## Models

- `User`: Custom user model with additional fields `is_job_seeker` and `is_employer`.
- `JobSeekerProfile`: Profile model for job seekers with fields like `resume`, `id_number`, and `passport_picture`.
- `EmployerProfile`: Profile model for employers with fields like `company_name`, `description`, `id_number`, and `passport_picture`.
- `Company`: Model to store company details.
- `Job`: Model to store job listings.
- `Application`: Model to store job applications.

## Forms

- `EmployeeRegistrationForm`: Form for registering job seekers.
- `EmployerRegistrationForm`: Form for registering employers.
- `UserLoginForm`: Form for user login.
- `YourProfileForm`: Form for managing user profiles.

## Views

- `RegisterEmployeeView`: Handles registration for job seekers.
- `RegisterEmployerView`: Handles registration for employers.
- `LoginView`: Handles user login.
- `LogoutView`: Handles user logout.
- `JobSeekerDashboardView`: Dashboard for job seekers.
- `EmployerDashboardView`: Dashboard for employers.
- `UploadResumeView`: Handles resume upload for job seekers.
- `JobListingsView`: Displays job listings.
- `ManageProfileView`: Allows users to manage their profile.
- `ViewApplicationsView`: Allows users to view job applications.

## URLs

- `/accounts/employee/register/`: Register as a job seeker
- `/accounts/employer/register/`: Register as an employer
- `/accounts/login/`: Login
- `/accounts/logout/`: Logout
- `/accounts/job_seeker/dashboard/`: Job seeker dashboard
- `/accounts/employer/dashboard/`: Employer dashboard
- `/accounts/upload_resume/`: Upload resume
- `/accounts/job_listings/`: View job listings
- `/accounts/manage_profile/`: Manage profile

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request

