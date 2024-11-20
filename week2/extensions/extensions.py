def get_media_type(filename):
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }
    filename = filename.lower().strip()
    for extension, media_type in media_types.items():
        if filename.endswith(extension):
            return media_type
    return "application/octet-stream"

def main():
    filename = input("Enter the file name: ")
    print(get_media_type(filename))

main()