from flask import Flask, render_template, request
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
        form = request.form
        response = query_processor(['abc','def'], request.form['query_box'])
        
        if('query_submission' in form):
            return render_template(
                "response_page.html", 
                query=form["query_box"],
                response=response
            ), 200
        else:
            return "Unknown form POSTed to response_page.", 400
    
    return app