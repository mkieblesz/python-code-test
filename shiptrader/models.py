from django.db import models


class Starship(models.Model):
    model = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    starship_class = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)

    length = models.FloatField(null=True, blank=True)
    hyperdrive_rating = models.FloatField(null=True, blank=True)
    cargo_capacity = models.BigIntegerField(null=True, blank=True)

    crew = models.IntegerField(null=True, blank=True)
    passengers = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.model

    @classmethod
    def get_starship_class_choices(self):
        return (sc for sc in Starship.objects.values_list('starship_class', flat=True).distinct())


class Listing(models.Model):
    headline = models.CharField(max_length=255)
    ship_type = models.ForeignKey(Starship, related_name='listings')
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.headline
