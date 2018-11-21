from longdiv import long_division

def verifier (transmitted_msg , generator_poly):

    poly_len = len(generator_poly)
    zeros = '0'*(poly_len - 1)

    msg = transmitted_msg + zeros

    remainder = long_division(msg , generator_poly)

    if remainder == zeros:

        print ("Correct!!")

    else:

        print("Error!!")
