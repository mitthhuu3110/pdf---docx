from pdf2docx import Converter


old_pdf = "Internship Offer Letter - Mithilesh.pdf"
new_doc = "Internship Offer Letter - Mithilesh.docx"

obj = Converter(old_pdf)
obj.convert(new_doc)
obj.close()
