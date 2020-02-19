from config import app
from pages import api


if __name__ == '__main__':
    api.ApiView.register(app)
    app.run(port="8000")



