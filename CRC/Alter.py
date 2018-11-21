def Alter (message_generator , to_change_bit):

    # Reverse the required bit
    reversed_bit = message_generator[to_change_bit-1]
    if reversed_bit == '1' 
        reversed_bit = '0'
    elif reversed_bit == '0' 
        reversed_bit = '1'
    # The edited message
    message_recieved = message_generator [0:to_change_bit-1] + reversed_bit + message_generator [to_change_bit:]
    
    return message_recieved 


