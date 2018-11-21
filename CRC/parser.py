def parser ():
    Data = open("Test.txt")

    message = ''
    generator = ''

    message = Data.readline()

    generator = Data.readline()

    while True :
        line = input("Enter Command:...")

        if line.find("generator") > -1 and line.find("alter") == -1:

            #mode 1 for verifying
            return message , generator ,"1" , 0 ;

        elif line.find("generator") > -1 and line.find("alter") > -1:

            # mode 2 for altering
            alter_bit = line[line.find("alter") + 6]
            return message , generator , "2" , alter_bit

