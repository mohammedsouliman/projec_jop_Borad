from django.db import models

# Create your models here.

'''

django model field :
  -html widget
  -validation
  -db size

'''
JOB_TYPE =(
    ('Full Time','Full Time'),
    ('Part Time', 'Part Time'),
)


class  job (models.Model):
    title = models.CharField(max_length=100) # column
    #location
    job_type = models.CharField( max_length=20  , choices = JOB_TYPE  )
    description = models.TextField(max_length =1000)
    punlished_at = models.DateTimeField( auto_now=True , auto_now_add=False)
    vacancy = models.IntegerField(default = 1)
    salary = models.FloatField(default =0) 
    experience = models.IntegerField(default = 1)
    category = models.ForeignKey("Category",  on_delete=models.CASCADE)

    def  __str__(self):
        return self.title
    
class Category  (models.Model):
    name = models.CharField( max_length=100)

    def __str__(self):
        return self.name