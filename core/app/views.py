from django.shortcuts import render

def home(request):
    return render(request=request, template_name='home.html')

def question(request, id):
    if request.method == 'GET':
        data = {}
        return render(request=request, template_name='question.html', context=data)
    if request.method == 'POST':
        data = {}
        return render(request=request, template_name='question.html', content=data)
