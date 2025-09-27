from flask import Flask, render_template
from llm import query_processor
import pdf_utility

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/", methods=('GET',))
    def index():
        return "Hello", 200
    
    @app.errorhandler(404)
    def page_not_found(e):
        return "OOPS! Page not found.", 404
    
    @app.route("/query_page", methods=('GET',))
    def query_page():
        return "Prompt Page", 200
    
    @app.route("/response_page", methods=('POST',))
    def result_page():
        return 
    
    return app