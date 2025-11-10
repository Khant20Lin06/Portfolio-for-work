from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .utils import alarm
from django.contrib import messages


# Create your views here.


def HomePage(request):
    Position = PositionModel.objects.all()
    Profile = ProfileModel.objects.all()
    skill = Skill.objects.all()
    Job = JobModel.objects.all()
    Introduce = IntroduceModel.objects.all()
    contact = Contact.objects.all()
    SkillM = SkillModel.objects.all()
    About = AboutModel.objects.all()
    experience = Experience.objects.all()
    Service = ServiceModel.objects.all()
    lg = Lg.objects.all()
    Skills = SkillsModel.objects.all()
    Project = ProjectModel.objects.all()
    feedback = Feedback.objects.all().order_by('-created_at')
    workExperience = WorkExperience.objects.all()
    education = Education.objects.all()
    
    context = {
        'Position': Position,
        'Profile': Profile,
        'skill': skill,
        'Job': Job,
        'Introduce': Introduce,
        'contact': contact,
        'SkillM': SkillM,
        'About': About,
        'experience': experience,
        'Service': Service,
        'lg': lg,
        'Skills': Skills,
        'Project': Project,
        'feedback': feedback,
        'workExperience': workExperience,
        'education': education,
    }
    return render(request, 'index.html', context)

def profile_list(request):
    profiles = ProfileModel.objects.all()
    return render(request, 'index.html', {'profiles': profiles})

def message(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if not name or not email:
            messages.error(request, "Please fill in all required fields.")
            return redirect("homePage")

        Message.objects.create(
            name=name,
            email=email,
            message=message,
        )

        messages.success(request, "Your message has been sended successfully!")
        return redirect("homePage")

    return render(request, "index.html")