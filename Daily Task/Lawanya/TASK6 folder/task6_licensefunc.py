my_plate=input("enter your license no.")
def licensedplate(x):
    if len(my_plate)==6 :
        my_plate[0] >= "A" and my_plate[0] <= "Z" 
        my_plate[1] >= "A" and my_plate[1] <= "Z" 
        my_plate[2] >= "A" and my_plate[2] <= "Z" 
        my_plate[3] >= "0" and my_plate[3] <= "9" 
        my_plate[4] >= "0" and my_plate[4] <= "9" 
        my_plate[5] >= "0" and my_plate[5] <= "9" 
        print("it is a valid older style plate no.")
    elif len(my_plate)==7 :
        my_plate[0] >= "0" and my_plate[0] <= "9" 
        my_plate[1] >= "0" and my_plate[1] <= "9" 
        my_plate[2] >= "0" and my_plate[2] <= "9" 
        my_plate[3] >= "0" and my_plate[3] <= "9" 
        my_plate[4] >= "A" and my_plate[4] <= "Z" 
        my_plate[5] >= "A" and my_plate[5] <= "Z" 
        my_plate[6] >= "A" and my_plate[6] <= "Z" 
        print("it is a valid newer style plate no.")
    else:
        return x
licensedplate(my_plate)   


    

