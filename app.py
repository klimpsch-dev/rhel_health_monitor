from flask import Flask, render_template
import subprocess
import os
import helper


app = Flask(__name__)

@app.route('/')
def home():
    # Run the 'cat' command for three different files and capture their outputs
    cat_output1 = get_ip_address()
    cat_output2 = get_routes()
    cat_output3 = get_listening_ports()

    # Pass the outputs to the template
    return render_template('index.html', file1_content=cat_output1.stdout,
                                         file2_content=cat_output2.stdout,
                                         file3_content=cat_output3.stdout)

if __name__ == '__main__':
    app.run(debug=True)