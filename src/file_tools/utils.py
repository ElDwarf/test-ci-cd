def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def append_text(file_path, text):
    with open(file_path, 'a') as file:
       file.write(text)

