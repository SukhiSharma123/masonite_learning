from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from app.models.Post import Post
from masonite.response import Response


class UsersController(Controller):
    def index(self, view: View):
        return view.render("")

    def show(self, view: View):
        return view.render("")

    def store(self, view: View):
        return view.render("")

    def update(self, view: View):
        return view.render("")

    def destroy(self, view: View):
        return view.render("")

    def create(self, request: Request, view: View):
        Post.create(
            title=request.input('title'),
            body=request.input('body'),
            # author_id=request.user().id
        )
        return Response()
