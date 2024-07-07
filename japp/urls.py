from django.urls import path
from japp import views

urlpatterns = [
    path('mainpage_book/',views.mainpage_book,name="mainpage_book"),
    path('save_book/',views.save_book,name="save_book"),
    path('display_book/',views.display_book,name="display_book"),
    path('edit_book/<int:bookid>',views.edit_book,name="edit_book"),
    path('update_book/<int:bookid>',views.update_book,name="update_book"),
    path('delete_book/<int:bookid>',views.delete_book,name="delete_book"),

]