from django.contrib.auth.models import User
from django.db import models
from django.template.loader import render_to_string

class EmailActivation(models.Model):
    activation_key = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    expire_date = models.DateTimeField()
    #activation_user = models.ForeignKey(User)

class Following(models.Model):
    followee = models.ForeignKey(User, related_name = 'following_followee')
    followee_str = models.CharField(max_length=20, blank=True)
    follower = models.ForeignKey(User, related_name = 'following_follower')
    follower_str = models.CharField(max_length=20, blank=True)
    
    class Meta:
        verbose_name_plural = "Followings"
        ordering = ['followee']
    
    def __unicode__(self):
        return "%s followed by %s" %(self.followee, self.follower)
        
    def get_absolute_url(self):
        return "/accounts/%s/followings/%d" %(self.followee, self.id)

class UserProfile(models.Model):
    EMOTION_CHOICES = (
        ('H', 'Happy'),
        ('S', 'Sad')
    )
    
    department = models.CharField(null=True, max_length=50)
    emotion = models.CharField(null=True, choices=EMOTION_CHOICES, max_length=20)
    phone = models.CharField(null=True, max_length=50)
    portrait = models.FileField(null=True, upload_to="user_profile/")
    position = models.CharField(null=True, max_length=50)
    user = models.OneToOneField(User) # User Profile have to contain this field.
    
    
    class Meta:
        ordering = ['user__username']
        
    def __unicode__(self):
        return "%s's profile" %(self.user.username)
    
    def get_absolute_url(self):
        return '/accounts/profile/%s' %(self.user.username)
    
    def get_rendered(self):
        return render_to_string('accounts/people_profile_render.html',{
                                                                       'people_profile':self
                                                                       })