from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from app.models.Post import Post
from masonite.response import Response


class BlogController(Controller):
    def show(self, view: View):
        blogs = Post.all()
        return view.render("blog", {"blogs": blogs})

    def create(self, request: Request, view: View, response: Response):
        Post.create(
            title=request.input('title'),
            body=request.input('body'),
            # author_id=request.user().id
        )
        return response.redirect('/blog')

    def delete(self, view: View, request: Request, response: Response):
        post = Post.find(request.param('post_id'))
        post.delete()
        return response.redirect('/blog')

    def showsingle(self, view: View, request: Request, response: Response):
        post = Post.find(request.param('post_id'))
        return view.render('updateblog', {"post": post})

    def update(self, view: View, request: Request, response: Response):
        post = Post.find(request.param('post_id'))
        print(post)
        post.title = request.input('title')
        post.body = request.input('body')

        post.save()

        return response.redirect('/blog')
