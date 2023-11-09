# write a python code using functions to calculate area and perimeter of circle, rectangle
pi=22/7

def area_circle(r):
    area=pi*r*r
    return area
# verified

def peri_circle(r):
    peri=2*pi*r
    return peri
#verified

def area_rectangle(l,b):
    area=l*b
    return area
#verified

def peri_rectangle(l,b):
    peri=2*(l+b)
    return peri
# verified


polygon = ''
while(polygon!="exit"):
    polygon = input("Enter type of polygon or exit:")
    if (polygon=="circle"):
        r = float(input("Enter the radius of circle:"))
        property=''
        if(property==''):
            porperty=input("Enter the type of property:")
            if(property=="area"):
                print("hello",property=='area')
                '''print(area_circle(r))'''
            elif(property=="perimeter"):
                print(peri_circle(r))    

    elif(polygon=="rectangle"):
        l = float(input("Enter the length of rectangle:"))
        b = float(input("Enter the breadth of rectangle:"))
        property=''
        porperty=input("Enter the type of property:")
        print(property)
        if(property=="area"):
            print(area_rectangle(l,b))
        elif(property=="perimeter"):
            print(peri_rectangle(l,b))  

    elif(polygon=="exit"):
        break
    else:
        print("Select the correct polygon type or exit:")        