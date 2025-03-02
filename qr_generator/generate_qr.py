import qrcode
import requests
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from PIL import Image
from logger import log_qr_generation, log_error

def fetch_metadata(url):
    """
    Extracts the title and description from a webpage.
    """
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else "No title found"
        meta_desc = soup.find("meta", attrs={"name": "description"})
        description = meta_desc["content"] if meta_desc else "No description available."

        return f"{title}: {description}"
    except Exception as e:
        log_error(f"Error fetching metadata: {e}")
        return f"Error fetching metadata: {e}"

def generate_summary(text, num_sentences=2):
    """
    Uses Sumy's LSA summarizer to generate a summary.
    """
    if not text or len(text.split()) < 10:
        return text  # Return the original text if it's too short for summarization

    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary_sentences = summarizer(parser.document, num_sentences)
        
        if summary_sentences:
            return " ".join(str(sentence) for sentence in summary_sentences)
        else:
            return text  # Return original text if summarization fails
    except Exception as e:
        log_error(f"Summarization error: {e}")
        return text  # Return original text as fallback

def generate_qr(content):
    """
    Generates a QR code with AI-optimized content.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    return img

def save_and_open_qr(qr_image):
    """
    Saves the QR code image to a file.
    """
    filename = "qr_code.png"
    qr_image.save(filename)
    log_qr_generation(f"QR code saved as {filename}")
    print(f"QR code saved as {filename}")

def main():
    """
    Main function to process user input and generate a QR code.
    """
    user_input = input("Enter a URL or text: ").strip()

    if not user_input:
        print("Error: Input cannot be empty!")
        return

    if user_input.startswith("http"):
        metadata = fetch_metadata(user_input)
        summarized_text = generate_summary(metadata)
    else:
        summarized_text = generate_summary(user_input)

    print(f"AI-Optimized QR Content: {summarized_text}")

    # Generate QR Code
    qr_image = generate_qr(summarized_text)

    # Save and open QR Code
    save_and_open_qr(qr_image)

if __name__ == "__main__":
    main()
