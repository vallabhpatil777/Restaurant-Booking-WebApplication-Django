from django.db import models

# Create your models here.
class ItemList(models.Model):
    Category_name = models.CharField(max_length= 50)
    def __str__(self):
        return self.Category_name

class Items(models.Model):
    Item_name = models.CharField(max_length=50)
    Description = models.TextField(blank=False)
    Price = models.IntegerField()
    Category = models.ForeignKey(ItemList, related_name='Category_Name', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='Items/')

    def __str__(self):
        return self.Item_name

class AboutUs(models.Model):
    description = models.TextField(blank=False)

    def __str__(self):
        return self.description[:5]




class Feedback(models.Model):
    User_name = models.CharField(max_length=20)
    Description = models.TextField(blank=False)
    Rating = models.IntegerField()
    Image = models.ImageField(upload_to='Items/',blank=True)

    def __str__(self):
        return f'{self.User_name} - {self.Rating}'

class BookTable(models.Model):
    Name = models.CharField(max_length=20)
    Phone_number = models.IntegerField()
    Email = models.EmailField()
    Total_people = models.IntegerField()
    Booking_Date = models.DateField()

    def __str__(self):
        return f'{self.Name} - {self.Booking_Date}'