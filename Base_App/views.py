from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def HomeView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all()
    
    return render(request, 'home.html', {'items': items , 'list': list, 'review':review})

def AboutView(request):
    data = AboutUs.objects.all()
    return render(request, 'about.html',{'data': data})

def MenuView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    return render(request, 'menu.html', {'items': items , 'list': list})

def BookTableView(request):
    success_message = ""
    if request.method == 'POST':
        name = request.POST.get('user_name')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('user_email')
        total_people = request.POST.get('total_people')
        booking_date = request.FILES.get('booking_date')

        if name != '' and total_people != 0 and booking_date !='' and email !='':
            data = BookTable(Name = name, Phone_number= phone_no, Email = email, Total_people = total_people, Booking_Date = booking_date)
            data.save()
            success_message = "Thank you! Your booking is successful!"
        else:
            success_message = "Please provide all required details."
    return render(request, 'book_table.html', {'message' : success_message})


def FeedbackView(request):
    feed_message = ""
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        rating = request.POST.get('rating')
        image = request.FILES.get('image')

        
        data = Feedback(User_name = name, Description= description, Rating = rating, Image = image)
        data.save()
        feed_message = "Thanks for your feedback..have a nice day!"

    return render(request, 'feedback.html',{'message' : feed_message})
