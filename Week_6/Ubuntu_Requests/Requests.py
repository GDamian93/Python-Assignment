import os
import requests
from urllib.parse import urlparse
import hashlib

""" 
    This function generates a unique identifier for a given file content 
    and returns it as a string.
"""
def hash_file(content):
    """Return the SHA256 hash of the file content."""
    return hashlib.sha256(content).hexdigest()

def main():
    print("=== Ubuntu-Inspired Multi Image Fetcher ===")
    urls = input("Digite as URLs das imagens (separadas por vírgula): ").strip().split(",")

    # Create "Fetched_Images" directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    # Set to store downloaded image hashes and avoid duplicates
    downloaded_hashes = set()

    # 
    for url in urls:
        url = url.strip()
        if not url:
            continue

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            # To check HTTP headers
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f"⚠️ Ignorado (não é imagem): {url}")
                continue

            content_length = response.headers.get("Content-Length")
            if content_length and int(content_length) > 10_000_000:  # limite de 10MB
                print(f"⚠️ Arquivo muito grande, ignorado: {url}")
                continue

            # To send duplicates via hash 
            file_hash = hash_file(response.content)
            if file_hash in downloaded_hashes:
                print(f"⚠️ Imagem duplicada ignorada: {url}")
                continue
            downloaded_hashes.add(file_hash)

            # Extract filename from URL
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)

            if not filename:
                filename = f"image_{len(downloaded_hashes)}.jpg"

            filepath = os.path.join("Fetched_Images", filename)

            # avoid overwriting existing file
            base, ext = os.path.splitext(filepath)
            counter = 1
            while os.path.exists(filepath):
                filepath = f"{base}_{counter}{ext}"
                counter += 1

            # Save the image
            with open(filepath, "wb") as f:
                f.write(response.content)

            print(f"✅ Imagem salva em: {filepath}")

        except requests.exceptions.RequestException as e:
            print(f"⚠️ Erro ao buscar {url}: {e}")

if __name__ == "__main__":
    main()