from flask import Flask, render_template, request
from llm import query_processor
from docmind import pdf_utility
from werkzeug.utils import secure_filename

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
        files = request.files
        file_data = {} # key:file name, value:text content of the file.

        # extracting text from files into file_data
        for name in files:
            file = files[name]
            filename = secure_filename(file.filename)
            if(filename != ''): # i.e. if file not empty
                match(file.mimetype):
                    case 'text/plain'|'text/markdown':
                        file_data[filename] = file.stream.read()
                    case 'application/pdf':
                        file_data[filename] = pdf_utility.text_from_pdf(file.stream)
                    case '_':
                        return "Unsupported filetype {} submitted.".format(file.mimetype), 400

        # getting the response text
        response = query_processor(file_data, request.form['query_box'])
        
        # rendering the template and returning the response
        # if correct form submitted.
        if('query_submission' in form):
            return render_template(
                "response_page.html", 
                query=form["query_box"],
                response=response
            ), 200
        else:
            return "Unknown form POSTed to response_page.", 400
    
    return app