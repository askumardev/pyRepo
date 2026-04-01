import PyPDF2
import sys

def merge_pdfs(pdf_list, output):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output)
    merger.close()
    print(f"PDFs merged successfully into {output}")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        pdf_files = sys.argv[1:-1]
        output_file = sys.argv[-1]
    else:
        pdf_files = input("Enter PDF file names separated by commas: ").split(',')
        pdf_files = [f.strip() for f in pdf_files]
        output_file = input("Enter output PDF file name: ").strip()

    merge_pdfs(pdf_files, output_file)


# python3 projs/pdf_merger.py file1.pdf file2.pdf output.pdf