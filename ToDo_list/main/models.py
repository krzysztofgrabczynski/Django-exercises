from django.db import models
from uuid import uuid4

class Goal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
    title = models.CharField(max_length=256, blank=False)
    details = models.TextField(blank=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    def __repr__(self) -> str:
        return self.__str__()

