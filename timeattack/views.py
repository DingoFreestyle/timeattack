from django.http import HttpResponse
from django.shortcuts import render

# 홈페이지 렌더시키기
def INDEX(request):
    return render(request, 'index.html')