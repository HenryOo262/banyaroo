from mysite import create_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
    
app = create_app()

def handler(event, context):
    return app(event, context)

if __name__ == '__main__':

    app.run(debug=True)