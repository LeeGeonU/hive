from accounts.models import UserProfile
from django.contrib.auth.models import User
from posts.models import Post
from timelines.models import Timeline
import random
import datetime

notice_bot = User.objects.create_user("notice_bot", "notice_bot@test.com", "notice_bot")
UserProfile.objects.create(user=notice_bot)

humor_bot = User.objects.create_user("humor_bot" , "humor_bot@test.com", "humor_bot")
UserProfile.objects.create(user=humor_bot)

for x in range(100):
    User.objects.create_user("test" + str(x) , "test" + str(x) + "@test.com" , "test" + str(x))
for user in User.objects.all():
    UserProfile.objects.create( user = user )

for x in range(10):
    now = datetime.datetime.now()
    users = User.objects.order_by("?").all()
    for user in users:
        post_content = "bull bull bull %d" %(random.randint(0,100000))
        now = now + datetime.timedelta(minutes=1)
        post = Post.objects.create( contents = post_content , create_time = now , writer = user , author = user.username)
        Timeline.objects.create( writer = user , post = post )


