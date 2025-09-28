def query_processor(context_data:dict[str,str], prompt:str)->str:
    '''
        - context_data contains the text of files attached by user.
        - It is a dictionary where filename is the key
          and respective value is the file's text content.
        - The prompt is a string containing the query provided by user.
        - The return value is a string (containing the answer to prompt).
    '''
    return "Not implemented yet. context_data = " + context_data.__str__()