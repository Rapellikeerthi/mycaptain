#Area of circle

PI=3.14
r=float(input("Enter the radius of the circle:"))
area=PI*r*r
print("area of the circle =%f" %area)



#The extension of the file
filename=input("Input the Filename:")
f_extns=filename.split(".")
print("The extension of the file is:"+repr(f_extns[-1])) #Here extension of the file is given by repr function 
