from django.shortcuts import render,redirect, get_object_or_404 # 데이터가 없다면 404 에러
from .models import Photo # model에서 Photo클래스 가져옴
from .forms import PhotoForm

# 뷰는 데이터베이스에서 데이터를 꺼내 탬플릿으로 전달하기도 하지만 
# 탬플릿을 보이게 하는 역할도 수행한다
# Create your views here.

# 함수형 뷰
def photo_list(request):
    photos = Photo.objects.all() # ORM
    return render(request, 'photo/photo_list.html', {'photos': photos})

def photo_detail(request,pk):
    photo = get_object_or_404(Photo,pk = pk) # pk는 django의 기본 ID값임
    return render(request, 'photo/photo_detail.html', {"photo": photo})

# 우리는 photo_list 라는 함수를 만들었다 
# render함수는 photo/photo_list.html을 렌더링, 쉽게말해
# 웹에 보여질수 있도록 가공하여 전달하였다.
# photo_list()라는 함수가 불렸을때 photo_list.html이 나타나게 됨
# 뷰에서 마지막 return 인자에 있던 {}을 사용하면 템플릿으로 데이터를 보낼수 있다
# 보내고자 하는 데이터를 이름과 함께 적으면 됨
# 그전에 이 데이터들을 모델에서 꺼내와야하는데 이때 Django에서 제공하는
# 대표적인 기술중 하나인 ORM 을 사용한다

# Photo.objects.all()로 모델데이터를 가져와, {}여기에 넣어서 템플릿으로 전달 
# 데이터를 전달 받은 템플릿은 photos를 템플릿 태그'{}'와 함께 이용할것이다

def photo_post(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit = False)
            photo.save()
            return redirect('photo_detail', pk=photo.pk) 
    else:
        form = PhotoForm()
    return render(request, 'photo/photo_post.html' , {'form': form})


def photo_edit(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'photo/photo_post.html' ,{'form': form})
