from app import create_app

app = create_app()

# DO NOT use app.run() in production
# Gunicorn will start the server
if __name__ == '__main__':
    app.run(debug=True)