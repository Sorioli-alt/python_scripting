from openai import OpenAI
import PyPDF2
import csv
import os

def pdf_reader(filename):
    pdfFileObj = open(filename,'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    for page in pdfReader.pages:
        print(page.extract_text())

dir = r""
def file_extension(directory):
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f) and f.endswith('.pdf'):
            print('PDF file')
            pdf_reader(f)
        elif os.path.isfile(f) and f.endswith('.xlsx'):
            print('Excel file')
        elif os.path.isfile(f) and f.endswith('.csv'):
            print('CSV file')
file_extension(directory=dir)     



# client = OpenAI()


# print(len(pdfReader.pages))

# pageObj = pdfReader.pages[0]

# text = pageObj.extract_text()

# pdfFileObj.close()

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You will be provided with unstructured data, and your task is to parse it into CSV format with the following headers: description, manufacturer, model, serial# (if applicable), price and lead time."},
#     {"role": "user", "content": text}
#   ]
# )

# with open('chatgpt_results.csv', 'w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow([completion.choices[0].message])
