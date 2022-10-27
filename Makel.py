# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:14:43 2022

@author: bolat
"""

import matplotlib.pyplot  as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np 


class Spring:
    
    def __init__(self,k = float("Nan"),force = float("nan"),deflection = float("nan"),diameter = float("Nan")):
        self.k = k
        self.force = force
        self.deflection = deflection
        self.diameter = diameter 
        self.radius = diameter/2
    
    def spring_rate(self,force,deflection):
        if(self.k != float("Nan")):
            self.k = force/deflection
            print("Spring rate(yay sabiti) : {}".format(self.k))
                
            return self.k
    
    def spring_strengt(self,diameter):
        
        data = {"Material" : ["Music Wire","Oil-tempred Wire","Hard-drawn Wire","Chrome-vanadium","chrome silicone"],
                "Size range down(mm)" : [0.1,0.5,0.7,0.8,1.6],
                "Size range up(mm)" : [6.5,12,12,12,10],
                "Exponent, m" : [0.146,0.186,0.192,0.167,0.112],
                "Constant ,A(Mpa.mm^m)" : [2170,1880,1750,2000,200]}
        df = pd.DataFrame(data)
        
        cevap = input("Default olarak Hard-drawn wire kullaniyorum degistirmek istiyormusun Y/n : \n")
        secim = True
        
        while(secim):
            if(cevap == "n" or cevap == "N"):
                self.material = df[["Material","Size range down(mm)","Size range up(mm)","Exponent, m","Constant ,A(Mpa.mm^m)"][2]]
                
                secim == False 
                
            elif(cevap == "y" or cevap == "Y"):
                print(df[["Material","Size range down(mm)","Size range up(mm)"]])
                mat_num = int(input("Yukaridaki tabloadan malzemeninin indexinu ver : \n"))
                self.material = df[["Material","Size range down(mm)","Size range up(mm)","Exponent, m","Constant ,A(Mpa.mm^m)"][mat_num]]
                
                if(diameter >= self.material["Size range down(mm)"][mat_num] and diameter <=self.material["Size range up(mm)"][mat_num]):
                    print("Verdigin diameter uygun \n")
                    
                    secim == False 
                
                else : 
                    
                    secim == True
      
        

class k_value():
    
    
    def __init__(self):
        pass
    
    
    def ka(self,s,plot):
        
        x = np.array([0.4,0.6,0.8,1.0,1.2,1.4,1.6]).reshape((-1,1))
        y = np.array([1,0.74,0.7,0.67,0.65,0.63,0.62])
        
        poly = PolynomialFeatures(degree = 6)
        x_poly = poly.fit_transform(x)
        
        reg = LinearRegression()
        
        lin = reg.fit(x_poly,y)
    
    
        pre_x = np.linspace(0,1.6,100).reshape(-1,1)
        pre_y = lin.predict(poly.fit_transform(pre_x))
    
        su = np.array(s).reshape(-1,1)
    
        ans_x = lin.predict(poly.fit_transform(su))
        
        if(plot == True):
            plt.scatter(x,y)
            plt.scatter(su,ans_x,color="red" ,label ="istenilen ka degeri")
            plt.plot(pre_x,pre_y)
            plt.xlabel("ultimate strenght GPa")
            plt.xlim(0,1.7)
            plt.ylim(0.5, 1)
            plt.ylabel("Surface Factor ka")
            plt.legend()
            
            plt.show()
        
        print("ka sabiti degeri : {}".format(round(float(ans_x),3)))
        return round(float(ans_x),3)


    def kb(self,m,plot = False):
    
        M = np.array([1,2,2.25,2.5,2.75,3,3.5,4,4.5,5,5.5,6,7,8,9,
                  10,11,12,14,16,18,20,22,25,28,32,36,40,45,50]).reshape(-1,1)
        kB = np.array([1,1,0.984,0.974,0.965,0.956,0.942,0.930,0.920,
                   0.910,0.902,0.894,0.881,0.870,0.860,0.851,0.843,
                  0.836,0.824,0.813,0.804,0.796,0.788,0.779,0.770,
                  0.760,0.752,0.744,0.736,0.728])
    
        poly = PolynomialFeatures(degree = 6)
        x_poly = poly.fit_transform(M)
    
        reg = LinearRegression()
    
        lin = reg.fit(x_poly,kB)
    
    
        pre_x = np.linspace(0,50,1000).reshape(-1,1)
        pre_y = lin.predict(poly.fit_transform(pre_x))
        
        m = np.array(m).reshape(-1,1)
    
        ans_x = lin.predict(poly.fit_transform(m))
        
        if(plot == True):
            plt.scatter(M,kB,s=1)
            plt.scatter(m,ans_x,color="red" ,label ="istenilen kb degeri")
            plt.plot(pre_x,pre_y)
            plt.xlabel("module")
            plt.ylabel("Size factor kb")
            plt.legend()
        
            plt.show()
            
            print("kb degeri : {}".format(round(float(ans_x),3)))
    
        return round(float(ans_x),3)


    def kc(self,r):
    
        R  =pd.DataFrame(data= {"reliability":[0.5,0.9,0.95,0.99,0.999,0.9999],
       "Factor kc":[1.0,0.897,0.868,0.814,0.753,0.702]})
    
        for i in range(0,len(R["reliability"])):
        
            if R["reliability"][i] ==  r:
                return R["Factor kc"][i]
        
        
    def kd(self,t=350):
        if t<=350:
            return 1
        elif t>350 or t<500:
            return 0.5
            

        