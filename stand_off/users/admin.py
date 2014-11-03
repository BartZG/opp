from django.contrib import admin
from users.models import User, Reservation, Comment
# Register your models here.
admin.site.register(User)
admin.site.register(Reservation)
admin.site.register(Comment)