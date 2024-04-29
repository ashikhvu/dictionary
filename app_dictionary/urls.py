from django.urls import path
from app_dictionary import views

urlpatterns = [
    path('',views.home,name='home',),
    path('dictionary',views.dictionary,name='dictionary'),
    path('dictionary_add',views.dictionary_add,name='dictionary_add'),
    path('add_words',views.add_words,name='add_words'),
    path('upload_file',views.upload_file,name='upload_file'),
    path('delete_all',views.delete_all,name='delete_all'),
    path('test_words/<int:pk>',views.test_words,name='test_words'),
    path('next_word/<int:pk>',views.next_word,name='next_word'),
    path('prev_word/<int:pk>',views.prev_word,name='prev_word'),
    path('edit_word/<int:pk>',views.edit_word,name='edit_word'),
    path('save_word/<int:pk>',views.save_word,name='save_word'),
]