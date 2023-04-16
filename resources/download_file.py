import urllib.request
import subprocess

def download_file(url):
    # Extract the filename from the URL
    filename = url.split('/')[-1]

    # Download the file from the internet
    urllib.request.urlretrieve(url, filename)

    # Install the downloaded file
    subprocess.call([filename])

# Example usage:
download_file("http://example.com/file.exe")
