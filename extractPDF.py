import PyPDF2

pdf = open("RoundOne.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdf, strict=False)

print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
pageText = pageObj.extractText()
#print(type(pageText))

print(pageText.replace("\r",""))