#import myapp Flask application
from main import app


if __name__ == "__main__":
    from werkzeug.middleware.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[5], profile_dir='logs')
    app.run(debug=True)
