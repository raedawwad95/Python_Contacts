# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    #your code is here...








    
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
