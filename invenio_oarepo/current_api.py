from flask import current_app
from flask.globals import _request_ctx_stack

#
# Usage:
#
# In cli or in UI request:
#
#  with app.app_context():                  (already active in UI request)
#     with current_api.app_context():
#         print('api url inside current_api', url_for('api', _external=True))
#
#

class CurrentApiApp:
    def app_context(self):
        return CurrentApiAppContext()


class CurrentApiAppContext:
    def __init__(self):
        self._current_api = current_app.wsgi_app.mounts['/api']

    def __enter__(self):
        reqctx = _request_ctx_stack.top
        if not reqctx:
            url_scheme = self._current_api.config['PREFERRED_URL_SCHEME']
            server_name = self._current_api.config['SERVER_NAME']
            base_url = f'{url_scheme}://{server_name}/api'
        else:
            base_url = reqctx.request.host_url + 'api'
        self._context = \
            self._current_api.test_request_context('/', base_url=base_url)
        return self._context.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._context.__exit__(exc_type, exc_val, exc_tb)


current_api = CurrentApiApp()

__all__ = ('current_api',)
