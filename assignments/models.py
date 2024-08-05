from django.db import models


class About(models.Model):
    about_heading = models.CharField(max_length=25)
    about_description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'
        
    def __str__(self):
        return f'{self.about_heading}'
    
    
class SocialLink(models.Model):
    platform = models.CharField(max_length=25)
    link = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'SocialLink'
        verbose_name_plural = 'SocialLinks'
    
    
    def __str__(self):
        return f'{self.platform}'