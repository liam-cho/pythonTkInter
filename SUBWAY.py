import tkinter as tk
from PIL import ImageTk,Image
win = tk.Tk()
win.geometry("1536x864")
def get_mouse_position(event):
    x = event.x  # 캔버스 기준 x 좌표
    y = event.y  # 캔버스 기준 y 좌표
    print(f"마우스 좌표: ({x}, {y})")



img = Image.open("Metro Line Map.png")
img = img.resize((1206,600))
image= ImageTk.PhotoImage(img)
#win.resizable(False,False)
canvas= tk.Canvas(win,relief='solid',bd=2,height=600,width=1206)
canvas.create_image(0,0,anchor='nw',image=image)
canvas.bind("<Button-1>", get_mouse_position)
#역 표시 원
화명역=canvas.create_oval(478,182,485,190,fill='pink')
수정역=canvas.create_oval(478,235,485,243,fill='pink')

R_frame=tk.Frame(win,relief='solid',border=2,width=330,height=861)
D_frame=tk.Frame(win,relief='solid',border=2,width=1203,height=264)

img1 = Image.open("IMG\95.png")
img1 = img1.resize((280,263))
image1= ImageTk.PhotoImage(img1)
label = tk.Label(D_frame,image=image1)
label.pack(side='left',padx=0,pady=0)


img2 = Image.open("IMG\95.png")
img2 = img2.resize((280,263))
image2= ImageTk.PhotoImage(img2)
label2 = tk.Label(D_frame,image=image2)
label2.pack(side='left',padx=0,pady=0)


R_frame.pack_propagate(False)
R_frame.pack(side='right',fill='both')

D_frame.pack_propagate(False)
D_frame.pack(side='bottom',fill='both')
canvas.pack(side='left',fill='both')


win.mainloop()