from django.shortcuts import render, get_object_or_404
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.http import Http404

#def index(request):
#    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    #context = {'latest_question_list': latest_question_list}
#    return render(request, 'index.html')



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

#def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)
#
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)
#
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")