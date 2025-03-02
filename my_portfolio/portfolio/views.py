from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings
from .models import Project,Skill,CV,Testimonials

def home(request):
    skills=Skill.objects.all()
    testimonials=Testimonials.objects.all()
    cv=CV.objects.first()
    context={
        "skills":skills,
        "cv":cv,
        "testimonials":testimonials
    }
    return render(request,"portfolio/index.html",context)

def about(request):

    experiences=[
        {
            "job_title":"IT support intern",
            "company":"Tourism Fund(TF)",
            "years":"2024(May-August)",
            "description":"Worked as an Information technology intern by providing services to the institution.",
            "skills":["Cybersecurity Basics","Database Management","Hardware and Software Installation"]
        },
        {
            "job_title": "Software Developer",
            "company": "Tech Solutions Ltd",
            "years": "2024 - Present",
            "description": "Developed and maintained full-stack e-commerce application using Django and React.",
            "skills":["Django", "React", "PostgreSQL", "REST APIs", "Database"]
        },

        {
            "job_title": "Backend Developer Intern",
            "company": "AI Innovations",
            "years": "2025",
            "description": "Worked on AI-driven backend services, optimizing database performance.",
            "skills": ["Python","Django","Tailwind CSS","Customer support","System Design"]
        },
        {
            "job_title":"IT support intern",
            "company":"Kenya ports Authority",
            "years":"2024(May-August)",
            "description":"Conducted my attachment as an IT support where i gained valuable expereince for the three months.",
            "skills":["Technical Support", "Network Troubleshooting", "Help Desk Support", "System Maintenance"]
        }
    ]
    certifications=[
            {"name": "Django Web Development", "organization": "Udemy", "year": "2023"},
            {"name": "PostgreSQL", "organization": "W3 Schools", "year": "2025"},
            {"name": "Full-Stack Development", "organization": "Google", "year": "2024"},
            {"name": "Certified in Cybersecurity", "organization": "ISC2", "year": "2024"},
    ]
    context={
        "experiences":experiences,
        "certifications":certifications,
    }
    return render(request,"portfolio/about.html",context)  
    #Uploading my Cv  

def projects(request):
    projects=Project.objects.all()
    context={
        "projects":projects,
    }
    return render(request,"portfolio/projects.html",context)

def contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            #send an email notification
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f"New Message from {name}"
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            send_mail(subject, email_message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])

            return redirect('portfolio:contact_success') 
    else:
        form = ContactForm()
    return render(request,"portfolio/contact.html")

def contact_success(request):
    return render(request, 'portfolio/contact_success.html')