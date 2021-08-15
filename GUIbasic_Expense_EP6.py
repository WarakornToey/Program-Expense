from datetime import date, datetime # import datetime เอาไว้ใช้บันทึกเวลา
from tkinter import*
from tkinter import ttk, messagebox # ttk คือ theme of Tk // ,messagebox ทำ Poup Error ในภายใต้การทำงานของ try-except
import csv # import csv เข้ามาใช้ในการบันทึกข้อมูล
 
GUI = Tk()
GUI.title("Program Expense by TorToey")
GUI.geometry("600x700+500+50") # ตั้งค่าขนาด GUI (500+50)ขนาดเเสดงผลตามขนาดจอ

##### Menu Bar ######

menubar = Menu(GUI)
GUI.config(menu=menubar)

# File Menu
filemenu = Menu(menubar,tearoff=0) # tearoff=0 เอาเส้นประออก
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export to Googlesheet')

# Help Menu
def About(): # ใช้ฟังชันก์ในเมนู help ประกาศที่ให้ทำงาน command=About
	messagebox.showinfo('About','Please Danate For Me\nOne BTC Thank You BTC Address : A12B203Z')



helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)

# Donate Menu
donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)
donatemenu.add_command(label='Thank You')


#####################




Tab = ttk.Notebook(GUI) # ใช้ .Notebook เรียก Tab ขึ้นมาเเปะที่ GUI
T1 = Frame(Tab) # กำหนด T1 ให้อยู่ใน Frame (Tab) สารถใส่ค่า width= "" , height = "" ได้
T2 = Frame(Tab) # กำหนด T2 ให้อยู่ใน Frame (Tab) สารถใส่ค่า width= "" , height = "" ได้
Tab.pack(fill = BOTH, expand=1) # fill = BOTH, expand = 1 ให้ขยายเต็มพื้นที่

icon_1 = PhotoImage(file='T1_expanse.png') # ประกาศตัวเเปรเก็บรูปภาพรอเรียกใช้งาน // .subsample(2) = เอาไว้ย่อรูป
icon_2 = PhotoImage(file='T2_expanse.png') # ประกาศตัวเเปรเก็บรูปภาพรอเรียกใช้งาน
icon_3 = PhotoImage(file='T3_save.png') # ประกาศตัวเเปรเก็บรูปภาพรอเรียกใช้งาน


Tab.add(T1, text = f'{"Add Menu" :^{20}}',image = icon_1, compound = 'top') # ,image = icon_1, compound = 'top' นำรูปภาพมาใช้และจัดตำเเหน่งให้อยู่ด้านบน
# กำหนดค่าใช้ f-string ช่วยในการกำหนดให้อักษรอยู่ในระหว่าง 20 ตัวอักขระ f'{"Add Menu" :^{20}}' 
Tab.add(T2, text = f'{"Total Cost" :^{20}}',image = icon_2, compound = 'top') # กำหนดค่าใช้ f-string ช่วยในการกำหนดให้อักษรอยู่ในระหว่าง 20 ตัวอักขระ f'{"Add Menu" :^{20}}' 


F1 = Frame(T1) #Frame ใส่เฟรมให้กับ GUI
#F1.place(x=100, y=50) # กำหนดขนาด Frame
F1.pack() # เวลาขยายจะอยู่กึ่งกลาง 

days = {'Mon' : 'จันทร์', # ประกาศ List Days
		'Tue' : 'อังคาร',
		'Wed' : 'พุธ',
		'Thu' : 'พฤหัสบดี',
		'Fri' : 'ศุกร์',
		'Sat' : 'เสาร์',
		'Sun' : 'อาทิตย์'}

def save(event=None): # ประกาศฟังก์ชัน, event=None เป็นตัวรับค่าจากการกด Enter ที่ Keyboard
	expense = v_expense.get() # .get ดึงมาจาก v_expense = StringVar()
	price = v_price.get() # .get ดึงมาจาก v_price = StringVar()
	quantity = v_quantity.get()

	if expense == '':   # ใช้ if กำหนดเงื่อนไข
		print('No Data')
		messagebox.showwarning('Error', 'กรุณากรอกข้อมูลให้ครบ')
		return
	elif price == '': # ใช้ elif กำหนดเงื่อนไขและเเสดง messagebox
		messagebox.showwarning('Error', 'กรุณากรอกราคา (Price)')
		return
	elif quantity == '': # ใช้ elif กำหนดเงื่อนไขและเเสดง messagebox
		messagebox.showwarning('Error', 'กรุณากรอกจำนวน (Quantity)')
		return

	try: 

		total = int(price) * int(quantity)

		print("Detail : {} Price : {} ฿".format(expense,price))
		print("Quantity : {} Total : {} ".format(quantity,total))
		text = "Detail : {} Price : {} ฿\n".format(expense,price) # กำหนดค่าให้ตัวเเปร text เเสดงผล \n กำหนดให้เว้นบรรทัด
		text = text + "Quantity : {} Total : {} ".format(quantity,total) # นำข้อมความมารวมกัน
		v_result.set(text)
		
		v_expense.set("") # Clear ข้อมูลเก่าของรายการ
		v_price.set("") # Clear ข้อมูลเก่าราคา
		v_quantity.set("") # Clear ข้อมูลของจำนวน

		today = datetime.now().strftime('%a') # ประกาศตัวเเปร ตั้งค่าให้ function datetime.now()
		dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # กำหนดให้ใช้ลักษณะบ่งบอก วัน เดือน ปี เวลา ชั่วโมง นาที วินาที
		dt = days[today] + '-' + dt

		#บันทึกข้อมูล
		with open("Savedata.csv",'a',encoding='utf-8',newline='') as f:
		# with open สั่งการ เปิด-ปิดไฟล์ Auto,'a' คือการบันทึกเรื่อย ๆ เพิ่มข้อมูลจากตัวเก่า, newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
			fw = csv.writer(f) # สร้างฟังก์ชันสำหรับเขียนข้อมูล
			data = [dt,expense,price,quantity,total]
			fw.writerow(data)

			# ทำให้ Cursor กลับไปตำเเหน่ช่องกรอกเเรก E1
			E1.focus()
			update_table() # นำมาจาก fn update table เพื่อให้ตารางมีการ update // fn save ยังไม่มีการ Run จึงสามารถใช้งานก่อนประกาศ fn update ได้
	
	except:
		print('Error')
		#messagebox.showerror('Error', 'กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด') #.showeerror แสดง Popup แบบ Error 
		messagebox.showwarning('Warning', 'กรุณาตรวจสอบข้อมูล คุณกรอกตัวเลขผิด') #.showwarning แสดง Popup แบบ warning
		#messagebox.showinfo('Info', 'กรุณาตรวจสอบข้อมูล คุณกรอกตัวเลขผิด') #.showeinfo แสดง Popup แบบ info
		v_expense.set("") # Clear ข้อมูลเก่าของรายการ
		v_price.set("") # Clear ข้อมูลเก่าราคา
		v_quantity.set("") # Clear ข้อมูลของจำนวน

#ทำให้กด Enter ได้
GUI.bind('<Return>',save) # ต้องเพิ่มใน def save(event=None)ด้วย
	
FONT1 = (None,20) # FONT1 คือ การเปลี่ยนขนาด Font, None สามารถเปลี่ยนเป็น Angsana New ก็ได้

main_icon = PhotoImage(file = 'T4_list.png') # เรียกใช้งานรูป Main 
main_icon1 = Label(F1,image = main_icon) # ใช้ Label ในการเก็บรูปภาพหน้า Main ใส่ไว้ใน F1
main_icon1.pack()


L = ttk.Label(F1,text = "My Detail Expense",font = FONT1).pack() #ตั้งค่า Label ใน F1 พร้อมกำหนด font

v_expense = StringVar() # StringVar() คือตัวเเปรสำหรับเก็บข้อมุลใน GUI
E1 = ttk.Entry(F1,textvariable = v_expense,font = FONT1) # .Entry เป็นช่องว่างให้พิมพ์
E1.pack() # .pack เอาไว้เเปะกับ Frame F1
#----------------------------

L2 = ttk.Label(F1,text = "Price (฿)",font = FONT1).pack() #ตั้งค่า Label ใน F1 พร้อมกำหนด font

v_price = StringVar() # StringVar() คือตัวเเปรสำหรับเก็บข้อมุลใน GUI
E2 = ttk.Entry(F1,textvariable = v_price,font = FONT1) # .Entry เป็นช่องว่างให้พิมพ์
E2.pack() # .pack เอาไว้เเปะกับ Frame F1
#----------------------------

L3 = ttk.Label(F1, text = "Quantity (Item)",font = FONT1).pack()

v_quantity = StringVar()
E3 = ttk.Entry(F1, textvariable = v_quantity,font = FONT1)
E3.pack()


B2 = ttk.Button(F1, text = "Save",command=save, image = icon_3, compound = 'left') 
# เรียกปุ่มใช้งาน //,image = icon_1, compound = 'top' นำรูปภาพมาใช้และจัดตำเเหน่งให้อยู่ด้านบน
B2.pack(ipadx=50, ipady=20, pady=20) # .pack กำหนดที่อยู่ของปุ่มตามเเกน x,y

v_result = StringVar() # StringVar() คือตัวเเปรสำหรับเก็บข้อมุลใน GUI
v_result.set('-----------Result----------') # set ค่าข้อความ
result = ttk.Label(F1, textvariable = v_result,font = FONT1, foreground = 'green') # กำหนดตัวเเปรตั้งค่า font
result.pack(pady = 20) # เเสดงกำหนดค่า pady

############## TAB 2 ##############

def read_csv(): # ฟังก์ชัน read csv file
	with open('Savedata.csv', newline='',encoding='utf-8') as f: # ให้เปิดใช้ csv ตัวนี้ขึ้นมา #with open มีป้องกันไว้เมื่อลืม close ไฟล์ csv
		fr = csv.reader(f)
		data = list(fr)
	return data
		
############# Table ###############

L = ttk.Label(T2,text='Show All Tables', font=FONT1).pack(pady=20)

header = ['Date-Time','Menu','Price','Item','Result']
resulttable = ttk.Treeview(T2,columns = header, show = 'headings', height = 10) # Treeview ช่องแสดงตาราง
resulttable.pack()

#กำหนด Header ตาราง โดยใช้ For loop เนื่องจากข้อมูลชุดเดียวกัน
for h in header:
	resulttable.heading(h, text= h)

headerwidth = [150,170,80,80,80] # กำหนดความกว้าง Header ขนาดตาราง
                                    
for h,w in zip(header,headerwidth): # ใช้ For loop ในการจับคู่โดยใช้ zip ในการช่วย
	resulttable.column(h,width=w)

def update_table(): # สร้าง fn update ตาราง
	resulttable.delete(*resulttable.get_children()) # * การเเสดงผลแบบเทคนิค for loop 
	data = read_csv() # ดึง data csv

	for d in data:
		resulttable.column(h,width=w)

	print(data)
	resulttable.insert('',0, value=d)



update_table()
print('GET CHILD : ', resulttable.get_children())

GUI.bind('<Tab>'), lambda x: E2.focus()
GUI.mainloop()
