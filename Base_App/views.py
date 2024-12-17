from django.shortcuts import render

# Create your views here.
def HomeView(request):
    return render(request, 'home.html')

def AboutView(request):
    return render(request, 'about_next.html')

def TaskManagementView(request):
    return render(request, 'task_next.html')

def HelpDeskView(request):
    return render(request, 'home.html')