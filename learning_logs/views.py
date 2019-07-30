from django.shortcuts import render

# Create your views here.
# try
# sdfg
def index(request):
    return render(request, 'learning_logs/index.html')