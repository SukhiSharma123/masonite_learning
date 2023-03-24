from masonite.routes import Route


ROUTES = [
    Route.get('/users', 'UsersController@index'),
    Route.api('users', "api.UserController"),
    Route.get('/users', 'UserController@show').middleware(["guard:jwt"]),
    Route.post('/post/', 'UsersController@create'),
]
