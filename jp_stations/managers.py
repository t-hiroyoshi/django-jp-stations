from django.db import models


class StationManager(models.Manager):
    def search_name(self, name):
        return self.filter(name__icontains=name)


class LineManager(models.Manager):
    def search_name(self, name):
        return self.filter(name__icontains=name)


class CompanyManager(models.Manager):
    def search_name(self, name):
        return self.filter(name__icontains=name)
