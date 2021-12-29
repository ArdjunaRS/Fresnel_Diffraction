import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate




def mysimpson1d(n,a,b,z,x,x_upper):
    xplots=[]
    yplots=[]

    
    
    f= lambda xpr: ((k)/(2*np.pi*0.02)) *np.exp(((k*1j)/(2*z))*((x-xpr)**2))
    while (x<x_upper):
        dxpr=(b-a)/n

        s=0.5*(f(a)+f(b))
        for i in range(1,n):
            if i % 2 == 0:
                s += f(a+i*dxpr)*2 #from the fact that x1=a+h, x2=a+2h etc
            else:
                s += f(a+i*dxpr)*4
        integral = ((dxpr/3)*s) 
        x +=0.00001
        xplots.append(x)
        yplots.append(abs(integral)**2)
    
    return xplots, yplots

k = (2*np.pi)/(1e-6)
a=0




########### FUNCTIONS FOR PART C
########## 1
def mysimpson(z,k,x,xprime):
    integral=np.exp(((k*1j)/(2*z))*((x-xprime)**2))
    return integral


########## 2
def mysimpson_y(yprime):
    function=np.exp(((k*1j)/(2*z))*((y-yprime)**2))
    return function

########## 3
def integral_x(n,xa,xb,ya,yb,x,mysimpson,y):
    x_integrals=[]
    dx = np.linspace(xa, xb, n) #this is the step size
    x_integrals.append(mysimpson(z,k,x,dx)) #this puts the integral values into a list
    np.asarray(x_integrals) #this changes the format of the list to an array
    final_integral= integrate.simps(x_integrals,dx)*integral_y(n,y,ya,yb)  
    return final_integral
    
########## 4
def integral_y(n,y,ya,yb):
    y_integrals= []
    dy= np.linspace(ya,yb, n)
    y_integrals.append(mysimpson_y(dy)) #notice that yprime replaced with dy, same for ##### 3
    np.asarray(y_integrals)
    final_integral_y= integrate.simps(y_integrals, dy)
    return final_integral_y


############################ INPUT FUNCTIONS
def asking_x():
    asking_x_range= input("Would you like to: \n(a) keep the default screen coordinate range (-0.005 to 0.005 m) \n(b) observe it near zero \n(c) chose your own? \nChoice: ")
    while asking_x_range != "a" or asking_x_range != "b" or asking_x_range != "c":
        if asking_x_range == "a":
            x=-0.005
            x_upper= 0.005
            break
        elif asking_x_range == "b":
            x=-0.001
            x_upper= 0.001  
            break

        elif asking_x_range == "c":
            myinput_x_lower= input("Please enter the lower bound of the screen coordinates: ")
            myinput_x_upper= input("Please enter the upper bound of the screen coordinates: ")
            x=float(myinput_x_lower)
            x_upper= float(myinput_x_upper)
            break

        else:
            asking_x_range= input("Please enter an option (a or b): ")
    return x, x_upper


def asking_z():
    myinput_z= float(input("Enter the distance from the aperture to the screen (cm): "))
    while myinput_z != float():
        if float(myinput_z)<0:
            myinput_z= input("Input a positive number: ")
        elif float(myinput_z)>=0:
            break
    z=float(myinput_z)*0.01
    print("you have chosen z = ",myinput_z," cm")
    return z


def asking_b():
    myinput_b= float(input("Enter the aperture width (x10^-5 m): "))
    while myinput_b != float():
        if float(myinput_b)<0:
            myinput_b= input("Input a positive number: ")
        elif float(myinput_b)>=0:
            break
    b=float(myinput_b)*1e-5
    print("you have chosen aperture width = ",myinput_b," x10^-5 m ")
    return b

def asking_n():
    myinput_n= float(input("Enter the number of intervals (default=100): "))
    while myinput_n != float():
        if float(myinput_n)<0:
            myinput_n= input("Input a positive number: ")
        elif float(myinput_n)>=0:
            break
    n=int(myinput_n)
    print("you have chosen  ",myinput_n," number of intervals")
    return n

MyInput = '0'
while MyInput != 'q':
    MyInput = input('Enter a choice: \n(a) To plot x against relative intensity with custom z, aperture width and N \n(b) To compare graphs of different z \n(c) To compare graphs of different aperture widths  \n(d) Compare N values  \n(e) Generate a 2D image of integration \n(q) Quit Programme \nChoice: ')
    print('You entered the choice: ',MyInput)
    
    if MyInput == 'a':
        print('You have chosen part (a)')
        
######################### OPTION A ###############################################################\
        
        x,x_upper=(asking_x())
        z=(asking_z())
        b=(asking_b())
        n=asking_n()
        
        xplots=mysimpson1d(n,a,b,z,x,x_upper)[0]
        yplots=mysimpson1d(n,a,b,z,x,x_upper)[1]
        plt.plot(xplots,yplots)
        plt.xlabel("Screen Coordinates (m)")
        plt.ylabel("Relative Intensity")
        plt.show()

######################### OPTION B ###############################################################

    elif MyInput == 'b':
        print('You have chosen part (b)')
        
        
        x,x_upper=(asking_x())
        
        n=asking_n()
        b=2e-5
        z=0.02

        myinputz1=input("Input your first z value (cm): ")
        myinputz2=input("Input your second z value (cm): ")
        myinputz3=input("Input your third z value (cm): ")
        myinputz4=input("Input your fourth z value (cm): ")
        myinputz5=input("Input your fifth z value (cm): ")

        
        z1=float(myinputz1)*0.01
        z2=float(myinputz2)*0.01
        z3=float(myinputz3)*0.01
        z4=float(myinputz4)*0.01
        z5=float(myinputz5)*0.01
        
        
        xplots=mysimpson1d(n,a,b,z,x,x_upper)[0]
        
        yplots1=[]
        yplots2=[]
        yplots3=[]
        yplots4=[]
        yplots5=[]
          
        yplots1=mysimpson1d(n,a,b,z1,x,x_upper)[1]
        yplots2=mysimpson1d(n,a,b,z2,x,x_upper)[1]
        yplots3=mysimpson1d(n,a,b,z3,x,x_upper)[1]
        yplots4=mysimpson1d(n,a,b,z4,x,x_upper)[1]
        yplots5=mysimpson1d(n,a,b,z5,x,x_upper)[1]
        
        
        print("The lengths of the lists are: ")
        print(len(mysimpson1d(n,a,b,z,x,x_upper)[0]))
        print(len(mysimpson1d(n,a,b,z1,x,x_upper)[1]))
        print(len(mysimpson1d(n,a,b,z2,x,x_upper)[1]))
        print(len(mysimpson1d(n,a,b,z3,x,x_upper)[1]))
        print(len(mysimpson1d(n,a,b,z4,x,x_upper)[1]))
        print(len(mysimpson1d(n,a,b,z5,x,x_upper)[1]))

        plt.plot(xplots,yplots1,color='b', label= (myinputz1, "cm"))
        plt.plot(xplots,yplots2,color='g', label= (myinputz2, "cm"))
        plt.plot(xplots,yplots3,color='r', label= (myinputz3, "cm"))
        plt.plot(xplots,yplots4,color='c', label= (myinputz4, "cm"))
        plt.plot(xplots,yplots5,color='m', label= (myinputz5, "cm"))
        
        plt.title("variation of screen coordinates against Relative intensity with z")
        plt.legend()
        plt.xlabel("Screen Coordinates (m)")
        plt.ylabel("Relative Intensity")
        plt.show()
        
######################### OPTION C ###############################################################
    
    elif MyInput == 'c':
        print('You have chosen part (c)')
        
        x,x_upper=(asking_x())
        
        n=asking_n()
        z= 0.02
        myinputb1=input("Input your first b value (x10^-5): ")
        myinputb2=input("Input your second b value (x10^-5): ")
        myinputb3=input("Input your third b value (x10^-5): ")
        myinputb4=input("Input your fourth b value (x10^-5): ")
        myinputb5=input("Input your fifth b value (x10^-5): ")

        b1=float(myinputb1)*1e-5
        b2=float(myinputb2)*1e-5
        b3=float(myinputb3)*1e-5
        b4=float(myinputb4)*1e-5
        b5=float(myinputb5)*1e-5

        xplots=mysimpson1d(n,a,b,z,x,x_upper)[0]
        
        yplots1=[]
        yplots2=[]
        yplots3=[]
        yplots4=[]
        yplots5=[]
        

        yplots1=mysimpson1d(n,a,b1,z,x,x_upper)[1]
        yplots2=mysimpson1d(n,a,b2,z,x,x_upper)[1]
        yplots3=mysimpson1d(n,a,b3,z,x,x_upper)[1]
        yplots4=mysimpson1d(n,a,b4,z,x,x_upper)[1]
        yplots5=mysimpson1d(n,a,b5,z,x,x_upper)[1]
    
  
        plt.plot(xplots,yplots1,color='b', label= (myinputb1, "(x10^-5)"))
        plt.plot(xplots,yplots2,color='g', label= (myinputb2, "(x10^-5)"))
        plt.plot(xplots,yplots3,color='r', label= (myinputb3, "(x10^-5)"))
        plt.plot(xplots,yplots4,color='c', label= (myinputb4, "(x10^-5)"))
        plt.plot(xplots,yplots5,color='m', label= (myinputb5, "(x10^-5)"))
        
        
        
        plt.title("Variation Of screen coordinates against Relative intensity with aperture width")
        plt.legend()
        plt.xlabel("Screen Coordinates (m)")
        plt.ylabel("Relative Intensity")
        plt.show()

######################### OPTION D ###############################################################
    elif MyInput == 'd':
        x,x_upper=(asking_x())
        
        b=2e-5
        z= 0.02
        a=0
        n=asking_n()
        
        myinputn1=input("Input your first N value (multiple of 10): ")
        myinputn2=input("Input your second N value (multiple of 10): ")
        myinputn3=input("Input your third N value (multiple of 10): ")

        n1=int(myinputn1)
        n2=int(myinputn2)
        n3=int(myinputn3)

        
        xplots=mysimpson1d(n,a,b,z,x,x_upper)[0]

        yplots1=[]
        yplots2=[]
        yplots3=[]

        yplots1=mysimpson1d(n1,a,b,z,x,x_upper)[1]
        yplots2=mysimpson1d(n2,a,b,z,x,x_upper)[1]
        yplots3=mysimpson1d(n3,a,b,z,x,x_upper)[1]

        plt.plot(xplots,yplots1,color='b', label= (myinputn1))
        plt.plot(xplots,yplots2,color='g', label= (myinputn2))
        plt.plot(xplots,yplots3,color='r', label= (myinputn3))

 
        plt.title("Variation Of screen coordinates against Relative intensity with N")
        plt.legend()
        plt.xlabel("Screen Coordinates (m)")
        plt.ylabel("Relative Intensity")
        plt.show()
        
 ######################### OPTION E ##########################################################
    
    elif MyInput == 'e':
    ############ INPUTTING Z
        myinput_z= float(input("Enter the distance from the aperture to the screen (mm): "))
        while myinput_z != float():
            if float(myinput_z)<0:
                myinput_z= input("Input a positive number: ")
            elif float(myinput_z)>=0:
                break
        z=float(myinput_z)*0.0005
        
        print("you have chosen z = ",myinput_z," mm")
        
        ############ OPTION TO CHANGE THE LIMITS OF INTEGRATION FOR EACH FUNCTION (X AND Y)
        
        myinput_limits_option= input("Would you like to: \n(a) Use the default limits of integration (-0.0001 to 0.0001) \n(b) Use custom limits of integration \nChoice: ")
        if myinput_limits_option == 'a':
            xprime1, xprime2 = -0.0001,0.0001
            yprime1, yprime2 = -0.0001,0.0001
        elif myinput_limits_option == 'b':
            myinput_xprime1=input("Input x'1 (x10^-4): ")
            myinput_xprime2=input("Input x'2 (x10^-4): ")
            myinput_yprime1=input("Input y'1 (x10^-4): ")
            myinput_yprime2=input("Input y'2 (x10^-4): ")
            xprime1 = float(myinput_xprime1) * 1e-4
            xprime2 = float(myinput_xprime2) * 1e-4
            yprime1 = float(myinput_yprime1) * 1e-4
            yprime2 = float(myinput_yprime2) * 1e-4
        else:
            print("Please enter a valid option: ")
            

        x1, x2=-3e-4, 3e-4
        y1, y2=-3e-4, 3e-4
        k = (2*np.pi)/(1e-6)
        iterations = 20  
        n=asking_n()
        I = np.zeros((n,n))
        
        y=y1
        for i in range (0,n):
            x=x1
            for j in range (0,n):
                I[i,j] = abs((k/(2*z*np.pi))*integral_x(iterations,xprime1,xprime2,yprime1,yprime2,x,mysimpson,y)**2) #n becomes iterations
                x += (x2-x1)/(n-1)
            y += (y2-y1)/(n-1)
                
        im = plt.imshow(I,extent = [x1*1e6,x2*1e6,y1*1e6,y2*1e6])    
        plt.xlabel('x ($\mu$m)',fontsize = 15)
        plt.ylabel('y ($\mu$m)',fontsize = 15)
        plt.colorbar(label = 'Intensity (units)')
        plt.show()
        
    elif MyInput != 'q':
        print('This is not a valid choice')

    print('You have chosen to finish - goodbye.')
    
    
    
    
    
    
    
