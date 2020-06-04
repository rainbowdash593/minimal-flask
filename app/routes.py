from app.controllers.hello import TestController


ROUTES = [
    {
        'prefix': '/api',
        'group': [
            {'prefix': '/test', 'controller':  TestController},
        ]
    }
]