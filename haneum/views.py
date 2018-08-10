from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import Http404
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from .models import Company, Report

'''
def search(request):
    # 백엔드 작업 수행
    
    # 데이터베이스 검색
    try:
        question = Question.objects.get(pk=parameter)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    
    # 또는 단축 함수를 사용하여
    question = get_object_or_404(Question, pk=question_id)
    
    # 템플릿 설정
    template = loader.get_template('haneum/search.html')
    # 템플릿 전달 인자 및 전달 값 설정
    context = {
        'question': question,
    }
    return HttpResponse(template.render(context, request))
    
    # 또는 redirect 처리
    return HttpResponse(reverse( 'haneum:articles', 
                                args=(company.company_name,) ))
'''

@csrf_exempt
def search(request):
    # 백엔드 작업 수행
    
    # 템플릿 전달 인자 및 전달 값 설정
    context = {
        "msg": "This is search, project start",
    }
    # 템플릿 설정
    return render(request, 'haneum/search.html', context)

def articles(request):
    
    
    
    context = {
        "company_name": request.POST["company_name"],
    }
    return render(request, 'haneum/articles.html', context)

def analytics(request):
    
    
    
    context = {
        "company_no": "",
    }
    return render(request, 'haneum/analytics.html', context)

def prediction(request):
    
    
    
    context = {
        "company_no": "",
    }
    return render(request, 'haneum/prediction.html', context)
