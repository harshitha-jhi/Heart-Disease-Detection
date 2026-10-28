from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2 
import numpy as np
import pickle
import warnings
import random
warnings.filterwarnings('ignore')

class Application:
    def __init__(self,root):
        self.root = root
        self.status =False
        self.root.geometry('1000x650')
        self.root.title('Heart disease Detection')
        self,root.resizable(False,False)
        l=Label(self.root, text='Hello').pack()
        img = ImageTk.PhotoImage(Image.open('./bg.jpg').resize((673,588)))
        lb = Label(self.root, image= img,borderwidth=5,relief='solid')
        lb.image=img
        lb.place(x=305,y=50)
        
        lb1 = Label(self.root, text= "Heart disease Detection",width = 65,height =1,
                    bg= 'blue',font=('bold',19),borderwidth=5,relief='solid')

        lb1.place(x=3,y=1)
       

        age_lb = Label(self.root,text = 'Age', width = 10,font =('bold',15),
                    bg='indianred3',borderwidth =5,relief = 'solid')
        age_lb.place(x=320,y=60)

        sex_lb = Label(self.root,text = 'Sex', width = 10,font =('bold',15),
                    bg='indianred3',borderwidth =5,relief = 'solid')
        sex_lb.place(x=320,y=100)

        cp_lb = Label(self.root,text = 'CP', width = 10,font =('bold',15),
                    bg='indianred3',borderwidth =5,relief = 'solid')
        cp_lb.place(x=320,y=140)

        resting_bp_lb = Label(self.root,text = 'Resting Bp', width = 10,font =('bold',15),
                    bg='indianred3',borderwidth =5,relief = 'solid')
        resting_bp_lb.place(x=320,y=180)

        serum_cholesterol_lb = Label(self.root,text = 'Serum Cholesterol', width = 15,font =('bold',15),
                    bg='indianred3',borderwidth =5,relief = 'solid')
        serum_cholesterol_lb.place(x=320,y=220)

        fasting_blood_sugar_lb = Label(self.root,text = 'Fasting blood sugar', width = 16,font =('bold',15),
                    bg='indianred3',borderwidth =5,relief = 'solid')
        fasting_blood_sugar_lb.place(x=320,y=260)

        resting_ecg_lb = Label(self.root,text = 'Resting ECG', width = 15,font =('bold',15),
                    bg='indianred3',borderwidth =5,relief = 'solid')
        resting_ecg_lb.place(x=320,y=300)

        max_heart_rate_lb = Label(self.root,text = 'Max heart rate', width = 15,font =('bold',15),
                    bg='indianred3',borderwidth =5,relief = 'solid')
        max_heart_rate_lb.place(x=320,y=340)

        exercise_induced_angina_lb = Label(self.root,text = 'Exercise induced angina', width = 20,font =('bold',15),
                    bg='indianred3',borderwidth =5,relief = 'solid')
        exercise_induced_angina_lb.place(x=320,y=380)

        st_depression_lb = Label(self.root,text = 'St depression', width = 15,font =('bold',15),
                    bg='indianred3',borderwidth =5,relief = 'solid')
        st_depression_lb.place(x=320,y=420)

        st_slope_lb = Label(self.root,text = 'St_slope', width = 15,font =('bold',15),
                    bg='indianred3',borderwidth =5,relief = 'solid')
        st_slope_lb.place(x=320,y=460)

        number_of_vessels_lb = Label(self.root,text = 'Number of vessels', width = 16,font =('bold',15),
                    bg='indianred3',borderwidth =5,relief = 'solid')
        number_of_vessels_lb.place(x=320,y=500)

        thallium_scan_results_lb = Label(self.root,text = 'Thallium scan results', width = 17,font =('bold',15),
                    bg='indianred3',borderwidth =5,relief = 'solid')
        thallium_scan_results_lb.place(x=320,y=540)
        # *********************************Entry Box *************************************** #
        
        self.age = Entry(self.root, width = 20,font =('bold',15),
                    bg='snow',borderwidth =5,relief = RAISED  )
        self.age.place(x=650,y=60)

        self.sex = Entry(self.root, width = 20,font =('bold',15),
                    bg='snow',borderwidth =5,relief = RAISED)
        self.sex.place(x=650,y=100)

        self.cp = Entry(self.root, width = 20,font =('bold',15),
                    bg='snow',borderwidth =5,relief = RAISED)
        self.cp.place(x=650,y=140)

        self.resting_bp = Entry(self.root, width = 20,font =('bold',15),
                    bg='snow',borderwidth =5,relief = RAISED)
        self.resting_bp.place(x=650,y=180)

        self.serum_cholesterol = Entry(self.root, width = 20,font =('bold',15),
                    bg='snow',borderwidth =5,relief = RAISED)
        self.serum_cholesterol.place(x=650,y=220)

        self.fasting_blood_sugar = Entry(self.root, width = 20,font =('bold',15),
                    bg='snow',borderwidth =5,relief = RAISED)
        self.fasting_blood_sugar.place(x=650,y=260)

        self.resting_ecg = Entry(self.root, width = 20,font =('bold',15),
                    bg='snow',borderwidth =5,relief = RAISED)
        self.resting_ecg.place(x=650,y=300)

        self.max_heart_rate = Entry(self.root, width = 20,font =('bold',15),
                    bg='snow',borderwidth =5,relief = RAISED)
        self.max_heart_rate.place(x=650,y=340)

        self.exercise_induced_angina = Entry(self.root, width = 20,font =('bold',15),
                    bg='snow',borderwidth =5,relief = RAISED)
        self.exercise_induced_angina.place(x=650,y=380)

        self.st_depression = Entry(self.root, width = 20,font =('bold',15),
                    bg='snow',borderwidth =5,relief = RAISED)
        self.st_depression.place(x=650,y=420)

        self.st_slope = Entry(self.root, width = 20,font =('bold',15),
                    bg='snow',borderwidth =5,relief = RAISED)
        self.st_slope.place(x=650,y=460)

        self.number_of_vessels = Entry(self.root, width = 20,font =('bold',15),
                    bg='snow',borderwidth =5,relief = RAISED)
        self.number_of_vessels.place(x=650,y=500)

        self.thallium_scan_results = Entry(self.root, width = 20,font =('bold',15),
                    bg='snow',borderwidth =5,relief = RAISED)
        self.thallium_scan_results.place(x=650,y=540)
        self.frame1()

    def clear(self):
        self.lb4.destroy()
        self.age.delete('0', END)
        self.sex.delete('0', END)
        self.cp.delete('0', END)
        self.resting_bp.delete('0', END)
        self.serum_cholesterol.delete('0', END) 
        self.fasting_blood_sugar.delete('0', END)
        self.resting_ecg.delete('0', END) 
        self.max_heart_rate.delete('0', END) 
        self.exercise_induced_angina.delete('0', END) 
        self.st_depression.delete('0', END) 
        self.st_slope.delete('0', END)
        self.number_of_vessels.delete('0', END) 
        self.thallium_scan_results.delete('0', END) 
        self.status=False

    def SVM_PCA_prediction(self):
        self.a = self.age.get()
        self.b = self.sex.get()
        self.c =self.cp.get()
        self.d = self.resting_bp.get()
        self.e = self.serum_cholesterol.get()
        self.f = self.fasting_blood_sugar.get()
        self.g = self.resting_ecg.get()
        self.h = self.max_heart_rate.get()
        self.i = self.exercise_induced_angina.get()
        self.j =self.st_depression.get()
        self.k = self.st_slope.get()
        self.l = self.number_of_vessels.get()
        self.m = self.thallium_scan_results.get()
        
        if self.a == '' or self.b == '' or self.c =='' or  self.d == '' or self.e == '' or self.f == '' or self.g == '' or self.h == '' or self.i == '' or self.j =='' or self.k == '' or self.l == '' or self.m == '':
            messagebox.showinfo('Info','Entre requried data')
        else:
            self.status =True
            with open('./svm_pca_model_pk.pkl', 'rb') as pickle_model_file:
                pca_model = pickle.load(pickle_model_file)
                
            with open('./svm_pca_model.pkl', 'rb') as pickle_model_file:
                model = pickle.load(pickle_model_file)

            with open('./svm__pca_st1_model.pkl', 'rb') as pickle_st_file:
                st_model1 = pickle.load(pickle_st_file)
            with open('./svm__pca_st2_model.pkl', 'rb') as pickle_st_file:
                st_model2 = pickle.load(pickle_st_file)

            predict_data=np.array([[self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h,self.i,self.j,self.k,self.l,self.m]])
            st_predict_data = st_model1.transform(predict_data)
            pca_predict_data = pca_model.transform(st_predict_data)
            st_predict_data = st_model2.transform(pca_predict_data)
            self.category = model.predict(st_predict_data)
            if self.category[0] == 0:
                self.result = 'Normal'
            else:
                self.result = 'Heart disease'
            
            self.lb4 = Label(self.root, text='' ,width = 20,height =1,
                        bg= '#7FFF00',font=('bold',19),borderwidth=2,relief='groove')

            self.lb4.place(x=400,y=600)
            self.lb4.config(text = f'Prediction : {self.result}')         
    def SVM_prediction(self):
        self.a = self.age.get()
        self.b = self.sex.get()
        self.c =self.cp.get()
        self.d = self.resting_bp.get()
        self.e = self.serum_cholesterol.get()
        self.f = self.fasting_blood_sugar.get()
        self.g = self.resting_ecg.get()
        self.h = self.max_heart_rate.get()
        self.i = self.exercise_induced_angina.get()
        self.j =self.st_depression.get()
        self.k = self.st_slope.get()
        self.l = self.number_of_vessels.get()
        self.m = self.thallium_scan_results.get()
        
        if self.a == '' or self.b == '' or self.c =='' or  self.d == '' or self.e == '' or self.f == '' or self.g == '' or self.h == '' or self.i == '' or self.j =='' or self.k == '' or self.l == '' or self.m == '':
            messagebox.showinfo('Info','Entre requried data')
        else:
            self.status =True
            
            with open('./svm_model.pkl', 'rb') as pickle_model_file:
                model = pickle.load(pickle_model_file)

            with open('./svm_st_model.pkl', 'rb') as pickle_st_file:
                st_model = pickle.load(pickle_st_file)

            predict_data=np.array([[self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h,self.i,self.j,self.k,self.l,self.m]])
            st_predict_data = st_model.transform(predict_data)
            self.category = model.predict(st_predict_data)
            if self.category[0] == 0:
                self.result = 'Normal'
            else:
                self.result = 'Heart disease'
            
            self.lb4 = Label(self.root, text='' ,width = 20,height =1,
                        bg= '#7FFF00',font=('bold',19),borderwidth=2,relief='groove')

            self.lb4.place(x=400,y=600)
            self.lb4.config(text = f'Prediction : {self.result}')        

    def RF_prediction(self):
        self.a = self.age.get()
        self.b = self.sex.get()
        self.c =self.cp.get()
        self.d = self.resting_bp.get()
        self.e = self.serum_cholesterol.get()
        self.f = self.fasting_blood_sugar.get()
        self.g = self.resting_ecg.get()
        self.h = self.max_heart_rate.get()
        self.i = self.exercise_induced_angina.get()
        self.j =self.st_depression.get()
        self.k = self.st_slope.get()
        self.l = self.number_of_vessels.get()
        self.m = self.thallium_scan_results.get()
        
        if self.a == '' or self.b == '' or self.c =='' or  self.d == '' or self.e == '' or self.f == '' or self.g == '' or self.h == '' or self.i == '' or self.j =='' or self.k == '' or self.l == '' or self.m == '':
            messagebox.showinfo('Info','Entre requried data')
        else:
            self.status =True
            with open('./RF_model.pkl', 'rb') as pickle_model_file:
                model = pickle.load(pickle_model_file)

            with open('./RF_st_model.pkl', 'rb') as pickle_st_file:
                st_model = pickle.load(pickle_st_file)

            predict_data=np.array([[self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h,self.i,self.j,self.k,self.l,self.m]])
            st_predict_data = st_model.transform(predict_data)
            self.category = model.predict(st_predict_data)
            if self.category[0] == 0:
                self.result = 'Normal'
            else:
                self.result = 'Heart disease'
            
            self.lb4 = Label(self.root, text='' ,width = 20,height =1,
                        bg= '#7FFF00',font=('bold',19),borderwidth=2,relief='groove')

            self.lb4.place(x=400,y=600)
            self.lb4.config(text = f'Prediction : {self.result}')
        
            

        

    def frame1(self):
        self.frm = Frame(self.root, width=300, height=600, bg='#9932CC',
                         borderwidth=5,relief='solid')
        self.frm.place(x=1,y=50)
        btn1 = Button(self.frm, text=' RF model',font=('bold',10),width=20,
                      borderwidth=4,relief='flat',bd=10,fg = '#37d3ff',bg = '#001d26',
                      highlightcolor="#37d3ff", highlightbackground="#37d3ff",
                      activebackground='#FF8C00',command =self.RF_prediction)
        btn1.place(x=20,y=10)

        btn2 = Button(self.frm, text=' SVM model',font=('bold',10),width=20,
                      borderwidth=4,relief='flat',bd=10,fg = '#37d3ff',bg = '#001d26',
                      highlightcolor="#37d3ff", highlightbackground="#37d3ff",
                      activebackground='#FF8C00',command =self.SVM_prediction)
        btn2.place(x=20,y=100)

        btn3 = Button(self.frm, text=' SVM PCA model',font=('bold',10),width=20,
                      borderwidth=4,relief='flat',bd=10,fg = '#37d3ff',bg = '#001d26',
                      highlightcolor="#37d3ff", highlightbackground="#37d3ff",
                      activebackground='#FF8C00',command =self.SVM_PCA_prediction)
        btn3.place(x=20,y=200)

        btn4 = Button(self.frm, text='Clear',font=('bold',10),width=20,
                      borderwidth=4,relief='flat',bd=10,fg = '#37d3ff',bg = '#001d26',
                      highlightcolor="#37d3ff", highlightbackground="#37d3ff",
                      activebackground='#FF8C00',command =self.clear)
        btn4.place(x=20,y=300)
   


if __name__ == '__main__':

    root = Tk()
    Application(root)
    root.mainloop()
