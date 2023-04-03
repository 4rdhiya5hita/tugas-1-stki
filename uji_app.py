from uji_data_retrieval_txt import process_data

with open('example.txt', 'r') as file:
    file_contents = file.read()
    output = process_data(file_contents)

    print(output)
    # print(file_contents)
