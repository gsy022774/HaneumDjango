from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

'''
def search(request):
    # 백엔드 작업 수행
    
    # 데이터베이스 검색
    try:
        question = Question.objects.get(pk=parameter)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    
    # 템플릿 설정
    template = loader.get_template('haneum/search.html')
    # 템플릿 전달 인자 및 전달 값 설정
    context = {
        'msg': 'This is search, project start',
    }
    return HttpResponse(template.render(context, request))
'''

def search(request):
    # 백엔드 작업 수행
    
    # 템플릿 전달 인자 및 전달 값 설정
    context = {
        "msg": "This is search, project start",
    }
    # 템플릿 설정
    return render(request, 'haneum/search.html', context)

def articles(request, company_name):
    
    
    
    context = {
        "company_name": company_name,
    }
    return render(request, 'haneum/articles.html', context)

def analytics(request, company_no):
    
    
    
    context = {
        "company_no": company_no,
    }
    return render(request, 'haneum/analytics.html', context)

def prediction(request, company_no):
    
    
    
    context = {
        "company_no": company_no,
    }
    return render(request, 'haneum/prediction.html', context)
