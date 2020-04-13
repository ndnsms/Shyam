
from tkinter import *


from tkinter import messagebox


from tkinter import ttk


from datetime import date

 
def clearAll() : 
  
    dayField.delete(0, END) 
    monthField.delete(0, END) 
    yearField.delete(0, END) 
    givenDayField.delete(0, END) 
    givenMonthField.delete(0, END) 
    givenYearField.delete(0, END) 
    rsltDayField.delete(0, END) 
    rsltMonthField.delete(0, END) 
    rsltYearField.delete(0, END) 



def checkError() : 
  
  
    if (dayField.get() == "" or monthField.get() == "" 
        or yearField.get() == "" or givenDayField.get() == "" 
        or givenMonthField.get() == "" or givenYearField.get() == "") : 
  
       
        messagebox.showerror("Input Error") 
  
       
        clearAll() 
          
        return -1


def calculateAge():
    
    #check for error
    value = checkError()

    

   
    if value==-1:
        return

    else:
        
        birth_day = int(dayField.get()) 
        birth_month = int(monthField.get()) 
        birth_year = int(yearField.get()) 
  
        given_day = int(givenDayField.get()) 
        given_month = int(givenMonthField.get()) 
        given_year = int(givenYearField.get()) 
          
          
      
        month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
          
        if (birth_day > given_day): 
            given_month = given_month - 1
            given_day = given_day + month[birth_month-1]  
                      
                      
     
        if (birth_month > given_month): 
            given_year = given_year - 1
            given_month = given_month + 12
                      
        # calculate day, month, year  
        calculated_day = given_day - birth_day;  
        calculated_month = given_month - birth_month;  
        calculated_year = given_year - birth_year; 
  
        # calculated day, month, year write back 
        # to the respective entry boxes 
  
        # insert method inserting the   
        # value in the text entry box. 
          
        rsltDayField.insert(10, str(calculated_day)) 
        rsltMonthField.insert(10, str(calculated_month)) 
        rsltYearField.insert(10, str(calculated_year))



if __name__ == '__main__':

    
    root = Tk()


    root.config(background='cyan')

  
    root.title('Age Calculator ')

    root.geometry('525x220')

    dob = Label(root, bg = 'blue')

   
    givenDate = Label(root, text='Age at the Date',font=("Arial Bold", 16),fg = "white" , bg = 'blue')

   
    birthDate = Label(root, text='Date of Birth',font=("Arial Bold", 16),fg = "white" ,bg = 'blue')


    day = Label(root, text = 'Day',bg = "cyan")

   
    month = Label(root, text = 'Month',bg = "cyan")


    year = Label(root, text = 'Year',bg = "cyan")

  
    givenDay = Label(root, text = "Given Day", bg = "cyan")

 
    givenMonth = Label(root, text = "Given Month", bg = "cyan")

    
    givenYear = Label(root, text = "Given Year", bg = "cyan")


    rsltYear = Label(root, text = "Years",font=("Arial Bold", 12), bg = "cyan")

   
    rsltMonth = Label(root, text = "Month",font=("Arial Bold", 12), bg = "cyan") 

    rsltDay = Label(root, text = "Days",font=("Arial Bold", 12), bg = "cyan")

   
    dayField = Entry(root)
    monthField = Entry(root)
    yearField = Entry(root)
  
    givenDayField = Entry(root)
    givenMonthField = Entry(root)
    givenYearField = Entry(root) 
      
    rsltYearField = Entry(root) 
    rsltMonthField = Entry(root) 
    rsltDayField = Entry(root)

   
   

    resultantAge = Button(root, text = "Calculate Age", fg = "Black", bg = "pink", command = calculateAge,font=("Arial Bold", 12))


    clearAllEntry = Button(root, text = "Check Another", fg = 'Black', bg = 'pink', command = clearAll,font=("Arial Bold", 12))

    
    dob.grid(row = 0, column = 1) 
      
    day.grid(row = 2, column = 0) 
    dayField.grid(row = 2, column = 1) 
      
    month.grid(row = 3, column = 0) 
    monthField.grid(row = 3, column = 1) 
      
    year.grid(row = 4, column = 0) 
    yearField.grid(row = 4, column = 1) 
      
    givenDate.grid(row = 0, column = 4)
    birthDate.grid(row = 0, column = 1) 
      
    givenDay.grid(row = 2, column = 3) 
    givenDayField.grid(row = 2, column = 4) 
      
    givenMonth.grid(row = 3, column = 3) 
    givenMonthField.grid(row = 3, column = 4) 
      
    givenYear.grid(row = 4, column = 3) 
    givenYearField.grid(row = 4, column = 4)
      
    resultantAge.grid(row = 11, column = 3) 
      
    rsltYear.grid(row = 7, column = 2) 
    rsltYearField.grid(row = 7, column = 3) 
      
    rsltMonth.grid(row = 8, column = 2) 
    rsltMonthField.grid(row = 8, column = 3) 
      
    rsltDay.grid(row = 9, column = 2) 
    rsltDayField.grid(row =9, column = 3) 

   
    clearAllEntry.grid(row = 11, column = 4)

    
    root.mainloop()
  

