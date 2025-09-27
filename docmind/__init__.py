from flask import Flask, render_template
from llm import query_processor
from docmind import pdf_utility

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/", methods=('GET',))
    def index_page():
        return render_template("index_page.html"), 200
    
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("page_not_found.html"), 404
    
    @app.route("/query_page", methods=('GET',))
    def query_page():
        return render_template("query_page.html"), 200
    
    @app.route("/response_page", methods=('POST',))
    def response_page():
        return render_template("response_page.html"), 200
    
    return app