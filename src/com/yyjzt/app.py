#!/usr/bin/env python
#-*- coding:utf-8 -*-
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

import os, sys,re,pygame,time,urllib,lxml,threading,time,requests,base64,json
import config
import http.cookiejar as cookielib
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from aip import AipSpeech 


class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('九州通数据采集系统')
        self.master.geometry('1272x734')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Data.TLabelframe',font=('宋体',9))
        self.Data = LabelFrame(self.top, text='数据', style='Data.TLabelframe')
        self.Data.place(relx=0.258, rely=0.011, relwidth=0.73, relheight=0.982)

        self.style.configure('Info.TLabelframe',font=('宋体',9))
        self.Info = LabelFrame(self.top, text='设置', style='Info.TLabelframe')
        self.Info.place(relx=0.006, rely=0.011, relwidth=0.246, relheight=0.982)

        self.style.configure('QuickViewFrame.TLabelframe',font=('宋体',9))
        self.QuickViewFrame = LabelFrame(self.Data, text='快速浏览', style='QuickViewFrame.TLabelframe')
        self.QuickViewFrame.place(relx=0.362, rely=0.022, relwidth=0.578, relheight=0.268)

        self.Picture1 = Canvas(self.QuickViewFrame)
        self.Picture1.place(relx=0.045, rely=0.166, relwidth=0.248, relheight=0.691)

        self.style.configure('QuickViewName.TLabel',anchor='w', font=('宋体',9))
        self.QuickViewName = Label(self.QuickViewFrame, text='品名', style='QuickViewName.TLabel')
        self.QuickViewName.place(relx=0.358, rely=0.166, relwidth=0.621, relheight=0.088)

        self.SearchKeywordTextVar = StringVar(value='在这里输入你要搜索的药物名称')
        self.SearchKeywordText = Entry(self.Data, text='在这里输入你要搜索的药物名称', textvariable=self.SearchKeywordTextVar, font=('宋体',9))
        self.SearchKeywordText.place(relx=0.103, rely=0.178, relwidth=0.208, relheight=0.037)

        self.SortComboThreeList = ['Add items in design or code!',]
        self.SortComboThree = Combobox(self.Data, values=self.SortComboThreeList, font=('宋体',9))
        self.SortComboThree.place(relx=0.146, rely=0.133, relwidth=0.165, relheight=0.028)
        self.SortComboThree.set(self.SortComboThreeList[0])

        self.SortComboTwoList = ['Add items in design or code!',]
        self.SortComboTwo = Combobox(self.Data, values=self.SortComboTwoList, font=('宋体',9))
        self.SortComboTwo.place(relx=0.146, rely=0.089, relwidth=0.165, relheight=0.028)
        self.SortComboTwo.set(self.SortComboTwoList[0])

        self.SortComboOneList = ['Add items in design or code!',]
        self.SortComboOne = Combobox(self.Data, values=self.SortComboOneList, font=('宋体',9))
        self.SortComboOne.place(relx=0.146, rely=0.044, relwidth=0.165, relheight=0.028)
        self.SortComboOne.set(self.SortComboOneList[0])

        self.List1Var = StringVar(value='List1')
        self.List1Font = Font(font=('宋体',9))
        self.List1 = Listbox(self.Data, listvariable=self.List1Var, font=self.List1Font)
        self.List1.place(relx=0.017, rely=0.244, relwidth=0.294, relheight=0.738)

        self.style.configure('SearchKeyWordLable.TLabel',anchor='w', font=('宋体',9))
        self.SearchKeyWordLable = Label(self.Data, text='检索关键字:', style='SearchKeyWordLable.TLabel')
        self.SearchKeyWordLable.place(relx=0.017, rely=0.178, relwidth=0.079, relheight=0.024)

        self.style.configure('SortLableThree.TLabel',anchor='w', font=('宋体',9))
        self.SortLableThree = Label(self.Data, text='药品分类3:', style='SortLableThree.TLabel')
        self.SortLableThree.place(relx=0.017, rely=0.133, relwidth=0.079, relheight=0.024)

        self.style.configure('SortLableTwo.TLabel',anchor='w', font=('宋体',9))
        self.SortLableTwo = Label(self.Data, text='药品分类2:', style='SortLableTwo.TLabel')
        self.SortLableTwo.place(relx=0.017, rely=0.089, relwidth=0.079, relheight=0.024)

        self.style.configure('SortLableOne.TLabel',anchor='w', font=('宋体',9))
        self.SortLableOne = Label(self.Data, text='药品分类1:', style='SortLableOne.TLabel')
        self.SortLableOne.place(relx=0.017, rely=0.044, relwidth=0.079, relheight=0.024)

        self.style.configure('Label1.TLabel',anchor='w', font=('宋体',9))
        self.Label1 = Label(self.QuickViewFrame, text='品名', style='Label1.TLabel')
        self.Label1.place(relx=0.358, rely=0.332, relwidth=0.62, relheight=0.088)

        self.style.configure('Label2.TLabel',anchor='w', font=('宋体',9))
        self.Label2 = Label(self.QuickViewFrame, text='品名', style='Label2.TLabel')
        self.Label2.place(relx=0.358, rely=0.497, relwidth=0.62, relheight=0.088)

 

class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self.configs={}
        self.browser=None
        self.ProvinceURLList={}



    # def InitialChromeBtn_Cmd(self, event=None):
    #     #TODO, Please finish the function here!
    #     d = threading.Thread(target=self.InitialChrome)
    #     d.start()
    #     pass

    def InitialChrome(self,event=None):
        if self.browser!=None:
            try:
                self.browser.quit()
                print('Close current page')
                pass
            except Exception as e:
                print("in Close current page")
                print(e)
        try:
            display=True
            login=False
            driverPath=os.path.dirname(os.path.realpath(sys.argv[0]))+"\\chromedriver.exe"
            chrome_options = webdriver.ChromeOptions()
            user_data_dir=self.getConf("最后用户目录地址","","一次性设置")
            if user_data_dir==None or user_data_dir=="" or not os.path.exists(user_data_dir):
                user_data_dir=os.getenv('TEMP')+"\\"+str(time.time()).replace(".","")+"\\"
                self.writeConfig("最后用户目录地址",user_data_dir,"一次性设置")
            chrome_options.add_argument('--user-data-dir='+user_data_dir)
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('--profile-directory=Default')
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument("--disable-plugins-discovery")
            chrome_options.add_argument("--start-maximized")
            if display:
                print("现在显示打开模式")
            else:
                print("显示处于后台模式")
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--enable-javascript')
            chrome_options.add_argument('--log-level=3')
            chrome_options.add_argument('--disable-popup-blocking')
            chrome_options.add_argument('-–single-process')
            chrome_options.add_argument('--ignore-ssl-errors')
            browser_ = webdriver.Chrome(chrome_options=chrome_options,executable_path=driverPath)
            if login:
                print("cookie keep")
            else :
                browser_.delete_all_cookies()
                print("cookie delete")
            browser_.set_page_load_timeout(5000) 
            browser_.get("chrome://version/")
            self.InitialChromeBtn.config(state="NORMAL")
        except Exception as e:
            if 'already in use' in str(e):
                print(str(e))
            print(e)
            self.InitialChromeBtn.config(state="NORMAL")
        self.browser=browser_
       



    def getConf(self,name,initValue,path):
        tmp_=str(initValue)
        try:
            value= config.read_config('config.ini', path, name)
            if value==None or value=="":
                self.writeConfig(name,tmp_,path)
                return initValue
            else:
                return value
        except Exception as e:
            print(e)
            self.writeConfig(name,tmp_,path)
            return initValue

    def writeConfig(self,confName,confValue,path):
        path_=path
        if path==None:
            path_="通用设置"
        config.write_config('config.ini', path_, confName,confValue)
        return confValue


   


def removeBom(file):
    BOM = b'\xef\xbb\xbf'
    existBom = lambda s: True if s==BOM else False

    f = open(file, 'rb')
    if existBom( f.read(3) ):
        fbody = f.read()
        #f.close()
        with open(file, 'wb') as f:
            f.write(fbody)


def is_nan(x):
    for s in x:
        if s==1 or s=="1": continue
        if s==2 or s=="2": continue
        if s==3 or s=="3": continue
        if s==4 or s=="4": continue
        if s==5 or s=="5": continue
        if s==6 or s=="6": continue
        if s==7 or s=="7": continue
        if s==8 or s=="8": continue
        if s==9 or s=="9": continue
        if s==0 or s=="0": continue
        if s=="." : continue
        return True
    return False


 


if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass
