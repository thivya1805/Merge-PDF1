from PyPDF2 import PdfMerger
from io import BytesIO
from flask import request,Flask,render_template,send_file,abort

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def merge_pdfs():
    if request.method =='POST':

        pdf_files = request.files.getlist("pdf_files")
        
        merger = PdfMerger()

        for pdf in pdf_files:
            merger.append(pdf)

        buffer = BytesIO()

        merger.write(buffer)

        buffer.seek(0)

        # Allow the file to be downloaded

        return send_file(buffer,as_attachment=True,download_name="merged.pdf")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

