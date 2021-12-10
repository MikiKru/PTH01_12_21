def read_files(path1, path2):
    with open(path1, mode="r") as file1, open(path2, mode="r", encoding='utf-8') as file2:
        return file1.readlines(), file2.readlines()

def write_file(path, content):
    with open(path, mode="w", encoding='utf-8') as file_out1:
        file_out1.writelines(content)

file1_content, file2_content = read_files(r'C:\Users\Student\PycharmProjects\PYTH01_12_21\d5\exercises\ex_7_1\files\w1.txt',
                                          r'C:\Users\Student\PycharmProjects\PYTH01_12_21\d5\exercises\ex_7_1\files\w2.txt')
write_file("new_file.txt", file1_content + ["\n\n"] + file2_content)


