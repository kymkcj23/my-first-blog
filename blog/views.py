from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    # views.post_list 함수는 이제 DB에서 필요한 데이터를 가져와서
    # post_list.html에게 넘겨줘야 함.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
                        # 출판일자가 지금보다 이전으로 들어있는 행만 검색
    return render(       # rander() 함수를 호출하여 화면을 출력
                request, # 함수에게 사용자가 요청한 정보를 전달
                'blog/post_list.html', # 화면 출력 주체 지정
                {'posts': posts}) # 화면 출력에 사용할 데이터 전달 중괄호 = 딕셔너리(사전)

