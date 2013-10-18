

# Servers config
servers = {
    # Master server
    'master': {
        'url': 'http://drupalinstall.example.org',
        'login': {
            # Username and password
            'username': 'frontdoor',
            'password': 'frontdoorpass',

            # These might change with Drupal versions
            'uri': '/user/login',
            'username_form_key': 'name',
            'password_form_key': 'pass',
            'login_form_id': 'user_login',
        },
    },
    # Local server that actually does auth
    'local': {
        'url': 'http://localhost',
        'login': {
            # Username and password
            'username': 'frontdoor',
            'password': 'frontdoorpass',

            # These might change with Drupal versions
            'uri': '/user/login',
            'username_form_key': 'name',
            'password_form_key': 'pass',
            'login_form_id': 'user_login',
        }
    }
}

