import fitz


def parse_pdf(file):

    doc = fitz.open(stream=file.read(), filetype="pdf")

    slides = []

    for page_num, page in enumerate(doc):

        # Extract clean text
        text = page.get_text("text")

        # Fix broken lines
        text = text.replace("\n", " ")

        # Remove extra spaces
        text = " ".join(text.split())

        slides.append({
            "page": page_num + 1,
            "content": text
        })

    return slides