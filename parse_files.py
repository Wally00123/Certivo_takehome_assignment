'''
IMPORTS

pdfplumber      :   library to parse PDF files in python
bs4             :   library holding BeautifulSoup, library to parse HTML
glob            :   for finding and iterating through files for parsing
'''
import pdfplumber
from bs4 import BeautifulSoup
import glob


'''
Function to parse HTML files and convert data to format Python can understand

Data is returned to be further processed/used

@Inputs:    file_path:str -> Path to HTML file
@Output:    html_data_table -> HTML data (only that found in tables)
            html_data_words -> HTML data (all words)
'''
def parse_HTML(file_path:str):
    return parse_HTML_tables(file_path), parse_HTML_words(file_path)


'''
Function to parse HTML files and convert data to format Python can understand

Data is returned to be further processed/used (all words)

@Inputs:    file_path:str -> Path to HTML file
@Output:    html_data_words -> HTML data (all words)
'''
def parse_HTML_words(file_path:str):
    with open(file_path) as fp:
        soup = BeautifulSoup(fp, 'lxml')

    html_data_words = ""

    tag = soup.body

    for string in tag.strings:
        html_data_words += string

    return html_data_words


'''
Function to parse HTML files and convert data to format Python can understand

Data is returned to be further processed/used (only that found in tables)

@Inputs:    file_path:str -> Path to HTML file
@Output:    html_data_table -> HTML data (only that found in tables)
'''
def parse_HTML_tables(file_path:str):
    with open(file_path) as fp:
        soup = BeautifulSoup(fp, 'lxml')

    table = soup.find_all('table')[0]

    headers = []
    rows = []
    for i, row in enumerate(table.find_all('tr')):
        if i == 0:
            headers = [el.text.strip() for el in row.find_all('th')]
        else:
            rows.append([el.text.strip() for el in row.find_all('td')])

    html_data_table = []
    html_data_table.append(headers)
    html_data_table.append(rows)

    return html_data_table


'''
Function to parse PDF files and convert data to format Python can understand

Data is returned to be further processed/used

@Inputs:    file_path:str -> Path to PDF file
@Output:    table       -> All information in tables within the PDF
            words       -> All words found in the PDF
'''
def parse_PDF(file_path:str):
    return parse_PDF_tables(file_path), parse_PDF_words(file_path)

    '''
    Has outer array with all tables

    Has inner array which is each array

    Each array has a bunch of arrays for each row


    If only extracting the one table, then outer array not present, just inner and items
    '''


'''
Function to parse PDF files and convert data to format Python can understand

Data is returned to be further processed/used (all words)

@Inputs:    file_path:str -> Path to PDF file
@Output:    words -> PDF file data (all words)
'''
def parse_PDF_words(file_path:str):
    pdf = pdfplumber.open(file_path)
    
    num_pages = len(pdf.pages)
    #print(num_pages)

    words = ""
    for page_num in range(num_pages):
        page = pdf.pages[page_num]

        words += page.extract_text()

    pdf.close()
    return words


'''
Function to parse PDF files and convert data to format Python can understand

Data is returned to be further processed/used (only that found in tables)

@Inputs:    file_path:str -> Path to PDF file
@Output:    table       -> All information in tables within the PDF
'''
def parse_PDF_tables(file_path:str):
    pdf = pdfplumber.open(file_path)
    
    num_pages = len(pdf.pages)
    #print(num_pages)

    table = []
    for page_num in range(num_pages):
        page = pdf.pages[page_num]
        tables = page.extract_tables()
        if tables != [] and table != []:
            for item in tables[0]:
                table[0].append(item)
        elif tables != []:
            for item in tables[0]:
                table.append(item)

    pdf.close()
    return table


'''
Goes through the Files folder (and any subfolders) and looks for all PDF and HTML files

Using those files, it extracts all necessary data and returns it for futher use

@Inputs:    None
@Output:    Data -> data from all the files found
'''
def get_data():
    pdf_files = []
    html_files = []

    for filename in glob.glob('Files\\*.pdf', recursive=True):
        pdf_files.append(filename)

    for filename in glob.glob('Files\\*.html', recursive=True):
        html_files.append(filename)

    # print(pdf_files, html_files)

    data = []

    for file in pdf_files:
        pdf_data_table, pdf_data_words = parse_PDF(file)
        
        data.append(pdf_data_table)
        data.append(pdf_data_words)

    for file in html_files:
        html_data_table, html_data_words = parse_HTML(file)

        data.append(html_data_table)
        data.append(html_data_words)

    return data


'''
Goes through the Files folder (and any subfolders) and looks for all PDF and HTML files

Using those files, it extracts all words and returns them

@Inputs:    None
@Output:    data -> words from all the files found
'''
def get_data_words():
    pdf_files = []
    html_files = []

    for filename in glob.glob('Files\\*.pdf', recursive=True):
        pdf_files.append(filename)

    for filename in glob.glob('Files\\*.html', recursive=True):
        html_files.append(filename)

    # print(pdf_files, html_files)

    data = []

    for file in pdf_files:
        data.append(parse_PDF_words(file))

    for file in html_files:
        data.append(parse_HTML_words(file))

    return data


'''
Goes through the Files folder (and any subfolders) and looks for all PDF and HTML files

Using those files, it extracts all words and returns them

@Inputs:    None
@Output:    data -> data from all the tables found within the files
'''
def get_data_tables():
    pdf_files = []
    html_files = []

    for filename in glob.glob('Files\\*.pdf', recursive=True):
        pdf_files.append(filename)

    for filename in glob.glob('Files\\*.html', recursive=True):
        html_files.append(filename)

    # print(pdf_files, html_files)

    data = []

    for file in pdf_files:
        data.append(parse_PDF_tables(file))

    for file in html_files:
        data.append(parse_HTML_tables(file))

    return data


# Main
if __name__ == "__main__":
    data = get_data()

    for item in data:
        print(item)
        print("\n\n\n")