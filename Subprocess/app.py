from flask import Flask, render_template
import subprocess
import os
import helper


app = Flask(__name__)

@app.route('/')
def home():
    # Run the 'cat' command for three different files and capture their outputs
    cat_output1 = helper.get_ip_address()
    cat_output2 = helper.get_routes()
    cat_output3 = helper.get_listening_ports()
    cat_output4 = helper.get_kernel_version()
    cat_output5 = helper.get_failed_services()


    # Pass the outputs to the template
    return render_template('index.html', file1_content=cat_output1,
                                         file2_content=cat_output2,
                                         file3_content=cat_output3,
                                         file4_content=cat_output4,
                                         file5_content=cat_output5)

if __name__ == '__main__':
    app.run(debug=True)