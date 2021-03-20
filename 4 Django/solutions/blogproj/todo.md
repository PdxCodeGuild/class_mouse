## Part 1: User System
- [x] Create the following pages:
    - [x] Register /register/
        - [x] form for creating a new user
        - [x] redirect to /profile/ after registering
    - [x] Login /login/
        - [x] form for logging a user in
        - [x] redirect to /profile/ after logging in
    - [x] Profile /profile/
        - [x] a protected page only logged in users can see
        - [x] just show a welcome message for now
## Part 2: List Blog Posts & Create Blog Post

- [x] Create the following model:
    - [x] BlogPost
        - [x] title (CharField)
        - [x] body (TextField)
        - [x] image (ImageField)
        - [x] user (ForeignKey to django.contrib.auth.models.User)
        - [x] public (BooleanField)
        - [x] date_created (DateTimeField with auto_now_add=True)
        - [x] (optional) date_edited (DateTimeField with auto_now=True)
- [x] Create the following pages:
    - [x] Profile /profile/
        - [x] show a list of the user's own posts, only showing the title of each
    - [x] Create Post /create/
        - [x] form for creating a new post
    - [x] Create /detail/<int:blog_id>/


## Part 3: Edit Post

- [x] Allow users to edit their BlogPosts by creating an edit page. Make sure you prevent users from editing eachother's blog posts (make sure the id for the blog post passed in via the path corresponds to a BlogPost for the logged-in User).
## Part 4: View Other Posts 
- [x] Add pages for users to browse each other's posts.
    - [x] List of Posts /posts/
        - [x] list posts by all users
    - [x] Post Detail /posts/<int:blogpost_id>/
        - [x] view a blog post