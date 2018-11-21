# Returns XOR of 'a' and 'b' 
# (both of same length) 
def xor (a, b): 
  
    # initialize result 
    result = [] 
  
    # Traverse all bits, if bits are 
    # same, then XOR is 0, else 1 
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result.append('0') 
        else: 
            result.append('1') 
  
    return ''.join(result)

	
def Long_division (divident, divisor): 
  
    # Number of bits to be XORed at a time. 
    pick = len(divisor) 
  
    # Slicing the divident to appropriate 
    # length for particular step 
    tmp = divident[0 : pick] 
  
    while pick < len(divident): 
  
        if tmp[0] == '1': 
  
            # replace the divident by the result 
            # of XOR and pull 1 bit down 
            tmp = xor(divisor, tmp) + divident[pick] 
  
        else:   # If leftmost bit is '0' 
            # If the leftmost bit of the dividend (or the 
            # part used in each step) is 0, the step cannot 
            # use the regular divisor; we need to use an 
            # all-0s divisor. 
            tmp = xor('0'*pick, tmp) + divident[pick] 
  
        # increment pick to move further 
        pick += 1
  
    # For the last n bits, we have to carry it out 
    # normally as increased value of pick will cause 
    # Index Out of Bounds. 
    if tmp[0] == '1': 
        tmp = xor(divisor, tmp) 
    else: 
        tmp = xor('0'*pick, tmp) 
  
    checkword = tmp 
    return checkword 
	
	
def Generator ():
    with open('Input.txt' , 'r') as Input :
        # takes the input in an array 
        content = Input.readlines()
        content = [x.strip() for x in content] 
        data = content[0]
        key = content[1]
        
        # to find the length of the key
        l_key = len(key) 
  
        # Appends n-1 zeroes at end of data 
        appended_data = data + '0'*(l_key-1) 
        remainder = Long_division(appended_data, key) 
  
        # Append remainder in the original data 
        codeword = data + remainder
        
        # Create output file contain the transmitted message
        with open('Transmitted_message.txt' , 'w') as output :
            output.write(str(codeword))
            
        return (str(codeword))
		
		
def Alter (message_generator , to_change_bit):

    # Get required bit
    reversed_bit = message_generator[int(to_change_bit)-1]
    
    # XOR the bit we want to reverse
    if reversed_bit == '1' :
        reversed_bit = '0'
    elif reversed_bit == '0' :
        reversed_bit = '1'
        
    # The edited message
    message_recieved = message_generator [0:int(to_change_bit)-1] + reversed_bit + message_generator [int(to_change_bit):]
    
    return message_recieved 
	
	
def verifier (transmitted_msg , generator_poly):

    poly_len = len(generator_poly)
    zeros = '0'*(poly_len - 1)

    msg = transmitted_msg + zeros

    remainder = Long_division(msg , generator_poly)

    with open('Verifier_message.txt' , 'w') as output :
        if remainder == zeros:
            output.write("message is Correct :D")

        else:
            output.write("message is not Correct :(")
			

def parser ():
    
    Data = open("Input.txt")
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
			

def main () :
    message,generator,mode,alter_bit = parser()
    
    # Incase of "generator <file | verifier" command
    if mode == '1' :
        transmitted_msg = Generator ()
        verifier (transmitted_msg , generator)
    
    # Incase of "generator <file | alter arg | verifier" command
    elif mode == '2' :
        transmitted_msg = Alter (Generator () , alter_bit)
        verifier (transmitted_msg , generator)
        
    else :
        print("undefined input command ! \n")
		
		
		
# Run the whole program 
main()