from masonite.routes import Route
from masonite.authentication import Auth
from masonite.api import Api

ROUTES = [Route.get("/", "WelcomeController@show"),
          Route.get('/blog', 'BlogController@show'),
          Route.post('/blog/create', 'BlogController@create'),
          Route.get('/blog/delete/@post_id', 'BlogController@delete'),
          Route.get('/blog/update/@post_id', 'BlogController@showsingle'),
          Route.post('/blog/update/@post_id', 'BlogController@update'),
          ]

ROUTES += Auth.routes()

ROUTES += Api.routes(auth_route="/api/auth", reauth_route="/api/reauth")
