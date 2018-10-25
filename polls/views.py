from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Question, Choice
from django.utils import timezone


def result(request, id):
    question = Question.objects.get(pk = id)
    return render(request, 'polls/result.html', {'question': question})







def input(request):
    return render(request, 'polls/input.html', {})

def puut(request, id):
    que = Question.objects.get(id = id)
    return render(request, '', {})


def add_question(request):
    text = request.POST['text']
    # q = Question(
    #     question_text = text,
    #     pub_date=timezone.now())
    # q.save()
    # return render(request, 'polls/add.html', {})
    return HttpResponse('입력완료')



def data(request, email, number):     #<!--데이터가 넘어간디야~~~-->
   #http://localhost:8000/polls/data?user_name=kim (GET방식)
    value = request.GET['user_name']    # ? 형식

    return HttpResponse(value + email + str(number))

def vote(request):
    choice = request.POST['choice']
    c = Choice.objects.get(pk=choice)
    c.votes = c.votes + 1
    c.save()

    return render(
        request,
        'polls/vote.html',
        {}
    )

def index(request):
    list = Question.objects.all()

    return render(
        request, 'polls/index.html',
        {'question' : list})
        #넘길때 이름(키) : 내용

          # 템플릿을 부르면서 질문을 줘야함
# Create your views here.

# polls의 url
def detail(request, id):
    question = Question.objects.get(id=id)
    return render(request, 'polls/detail.html', {'item' : question})
