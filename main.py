from tkinter import *
from tkinter import ttk
from helper import *
from PIL import Image, ImageTk

main = Tk()
main.title("Water Potability Checker")

frame1 = Frame(main)
# frame1.configure(background=bgImage)
bgImage = ImageTk.PhotoImage(Image.open("pharmaceutical-water.png"))
bgImageContainer = Label(frame1,image=bgImage,bg="#000000")
bgImageContainer.pack()
frame2 = Frame(main)
frame1.pack()
frame2.pack()

frame2.columnconfigure(0,weight=1)
frame2.columnconfigure(1,weight=1)

font_tuple_header = ("Liberation Mono",20,"bold")
font_tuple = ("Liberation Mono",20)

# image_holder = Label(frame1,i=PhotoImage("pharmaceutical-water.png"))
# image_holder.pack()

header = Label(frame2,text="Enter details",justify="center",font=font_tuple_header)
header.grid(row=0,column=0,columnspan=2)

lab1 = Label(frame2,text="Ph",font=font_tuple)
lab1.grid(row=1,column=0)
lab2 = Label(frame2,text="Hardness",font=font_tuple)
lab2.grid(row=2,column=0)
lab3 = Label(frame2,text="Solids",font=font_tuple)
lab3.grid(row=3,column=0)
lab4 = Label(frame2,text="Chloramines",font=font_tuple)
lab4.grid(row=4,column=0)
lab5 = Label(frame2,text="Sulfate",font=font_tuple)
lab5.grid(row=5,column=0)
lab6 = Label(frame2,text="Conductivity",font=font_tuple)
lab6.grid(row=6,column=0)
lab7 = Label(frame2,text="Organic Carbon",font=font_tuple)
lab7.grid(row=7,column=0)
lab8 = Label(frame2,text="Trihalomethanes",font=font_tuple)
lab8.grid(row=8,column=0)
lab9 = Label(frame2,text="Turbidity",font=font_tuple)
lab9.grid(row=9,column=0)

inp1 = Entry(frame2)
inp1.grid(row=1,column=1,padx=8,pady=8)
inp2 = Entry(frame2)
inp2.grid(row=2,column=1,padx=8,pady=8)
inp3 = Entry(frame2)
inp3.grid(row=3,column=1,padx=8,pady=8)
inp4 = Entry(frame2)
inp4.grid(row=4,column=1,padx=8,pady=8)
inp5 = Entry(frame2)
inp5.grid(row=5,column=1,padx=8,pady=8)
inp6 = Entry(frame2)
inp6.grid(row=6,column=1,padx=8,pady=8)
inp7 = Entry(frame2)
inp7.grid(row=7,column=1,padx=8,pady=8)
inp8 = Entry(frame2)
inp8.grid(row=8,column=1,padx=8,pady=8)
inp9 = Entry(frame2)
inp9.grid(row=9,column=1,padx=8,pady=8)

out = Frame(frame2)
out.grid(row=11,column=0,columnspan=2)

def get_results():
    for x in out.winfo_children():
        x.destroy()
    try:
        output = get_pred(inp1.get(),inp2.get(),inp3.get(),inp4.get(),inp5.get(),inp6.get(),inp7.get(),inp8.get(),inp9.get())
        print(output)
        if(output[0]=="Not safe for drinking"):
            res = Label(out,text=output[0],fg="#e82a15")
            res.grid(row=11,column=0)
            Label(out,text="Reason:"+output[1],background="#dae815").grid(row=11,column=1)
        else:
            res = Label(out,text=output[0],fg="#2ae815")
            res.grid(row=11,column=0,columnspan=2)
    except ValueError:
        res = Label(out,text="Please enter proper values",fg="#e82a15")
        res.grid(row=11,column=0,columnspan=2)
        

btn = Button(frame2,text="Get Results",command=get_results)
btn.grid(row=10,column=0,columnspan=2)


if __name__=="__main__":
    main.mainloop()
