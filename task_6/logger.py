class Logger:
    def write_to_file(li, file_name = "observer_.txt"):
        my_file = open(file_name, 'a')
        my_file.write( str(li) + '\n')
        my_file.close()

