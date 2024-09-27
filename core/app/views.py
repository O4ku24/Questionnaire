from django.shortcuts import render
from .models import Questions, Users

def home(request):
    return render(request=request, template_name='home.html')

def question(request):

    if request.method == 'GET':
        data = []
        questions_list = Questions.objects.all()
        for quest in questions_list:
            data.append({'text':quest.question, 'answers':[quest.answer1, quest.answer2, quest.answer3, quest.answer4]})
        print(data)
        return render(request=request, template_name='question.html', context={'questions': data})
    
    if request.method == 'POST':
        data = {}
        return render(request=request, template_name='question.html', content=data)
    
def root(request):

    if request.method == 'GET':
        data = []
        questions_list = Questions.objects.all()
        for quest in questions_list:
            data.append({'text':quest.question, 'answers':[quest.answer1, quest.answer2, quest.answer3, quest.answer4]})
        return render(request=request, template_name='root.html', context={'questions': data})

    if request.method == 'POST':
        data = {}
        return render(request=request, template_name='root', context=data)

def add_quest(request):

    if request.method == 'GET':
        return render(request=request, template_name='form_quest.html')
    
    if request.method == 'POST':
        questionText = request.POST.get('questionText')
        print(questionText)
        return render(request=request, template_name='form_quest.html')
