import tkinter

# screen
screen = tkinter.Tk()
screen.title("BMI calculator")
screen.minsize(300,250)
screen.config(padx=20,pady=20)
 
FONT = ("Arial",10,"normal")


# wight label
weight_label = tkinter.Label(text="Please enter your weight(kg)",font=FONT)
weight_label.config(padx=5,pady=5)
weight_label.pack()

#weight entry
weight_Entry = tkinter.Entry()
weight_Entry.config(bg="light blue")
weight_Entry.pack()


# height label
height_label = tkinter.Label(text="Please enter your height(cm)",font=FONT)
height_label.config(padx=5,pady=5)
height_label.pack()

#height entry 
height_entry = tkinter.Entry()
height_entry.config(bg="light blue")
height_entry.pack()



#result label 
result_label = tkinter.Label(text="")





# get items
def geetting():
    weight = weight_Entry.get()
    height = height_entry.get()
    try:
        weight = int(weight)
        height = int(height)
        
        resultFunc(weight=weight, height=height)
        result_label.pack()
    except:
        result_label.config(text="Please enter integers !!")
        result_label.pack()


# result func
def resultFunc(weight,height):
    height = height/100
    result = weight/ (height**2)
    result = round(result,2)
    if result <18.5:
            variable_of_result = "you are weak"
            result_label.config(text=f"{variable_of_result} {result}")
    elif 18.5 <= result <= 24.9:
            variable_of_result = "you are normal"
            result_label.config(text=f"{variable_of_result} {result}")
    elif 25 <= result <= 29.9:
            variable_of_result = "you are fat"
            result_label.config(text=f"{variable_of_result} {result}")
    elif 30 <= result <= 34.9:
            variable_of_result = "you are obase"
            result_label.config(text=f"{variable_of_result} {result}")
    elif result >= 35 :
            variable_of_result = "you are morbid obase"
            result_label.config(text=f"{variable_of_result} {result}")


    
# calculator button
calculate_button = tkinter.Button(text="calculate",command=geetting)
calculate_button.config(padx=5,pady=5)
calculate_button.pack()


screen.mainloop()