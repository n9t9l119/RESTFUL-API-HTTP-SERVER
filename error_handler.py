from config import app


@app.errorhandler(404)
def not_found_error(error):
    return "Error 404\nPage Not Found"


@app.errorhandler(400)
def not_found_error(error):
    return "Error 400!\nIncorrect syntax"


@app.errorhandler(500)
def internal_error(error):
    return "Error 500\nInternal Server Error"
