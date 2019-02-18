a = 5;
def bb():
    global a;
    a = 8;




if __name__ == "__main__":
    bb();
    print(a)