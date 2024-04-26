from django.shortcuts import render,redirect
from django.contrib import messages
from app_dictionary.models import *

def home(request):
    return render(request,'home.html')

def dictionary(request):
    dict = dictionary_model.objects.all().order_by('id')
    try:
        response = request.get('https://www.example.com',timeout=5)
        is_online = response.status_code == 200
    except:
        is_online = False
    return render(request,'dictionary.html',{'dict':dict,'is_online':is_online})

def dictionary_add(request):
    try:
        response = request.get('https://www.example.com',timeout=5)
        is_online = response.status_code == 200
    except:
        is_online = False
    return render(request,'dictionary_add.html',{'is_online':is_online})

def add_words(request):
    if request.method == "POST":
        eng = request.POST.getlist('eng[]')
        mal = request.POST.getlist('mal[]')
        for i in range(len(eng)):
            print(f'{eng[i]} = {mal[i]}\n')
            dict = dictionary_model(eng_word=eng[i],mal_word=mal[i])
            dict.save()
    messages.info(request,'saved successfull')
    return redirect('dictionary_add')

def upload_file(request):
    if 'file' in request.FILES:
        file = request.FILES['file']
        file_content = file.read()
        words =  file_content.decode().split()
        for i in range(len(words)):
            if words[i].isalpha():
                dict1 = dictionary_model(eng_word=words[i])
            else:
                dict1.mal_word = words[i]
                dict1.save()
    return redirect('dictionary_add')

def delete_all(request):
    dict = dictionary_model.objects.all()
    dict.delete()
    return redirect('dictionary')

def test_words(request,pk):
    if pk == 0:
        dict = dictionary_model.objects.first()
    else:
        dict = dictionary_model.objects.get(id=pk)
    return render(request,'test_words.html',{"dict":dict})

def next_word(request,pk):
    try:
        next_word = dictionary_model.objects.filter(pk__gt=pk).order_by('pk').first()
        dict = next_word
        return render(request,'test_words.html',{"dict":dict})
    except:
        dict = dictionary_model.objects.last()
        return  render(request,'test_words.html',{"dict":dict})
    
def prev_word(request,pk):
    try:
        next_word = dictionary_model.objects.filter(pk__lt=pk).order_by('-pk').first()
        dict = next_word
        return render(request,'test_words.html',{"dict":dict})
    except:
        dict = dictionary_model.objects.first()
        return  render(request,'test_words.html',{"dict":dict})