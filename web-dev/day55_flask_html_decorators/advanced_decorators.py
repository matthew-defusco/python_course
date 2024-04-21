class User:
  def __init__(self, name) -> None:
    self.name = name
    self.is_logged_in = False

def is_authenticated_decorator(function):
  def wrapper(*args, **kwargs):
    # Takes the arguments from the function that's being "decorated" and can access them
    # through *args and **kwargs
    if args[0].is_logged_in == True:
      function(args[0])
    else:
      print("They're not logged in!")
  return wrapper

@is_authenticated_decorator
def create_blog_post(user):
  print(f"This is {user.name}'s new blog post.")

new_user = User("Matt")
new_user.is_logged_in = True
create_blog_post(new_user)