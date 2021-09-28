def file_read(fname):
    with open(fname, "a") as myfile:
        myfile.write("Python Exercises\n")
        myfile.write("Practical Exam\n")
    py = open(fname)
    print(py.read())


file_read('Python.py')
