from django.contrib import admin

# Register your models here.
from .models import Project, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('repo', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']
	
class RepoAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('id', 'url', 'owner_id', 'name', 'description', 'language', 'created_at', 'updated_at')
    search_fields = ['name','owner_id', 'language']
	
admin.site.register(Project, RepoAdmin)
admin.site.register(Review, ReviewAdmin)
