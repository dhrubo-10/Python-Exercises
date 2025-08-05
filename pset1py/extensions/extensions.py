def file_t(extension):
    ext = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip'
    }

    return ext.get(extension, 'application/octet-stream')


def main():

    file_n = input("FIle Name: ")

    extension = file_n.strip().split('.')[-1].lower() if '.' in file_n else None


    if extension in ['gif', 'jpg', 'jpeg', 'png', 'pdf', 'txt', 'zip']:

        extn = file_t(extension)

        print(extn)

    else:
        print("application/octet-stream")

main()
