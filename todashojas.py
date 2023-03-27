from PyPDF2 import PdfReader

reader = PdfReader("Ley4988.pdf")
parts = []

def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if y > 50 and y < 720:
        parts.append(text)

for page in reader.pages:
    page.extract_text(visitor_text=visitor_body)

text_body = "".join(parts)
print(text_body)