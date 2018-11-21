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
