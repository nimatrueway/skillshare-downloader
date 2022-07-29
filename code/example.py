from downloader import Downloader

cookie = """
PHPSESSID=8eca04603401f57dfd4c75aa2c00348b
"""

dl = Downloader(cookie=cookie)

# download by class URL:
dl.download_course_by_url('https://www.skillshare.com/classes/Art-Fundamentals-in-One-Hour/189505397')

# or by class ID:
# dl.download_course_by_class_id(189505397)
