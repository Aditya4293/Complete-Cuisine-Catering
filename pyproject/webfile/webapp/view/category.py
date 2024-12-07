from django.db import models

class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    cat_name=models.CharField(max_length=100)
    description=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return "%s %s %s" % (self.cat_id,self.cat_name, self.created_date)