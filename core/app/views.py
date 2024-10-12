from django.shortcuts import render
from collections import defaultdict
from .models import Questions
from .stata import get_stata, add_stata

def home(request):
    return render(request=request, template_name='home.html')

def question_render(request):

    if request.method == 'GET':
        data = []
        questions_list = Questions.objects.all()
        for quest in questions_list:
            data.append({'text':quest.question, 
                         'answers':[quest.answer1, 
                                    quest.answer2, 
                                    quest.answer3, 
                                    quest.answer4]})
            
        return render(request=request, template_name='question.html', context={'questions': data})
    
    if request.method == 'POST':
        user_answer = {}
        name = request.POST.get("username") 
        answer_quest_list = request.POST.getlist('answer')
        user_answer['username'] = name
        user_answer['answer'] = defaultdict(list)
        for i in answer_quest_list:
            answer = i.split(', ')
            question = answer[0]
            response = answer[1]
            user_answer['answer'][question].append(response)  # Добавляем ответ к вопросу
        user_answer['answer'] = dict(user_answer['answer'])
        print(user_answer)

        return render(request=request, template_name='question.html')

        data = []
        questions_list = Questions.objects.all()
        for quest in questions_list:
            data.append({'text':quest.question, 
                         'answers':[quest.answer1, 
                                    quest.answer2, 
                                    quest.answer3, 
                                    quest.answer4]})
            
    
def root(request):

    if request.method == 'GET':
        data = []
        questions_list = Questions.objects.all()
        for quest in questions_list:
            
            data.append({'text':quest.question, 
                         'answers':[quest.answer1, 
                                    quest.answer2, 
                                    quest.answer3, 
                                    quest.answer4], 
                         'id_quest':quest.id})
            
        return render(request=request, template_name='root.html', context={'questions': data})

    if request.method == 'POST':

        return render(request=request, template_name='root.html', context=data)

def add_quest(request):

    if request.method == 'GET':
        return render(request=request, template_name='form_quest.html')
    
    if request.method == 'POST':

        quest = request.POST.get('question')
        answer1 = request.POST.get('answer1') 
        answer2 = request.POST.get('answer2') 
        answer3 = request.POST.get('answer3') 
        answer4 = request.POST.get('answer4') 

        Questions.objects.get_or_create(question = quest, 
                                        answer1 = answer1,
                                        answer2 = answer2,
                                        answer3 = answer3,
                                        answer4 = answer4)
        return render(request=request, template_name='form_quest.html')
    
def delete_quest(request, id_question):
    Questions.objects.get(id=id_question).delete()
    data = []
    questions_list = Questions.objects.all()
    for quest in questions_list:
        data.append({'text':quest.question, 
                     'answers':[quest.answer1, 
                                quest.answer2, 
                                quest.answer3, 
                                quest.answer4], 
                     'id_quest':quest.id})
    return render(request=request, template_name='root.html', context={'questions': data})

def statistik_render(request):
    if request.method == "GET":
        data = get_stata()
        print(data)
        return render(request=request, template_name='statistik.html')
