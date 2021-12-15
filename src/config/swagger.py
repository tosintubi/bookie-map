
# Swagger template and configuration setup

template = {
    'swagger': '2.0',
    'info': {
        'title': 'Bookie P2P API',
        'description': 'API for Bookie P2P App',
        'contact': {
            'responsibleOrganization': '',
            'responsibleDeveloper': '',
            'email': 'api@bookie-api.com',
            'url': 'www.bookie-api.com',
        },
        'termsOfService': 'www.bookie-api.com/terms',
        'version': '1.0'
    },
    'basePath': '/api',  # base path for blueprint registration
    'schemes': [
        'http',
        'https'
    ],
    'securityDefinitions': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'JWT Authorization header using the Bearer scheme. Example: \'Authorization: Bearer {token}\''
        }
    },
}

swagger_config = {
    'headers': [
    ],
    'specs': [
        {
            'endpoint': 'apispec',
            'route': '/apispec.json',
            'rule_filter': lambda rule: True,  # all in
            'model_filter': lambda tag: True,  # all in
        }
    ],
    'static_url_path': '/flasgger_static',
    'swagger_ui': True,
    'specs_route': '/'
}
