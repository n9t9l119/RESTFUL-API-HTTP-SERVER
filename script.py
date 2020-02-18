from config import app#, BaseConfig#, TestConfig
from pages import api

if __name__ == '__main__':
    #app.config.from_object(config)
    api.ApiView.register(app)
    app.run(port="4000")



