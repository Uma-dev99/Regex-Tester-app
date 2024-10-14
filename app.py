from flask import Flask, render_template, request
import re

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    pattern = ''
    test_string = ''
    
    if request.method == 'POST':
        pattern = request.form.get('pattern', '')
        test_string = request.form.get('test_string', '')
        
        try:
            result = re.findall(pattern, test_string)
        except re.error as e:
            result = f"Regex error: {e}"
    
    return render_template('index.html', pattern=pattern, test_string=test_string, result=result)


if __name__ == '__main__':
    app.run(debug=True)
