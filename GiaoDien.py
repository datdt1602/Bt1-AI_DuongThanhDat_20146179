import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
from keras.models import load_model
from keras.utils import img_to_array
model = load_model('Final_Test_cnn.h5')

#initialise GUI
top=tk.Tk()
top.geometry('800x600')
top.title('NHẬN DẠNG CÁC LOẠI BỆNH TRÊN CÂY QUÝT')
top.configure(background='#FFFFFF')
label=Label(top,background='#FFFFFF', font=('arial',15,'bold'))
sign_image = Label(top)
def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((40,40))
    image = img_to_array(image)
    Test_image = np.expand_dims(image, axis=0)
    #pred = np.argmax(model.predict(image), axis=-1)
    result = (model.predict(Test_image) > 0.5).astype("int32")
    #result = np.argmax(model.predict(Test_image), axis=-1)
    print(result)
    x=0
    c=0
    i=0
    while (i<5):
        if result[0][i]>= x:
            x=result[0][i]
            c=i
        i=i+1
    if (x<=0 and c>=4) :
        c = 4
    if c == 0:
        prediction = 'Brown rot'
    elif c == 1:
        prediction = 'Brown rot'
    elif c == 2:
        prediction = 'Fissure craking'
    elif c == 3:
        prediction = 'Root rot yellow leaf'
    elif c == 4:
        prediction = 'Scabies'

    label.configure(foreground='#B20000', text=prediction, font=('arial',24,'bold'))
def show_classify_button(file_path):
    classify_b=Button(top,text="Classify Image",
   command=lambda: classify(file_path),
   padx=12,pady=5)
    classify_b.configure(background='#364156', foreground='white',
font=('arial',13,'bold'))
    classify_b.place(relx=0.79,rely=0.46)
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),
    (top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass
upload=Button(top,text="Upload an image",command=upload_image,padx=12,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',13,'bold'))
upload.pack(side=BOTTOM,pady=40)
sign_image.pack(side=BOTTOM,expand=True)
print(sign_image)

label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="NHẬN DẠNG CÁC LOẠI BỆNH TRÊN CÂY QUÝT",pady=20, font=('arial',20,'bold'))
heading.configure(background='#FFFFFF',foreground='#B20000')
heading.pack()
top.mainloop()

