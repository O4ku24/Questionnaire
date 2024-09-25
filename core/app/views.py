from django.shortcuts import render

def home(request):
    return render(request=request, template_name='home.html')

def question(request, id):
    if request.method == 'GET':
        data = {f'quest{id}':['var1', 'var2', 'var3']}
        return render(request=request, template_name='question.html', context=data)
    if request.method == 'POST':
        data = {f'quest{id}':['var1', 'var2', 'var3']}
        return render(request=request, template_name='question.html', content=data)
