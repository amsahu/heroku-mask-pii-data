from flask import Flask, request, render_template, send_file
import os
from werkzeug.utils import secure_filename
from spacy import load
from custom_functions import *



app = Flask(__name__)
global df
model = load('model_spacy')

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/uploader" , methods=['GET', 'POST'])
def uploader():
    if request.method=='POST':
        f = request.files['file']
        f.save(os.path.join(os.getcwd(), 'upload', secure_filename(f.filename)))
        filename = os.path.join('upload',secure_filename(f.filename))
        global df
        if filename.endswith('.csv'):
            df= create_df(filename, 1)
        else:
            df= create_df(filename, 2)

        return render_template('index.html', 
                               msg_text='Uploaded successfully',
                               total_text='Total data (row*column): {}'.format(df.shape[0]*df.shape[1]),
                               time_text= 'After clicking "Mask and download", it will take less than {} seconds, do not close the browser'.format(int((0.006*df.shape[0]*df.shape[1])+12)))


@app.route("/mask_data_download" , methods=['GET', 'POST'])
def mask_data_download():
    try:
        
        if request.method=='POST':
            indices = get_indices(df, model)
            df_masked = mask_data(df, indices, masking_rule)
            df_masked.to_csv(os.path.join('download','masked_data.csv'), index=False)
            return send_file('download\\masked_data.csv')
    finally:
        for file in list(os.scandir('upload')):
            os.remove(file.path)


if __name__ == "__main__":
    app.run(debug=True)