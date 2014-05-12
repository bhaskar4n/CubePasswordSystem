import wx
import hashlib             # cube password system(cps)
import bz2
import os
import base64
import fileinput
from os import walk


class cube(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"cube password system(cps)",size=(700,700))
        self.panel=wx.Panel(self,-1)
        self.SetBackgroundColour("#25163")
        self.retrive=wx.Button(self.panel,230,"Retrieve Data",pos=(270,200),size=(100,70))
        self.encryptData=wx.Button(self.panel,231,"Encrypt Data",pos=(270,300),size=(100,70))
        
        self.Bind(wx.EVT_BUTTON,self.retriv,id=230)
        self.Bind(wx.EVT_BUTTON,self.encrypt,id=231)
        
        
        self.head=wx.StaticText(self.panel,-1,"Cube password system(CPS)",pos=(170,10))
        font = wx.Font(21, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Garamond')
        self.head.SetFont(font)
        self.encrypted_data_path="EncryptedData"
        self.passwords_path="passwords"
        self.filenames="filenames"
        if not os.path.exists(self.encrypted_data_path):
            
            os.makedirs('EncryptedData')
        if not os.path.exists(self.passwords_path):
            
            os.makedirs('Passwords')

        if not os.path.exists(self.filenames):

            os.makedirs("filenames")

    # for decryption        
    def encrypt(self,event):
        


        self.retrive.Destroy()
        self.encryptData.Destroy()
        self.head1=wx.StaticText(self.panel,-1,"Title",pos=(150,100))
        self.title=wx.TextCtrl(self.panel,-1,"",pos=(180,100),size=(150,20))
        self.data=wx.TextCtrl(self.panel,-1,"",style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER|wx.TE_AUTO_URL|wx.TE_LEFT|wx.TE_RICH2,size=(400,400),pos=(150,150))
        #self.data.SetForegroundColour("green")
        #self.data.SetBackgroundColour("black")
       
        #self.data.SetMaxLength(5)
        font1 = wx.Font(11, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.data.SetFont(font1)
        self.btn1=wx.Button(self.panel,201,"Enter",pos=(300,570),size=(70,20))
        self.Bind(wx.EVT_BUTTON,self.Enter,id=201)
        self.y=100


    def Enter(self,event):

        self.name=self.title.GetValue()
        self.data1=(self.data.GetValue())
        if ((len(self.name) and len(self.data1))==0):
           self.dial = wx.MessageDialog(None, 'fill all the fields', 'Info', wx.OK)
           self.dial.ShowModal()
        elif os.path.exists('EncryptedData/'+self.name+'.ef'):
            self.dial = wx.MessageDialog(None, 'same title name exists', 'Info', wx.OK)
            self.dial.ShowModal()
        else:
            
                
            encoded = base64.b64encode(self.data1)
            self.file=open('EncryptedData/'+self.name+'.ef','w')
            
            self.file.write(encoded)
            self.file.close()
            self.finenam = open('filenames/filenames.txt','a')
            self.finenam.write(self.name+'\n')
            self.finenam.close()


            #self.data.Enable(False)
            #self.data.Clear()
            self.head1.Destroy()
            self.data.Destroy()
            self.btn1.Destroy()
            self.title.Destroy()
            #self.please_enter_titlename=wx.StaticText(self.panel,-1,"title name accepted.....",pos=(30,50))
            #self.data_encrypted=wx.StaticText(self.panel,-1,"Data Encrypted.....",pos=(30,75))
            self.please_passwordd=wx.StaticText(self.panel,-1,"Now enter the your cube password....",pos=(30,100))
            #self.data_encrypted.SetBackgroundColour('green')
            self.side1=wx.StaticText(self.panel,-1,"Side 1 ",pos=(300,100))
            #self.data1=wx.TextCtrl(self.panel,-1,"hello",pos=(100,200))
            self.image_file = 'grid3.jpg'
            self.bmp1 = wx.Image(self.image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            # image's upper left corner anchors at panel coordinates (0, 0)
            self.bitmap1 = wx.StaticBitmap(self, -1, self.bmp1, (150,150 ))

        
        
        
            #self.file.write(self.data1)
            #self.file.close()
            self.box1=wx.TextCtrl(self.panel,209,"",pos=(170,170),size=(60,60),style=wx.TE_PASSWORD)
            self.box2=wx.TextCtrl(self.panel,-1,"",pos=(320,170),size=(60,60),style=wx.TE_PASSWORD)
            self.box3=wx.TextCtrl(self.panel,-1,"",pos=(470,170),size=(60,60),style=wx.TE_PASSWORD)

            self.box4=wx.TextCtrl(self.panel,-1,"",pos=(170,320),size=(60,60),style=wx.TE_PASSWORD)
            self.box5=wx.TextCtrl(self.panel,-1,"",pos=(320,320),size=(60,60),style=wx.TE_PASSWORD)
            self.box6=wx.TextCtrl(self.panel,-1,"",pos=(470,320),size=(60,60),style=wx.TE_PASSWORD)

            self.box7=wx.TextCtrl(self.panel,-1,"",pos=(170,470),size=(60,60),style=wx.TE_PASSWORD)
            self.box8=wx.TextCtrl(self.panel,-1,"",pos=(320,470),size=(60,60),style=wx.TE_PASSWORD)
            self.box9=wx.TextCtrl(self.panel,-1,"",pos=(470,470),size=(60,60),style=wx.TE_PASSWORD)
            self.font2 = wx.Font(31, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Garamond')
            self.box1.SetFont(self.font2)
            self.box2.SetFont(self.font2)
            self.box3.SetFont(self.font2)
            self.box4.SetFont(self.font2)
            self.box5.SetFont(self.font2)
            self.box6.SetFont(self.font2)
            self.box7.SetFont(self.font2)
            self.box8.SetFont(self.font2)
            self.box9.SetFont(self.font2)
            self.btn2=wx.Button(self.panel,250,"next",pos=(300,570),size=(70,20))
            self.Bind(wx.EVT_BUTTON,self.side2,id=250)
            #self.paint=self.panel.Bind(wx.EVT_PAINT, self.on_paint0)


    def side2(self,event):
        if len(self.box1.GetValue()) or len(self.box2.GetValue()) or len(self.box3.GetValue()) or len(self.box4.GetValue()) or len(self.box5.GetValue()) or len(self.box6.GetValue()) or len(self.box7.GetValue()) or len(self.box8.GetValue()) or len(self.box9.GetValue())==1:
            
            self.a=str(1)+(self.box1.GetValue())+str(2)+(self.box2.GetValue())+str(3)+(self.box3.GetValue())+str(4)+(self.box4.GetValue())+str(5)+(self.box5.GetValue())+str(6)+(self.box6.GetValue())+str(7)+(self.box7.GetValue())+str(8)+(self.box8.GetValue())+str(9)+(self.box9.GetValue())
            print self.a
            #password_encryption=hashlib.md5(self.a).hexdigest()
            #self.file1=open("Passwords/cps1.DAT","a")
            #self.file1.write(password_encryption+"\n")
            #self.file1.close()


            # destroying the previous side of the cube
            self.side1.Destroy()
            self.box1.Destroy()
            self.box2.Destroy()
            self.box3.Destroy()
            self.box4.Destroy()
            self.box5.Destroy()
            self.box6.Destroy()
            self.box7.Destroy()
            self.box8.Destroy()
            self.box9.Destroy()
            self.btn2.Destroy()

            # creating the side 2 of the cube
            self.side1=wx.StaticText(self.panel,-1,"Side 2 ",pos=(300,100))
            self.box21=wx.TextCtrl(self.panel,209,"",pos=(170,170),size=(60,60),style=wx.TE_PASSWORD)
            self.box22=wx.TextCtrl(self.panel,-1,"",pos=(320,170),size=(60,60),style=wx.TE_PASSWORD)
            self.box23=wx.TextCtrl(self.panel,-1,"",pos=(470,170),size=(60,60),style=wx.TE_PASSWORD)

            self.box24=wx.TextCtrl(self.panel,-1,"",pos=(170,320),size=(60,60),style=wx.TE_PASSWORD)
            self.box25=wx.TextCtrl(self.panel,-1,"",pos=(320,320),size=(60,60),style=wx.TE_PASSWORD)
            self.box26=wx.TextCtrl(self.panel,-1,"",pos=(470,320),size=(60,60),style=wx.TE_PASSWORD)

            self.box27=wx.TextCtrl(self.panel,-1,"",pos=(170,470),size=(60,60),style=wx.TE_PASSWORD)
            self.box28=wx.TextCtrl(self.panel,-1,"",pos=(320,470),size=(60,60),style=wx.TE_PASSWORD)
            self.box29=wx.TextCtrl(self.panel,-1,"",pos=(470,470),size=(60,60),style=wx.TE_PASSWORD)

            # setting font for the side 2 
            self.box21.SetFont(self.font2)
            self.box22.SetFont(self.font2)
            self.box23.SetFont(self.font2)
            self.box24.SetFont(self.font2)
            self.box25.SetFont(self.font2)
            self.box26.SetFont(self.font2)
            self.box27.SetFont(self.font2)
            self.box28.SetFont(self.font2)
            self.box29.SetFont(self.font2)

            #saving creating button

            self.btn3=wx.Button(self.panel,250,"next",pos=(300,570),size=(70,20))
            self.Bind(wx.EVT_BUTTON,self.side3,id=250)

        else:
            #self.enter_password=wx.StaticText(self.panel,-1,"enter password",pos=(30,125))
            #self.enter_password.SetBackgroundColour('red')
            #self.box = wx.Dialog(None,"enter your password")
            self.dial = wx.MessageDialog(None, 'Enter your password', 'Info', wx.OK)
            self.dial.ShowModal()
        


    def side3(self,event):
        if len(self.box21.GetValue()) or len(self.box22.GetValue()) or len(self.box23.GetValue()) or len(self.box24.GetValue()) or len(self.box25.GetValue()) or len(self.box26.GetValue()) or len(self.box27.GetValue()) or len(self.box28.GetValue()) or len(self.box29.GetValue())==1:



            self.b=str(1)+(self.box21.GetValue())+str(2)+(self.box22.GetValue())+str(3)+(self.box23.GetValue())+str(4)+(self.box24.GetValue())+str(5)+(self.box25.GetValue())+str(6)+(self.box26.GetValue())+str(7)+(self.box27.GetValue())+str(8)+(self.box28.GetValue())+str(9)+(self.box29.GetValue())
            print "side 2 password",self.b

        #destroying the side 2 of the cube
            self.side1.Destroy()
            self.box21.Destroy()
            self.box22.Destroy()
            self.box23.Destroy()
            self.box24.Destroy()
            self.box25.Destroy()
            self.box26.Destroy()
            self.box27.Destroy()
            self.box28.Destroy()
            self.box29.Destroy()
            self.btn3.Destroy()

        # creating the side 3 of the cube
            self.side1=wx.StaticText(self.panel,-1,"Side 3 ",pos=(300,100))
            self.box31=wx.TextCtrl(self.panel,209,"",pos=(170,170),size=(60,60),style=wx.TE_PASSWORD)
            self.box32=wx.TextCtrl(self.panel,-1,"",pos=(320,170),size=(60,60),style=wx.TE_PASSWORD)
            self.box33=wx.TextCtrl(self.panel,-1,"",pos=(470,170),size=(60,60),style=wx.TE_PASSWORD)

            self.box34=wx.TextCtrl(self.panel,-1,"",pos=(170,320),size=(60,60),style=wx.TE_PASSWORD)
            self.box35=wx.TextCtrl(self.panel,-1,"",pos=(320,320),size=(60,60),style=wx.TE_PASSWORD)
            self.box36=wx.TextCtrl(self.panel,-1,"",pos=(470,320),size=(60,60),style=wx.TE_PASSWORD)

            self.box37=wx.TextCtrl(self.panel,-1,"",pos=(170,470),size=(60,60),style=wx.TE_PASSWORD)
            self.box38=wx.TextCtrl(self.panel,-1,"",pos=(320,470),size=(60,60),style=wx.TE_PASSWORD)
            self.box39=wx.TextCtrl(self.panel,-1,"",pos=(470,470),size=(60,60),style=wx.TE_PASSWORD)

        # setting font for the side 2 
            self.box31.SetFont(self.font2)
            self.box32.SetFont(self.font2)
            self.box33.SetFont(self.font2)
            self.box34.SetFont(self.font2)
            self.box35.SetFont(self.font2)
            self.box36.SetFont(self.font2)
            self.box37.SetFont(self.font2)
            self.box38.SetFont(self.font2)
            self.box39.SetFont(self.font2)

            #saving creating button

            self.btn4=wx.Button(self.panel,250,"next",pos=(300,570),size=(70,20))
            self.Bind(wx.EVT_BUTTON,self.side4,id=250)

        else:
            self.dial.ShowModal()


    def side4(self,event):
        if len(self.box31.GetValue()) or len(self.box32.GetValue()) or len(self.box33.GetValue()) or len(self.box34.GetValue()) or len(self.box35.GetValue()) or len(self.box36.GetValue()) or len(self.box37.GetValue()) or len(self.box38.GetValue()) or len(self.box39.GetValue())==1:

            self.c=str(1)+(self.box31.GetValue())+str(2)+(self.box32.GetValue())+str(3)+(self.box33.GetValue())+str(4)+(self.box34.GetValue())+str(5)+(self.box35.GetValue())+str(6)+(self.box36.GetValue())+str(7)+(self.box37.GetValue())+str(8)+(self.box38.GetValue())+str(9)+(self.box39.GetValue())
            print "side 3 password",self.c

            # destroying the side 3 of the cube
            self.side1.Destroy()
            self.box31.Destroy()
            self.box32.Destroy()
            self.box33.Destroy()
            self.box34.Destroy()
            self.box35.Destroy()
            self.box36.Destroy()
            self.box37.Destroy()
            self.box38.Destroy()
            self.box39.Destroy()
            self.btn4.Destroy()

            # creating side 4 of the cube
            self.side1=wx.StaticText(self.panel,-1,"Side 4 ",pos=(300,100))
            self.box41=wx.TextCtrl(self.panel,209,"",pos=(170,170),size=(60,60),style=wx.TE_PASSWORD)
            self.box42=wx.TextCtrl(self.panel,-1,"",pos=(320,170),size=(60,60),style=wx.TE_PASSWORD)
            self.box43=wx.TextCtrl(self.panel,-1,"",pos=(470,170),size=(60,60),style=wx.TE_PASSWORD)

            self.box44=wx.TextCtrl(self.panel,-1,"",pos=(170,320),size=(60,60),style=wx.TE_PASSWORD)
            self.box45=wx.TextCtrl(self.panel,-1,"",pos=(320,320),size=(60,60),style=wx.TE_PASSWORD)
            self.box46=wx.TextCtrl(self.panel,-1,"",pos=(470,320),size=(60,60),style=wx.TE_PASSWORD)

            self.box47=wx.TextCtrl(self.panel,-1,"",pos=(170,470),size=(60,60),style=wx.TE_PASSWORD)
            self.box48=wx.TextCtrl(self.panel,-1,"",pos=(320,470),size=(60,60),style=wx.TE_PASSWORD)
            self.box49=wx.TextCtrl(self.panel,-1,"",pos=(470,470),size=(60,60),style=wx.TE_PASSWORD)

            # setting side 4 font

            self.box41.SetFont(self.font2)
            self.box42.SetFont(self.font2)
            self.box43.SetFont(self.font2)
            self.box44.SetFont(self.font2)
            self.box45.SetFont(self.font2)
            self.box46.SetFont(self.font2)
            self.box47.SetFont(self.font2)
            self.box48.SetFont(self.font2)
            self.box49.SetFont(self.font2)

            # creating side 4 button

            self.btn4=wx.Button(self.panel,250,"finish",pos=(300,570),size=(70,20))
            self.Bind(wx.EVT_BUTTON,self.final,id=250)

        else:
            self.dial.ShowModal()


    def final(self,event):
        if len(self.box41.GetValue()) or len(self.box42.GetValue()) or len(self.box43.GetValue()) or len(self.box44.GetValue()) or len(self.box45.GetValue()) or len(self.box46.GetValue()) or len(self.box47.GetValue()) or len(self.box48.GetValue()) or len(self.box49.GetValue())==1:
            self.f=str(1)+(self.box41.GetValue())+str(2)+(self.box42.GetValue())+str(3)+(self.box43.GetValue())+str(4)+(self.box44.GetValue())+str(5)+(self.box45.GetValue())+str(6)+(self.box46.GetValue())+str(7)+(self.box47.GetValue())+str(8)+(self.box48.GetValue())+str(9)+(self.box49.GetValue())
            
            print "side final password",self.f

            print "cube password", self.a+self.b+self.c+self.f

            # saving password file

            password_encryption=hashlib.md5(self.a+self.b+self.c+self.f).hexdigest()
            password_encryption_filename=hashlib.md5(self.name).hexdigest()
            password_append = password_encryption+password_encryption_filename
            print password_append
            self.file1=open("Passwords/cps1.DAT","a")
            self.file1.write(password_append+"\n")
            self.file1.close()


            # destroying the final side
            self.side1.Destroy()
            self.box41.Destroy()
            self.box42.Destroy()
            self.box43.Destroy()
            self.box44.Destroy()
            self.box45.Destroy()
            self.box46.Destroy()
            self.box47.Destroy()
            self.box48.Destroy()
            self.box49.Destroy()
           # self.image_file.Destroy()
            self.bmp1.Destroy()
            self.bitmap1.Destroy()
            self.btn4.Destroy()
            self.please_passwordd.Destroy()

            # final data
            self.text1 = wx.StaticText(self,-1,"your password and data encrypted successfully.....",pos=(70,150))
            self.font3 = wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Garamond')
            self.text1.SetFont(self.font3)


        else:

            self.dial.ShowModal()





  
        #insert=self.box2.GetInsertionPoint()
        #print insert



    def retriv(self,event):

        
        self.finenam = open('filenames/filenames.txt','r')
        f=self.finenam.readlines()
        self.finenam.close()


        self.box = wx.SingleChoiceDialog(None,"choose your filename to decrypt","filenames",f)
        if self.box.ShowModal()==wx.ID_OK:
            self.apples=self.box.GetStringSelection()
            

        self.retrive.Destroy()
        self.encryptData.Destroy()
        self.file_retrive=wx.StaticText(self.panel,-1,"enter file name to be retrive....",pos=(30,70))
        self.cube_password=wx.StaticText(self.panel,-1,"enter your password....",pos=(30,90))
        image_file = 'grid3.jpg'
        bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        # image's upper left corner anchors at panel coordinates (0, 0)
        self.bitmap1 = wx.StaticBitmap(self, -1, bmp1, (150,150 ))
        
        self.filename=wx.StaticText(self.panel,-1,"type fileName again:",pos=(150,120))
        self.filename=wx.StaticText(self.panel,-1,self.apples,pos=(300,85))
        self.finename1=wx.TextCtrl(self.panel,-1,"",pos=(270,120),size=(150,20))
        self.p1=wx.StaticText(self.panel,-1,"Side 1 ",pos=(400,100))
        self.box1=wx.TextCtrl(self.panel,-1,"",pos=(170,170),size=(60,60),style=wx.TE_PASSWORD)
        self.box2=wx.TextCtrl(self.panel,-1,"",pos=(320,170),size=(60,60),style=wx.TE_PASSWORD)
        self.box3=wx.TextCtrl(self.panel,-1,"",pos=(470,170),size=(60,60),style=wx.TE_PASSWORD)

        self.box4=wx.TextCtrl(self.panel,-1,"",pos=(170,320),size=(60,60),style=wx.TE_PASSWORD)
        self.box5=wx.TextCtrl(self.panel,-1,"",pos=(320,320),size=(60,60),style=wx.TE_PASSWORD)
        self.box6=wx.TextCtrl(self.panel,-1,"",pos=(470,320),size=(60,60),style=wx.TE_PASSWORD)

        self.box7=wx.TextCtrl(self.panel,-1,"",pos=(170,470),size=(60,60),style=wx.TE_PASSWORD)
        self.box8=wx.TextCtrl(self.panel,-1,"",pos=(320,470),size=(60,60),style=wx.TE_PASSWORD)
        self.box9=wx.TextCtrl(self.panel,-1,"",pos=(470,470),size=(60,60),style=wx.TE_PASSWORD)
        self.font2 = wx.Font(31, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.box1.SetFont(self.font2)
        self.box2.SetFont(self.font2)
        self.box3.SetFont(self.font2)
        self.box4.SetFont(self.font2)
        self.box5.SetFont(self.font2)
        self.box6.SetFont(self.font2)
        self.box7.SetFont(self.font2)
        self.box8.SetFont(self.font2)
        self.box9.SetFont(self.font2)
        self.btn6=wx.Button(self.panel,250,"next",pos=(300,570),size=(100,20))
        self.Bind(wx.EVT_BUTTON,self.side2_decrypt,id=250)

    def side2_decrypt(self,event):

        self.decodefile=self.finename1.GetValue()
        print str(self.decodefile)
        #print self.decodefile
        self.x =str(1)+(self.box1.GetValue())+str(2)+(self.box2.GetValue())+str(3)+(self.box3.GetValue())+str(4)+(self.box4.GetValue())+str(5)+(self.box5.GetValue())+str(6)+(self.box6.GetValue())+str(7)+(self.box7.GetValue())+str(8)+(self.box8.GetValue())+str(9)+(self.box9.GetValue())
        #print self.x
        #self.password_encryption1=hashlib.md5(self.b).hexdigest()
        #print self.password_encryption1
        #if self.password_encryption1 in open("/Passwords/cps1.DAT").read():
            
         #   self.fo=open('/EncryptedData/'+self.decodefile+'.ef','r')
          #  d=self.fo.read()
           # print self.fo.read()
            #self.datadecode=base64.b64decode(d)
            # destroying side 1 of the cube
        self.p1.Destroy()
        self.box1.Destroy()
        self.box2.Destroy()
        self.box3.Destroy()
        self.box4.Destroy()
        self.box5.Destroy()
        self.box6.Destroy()
        self.box7.Destroy()
        self.box8.Destroy()
        self.box9.Destroy()
        self.btn6.Destroy()

            # creating side 2 of the cube 
        self.p2=wx.StaticText(self.panel,-1,"side 2 ",pos=(300,100))
        self.box21=wx.TextCtrl(self.panel,-1,"",pos=(170,170),size=(60,60),style=wx.TE_PASSWORD)
        self.box22=wx.TextCtrl(self.panel,-1,"",pos=(320,170),size=(60,60),style=wx.TE_PASSWORD)
        self.box23=wx.TextCtrl(self.panel,-1,"",pos=(470,170),size=(60,60),style=wx.TE_PASSWORD)

        self.box24=wx.TextCtrl(self.panel,-1,"",pos=(170,320),size=(60,60),style=wx.TE_PASSWORD)
        self.box25=wx.TextCtrl(self.panel,-1,"",pos=(320,320),size=(60,60),style=wx.TE_PASSWORD)
        self.box26=wx.TextCtrl(self.panel,-1,"",pos=(470,320),size=(60,60),style=wx.TE_PASSWORD)

        self.box27=wx.TextCtrl(self.panel,-1,"",pos=(170,470),size=(60,60),style=wx.TE_PASSWORD)
        self.box28=wx.TextCtrl(self.panel,-1,"",pos=(320,470),size=(60,60),style=wx.TE_PASSWORD)
        self.box29=wx.TextCtrl(self.panel,-1,"",pos=(470,470),size=(60,60),style=wx.TE_PASSWORD)
        self.box21.SetFont(self.font2)
        self.box22.SetFont(self.font2)
        self.box23.SetFont(self.font2)
        self.box24.SetFont(self.font2)
        self.box25.SetFont(self.font2)
        self.box26.SetFont(self.font2)
        self.box27.SetFont(self.font2)
        self.box28.SetFont(self.font2)
        self.box29.SetFont(self.font2)

        self.btn7=wx.Button(self.panel,250,"next",pos=(300,570),size=(100,20))
        self.Bind(wx.EVT_BUTTON,self.side3_decrypt,id=250)

    def side3_decrypt(self,event):


        self.y=str(1)+(self.box21.GetValue())+str(2)+(self.box22.GetValue())+str(3)+(self.box23.GetValue())+str(4)+(self.box24.GetValue())+str(5)+(self.box25.GetValue())+str(6)+(self.box26.GetValue())+str(7)+(self.box27.GetValue())+str(8)+(self.box28.GetValue())+str(9)+(self.box29.GetValue())
        #print self.y
        # destroying side 2 of the cube
        
        self.p2.Destroy()
        self.box21.Destroy()
        self.box22.Destroy()
        self.box23.Destroy()
        self.box24.Destroy()
        self.box25.Destroy()
        self.box26.Destroy()
        self.box27.Destroy()
        self.box28.Destroy()
        self.box29.Destroy()
        self.btn7.Destroy()

        # creating the side 3 of the cube:
        self.p3=wx.StaticText(self.panel,-1,"Side 3 ",pos=(300,100))
        self.box31=wx.TextCtrl(self.panel,-1,"",pos=(170,170),size=(60,60),style=wx.TE_PASSWORD)
        self.box32=wx.TextCtrl(self.panel,-1,"",pos=(320,170),size=(60,60),style=wx.TE_PASSWORD)
        self.box33=wx.TextCtrl(self.panel,-1,"",pos=(470,170),size=(60,60),style=wx.TE_PASSWORD)

        self.box34=wx.TextCtrl(self.panel,-1,"",pos=(170,320),size=(60,60),style=wx.TE_PASSWORD)
        self.box35=wx.TextCtrl(self.panel,-1,"",pos=(320,320),size=(60,60),style=wx.TE_PASSWORD)
        self.box36=wx.TextCtrl(self.panel,-1,"",pos=(470,320),size=(60,60),style=wx.TE_PASSWORD)

        self.box37=wx.TextCtrl(self.panel,-1,"",pos=(170,470),size=(60,60),style=wx.TE_PASSWORD)
        self.box38=wx.TextCtrl(self.panel,-1,"",pos=(320,470),size=(60,60),style=wx.TE_PASSWORD)
        self.box39=wx.TextCtrl(self.panel,-1,"",pos=(470,470),size=(60,60),style=wx.TE_PASSWORD)

        # adding font for the side 3 of the cube

        self.box31.SetFont(self.font2)
        self.box32.SetFont(self.font2)
        self.box33.SetFont(self.font2)
        self.box34.SetFont(self.font2)
        self.box35.SetFont(self.font2)
        self.box36.SetFont(self.font2)
        self.box37.SetFont(self.font2)
        self.box38.SetFont(self.font2)
        self.box39.SetFont(self.font2)
        
        self.btn8=wx.Button(self.panel,250,"next",pos=(300,570),size=(100,20))
        self.Bind(wx.EVT_BUTTON,self.side4_decrypt,id=250)

    def side4_decrypt(self,event):

        self.z=str(1)+(self.box31.GetValue())+str(2)+(self.box32.GetValue())+str(3)+(self.box33.GetValue())+str(4)+(self.box34.GetValue())+str(5)+(self.box35.GetValue())+str(6)+(self.box36.GetValue())+str(7)+(self.box37.GetValue())+str(8)+(self.box38.GetValue())+str(9)+(self.box39.GetValue())
        #print self.z
        # destroying the side 3 of the cube
        
        self.p3.Destroy()
        self.box31.Destroy()
        self.box32.Destroy()
        self.box33.Destroy()
        self.box34.Destroy()
        self.box35.Destroy()
        self.box36.Destroy()
        self.box37.Destroy()
        self.box38.Destroy()
        self.box39.Destroy()
        self.btn8.Destroy()

        # creating the side 4 of the cube
        self.p4=wx.StaticText(self.panel,-1,"Side 4 ",pos=(300,100))
        self.box41=wx.TextCtrl(self.panel,-1,"",pos=(170,170),size=(60,60),style=wx.TE_PASSWORD)
        self.box42=wx.TextCtrl(self.panel,-1,"",pos=(320,170),size=(60,60),style=wx.TE_PASSWORD)
        self.box43=wx.TextCtrl(self.panel,-1,"",pos=(470,170),size=(60,60),style=wx.TE_PASSWORD)

        self.box44=wx.TextCtrl(self.panel,-1,"",pos=(170,320),size=(60,60),style=wx.TE_PASSWORD)
        self.box45=wx.TextCtrl(self.panel,-1,"",pos=(320,320),size=(60,60),style=wx.TE_PASSWORD)
        self.box46=wx.TextCtrl(self.panel,-1,"",pos=(470,320),size=(60,60),style=wx.TE_PASSWORD)

        self.box47=wx.TextCtrl(self.panel,-1,"",pos=(170,470),size=(60,60),style=wx.TE_PASSWORD)
        self.box48=wx.TextCtrl(self.panel,-1,"",pos=(320,470),size=(60,60),style=wx.TE_PASSWORD)
        self.box49=wx.TextCtrl(self.panel,-1,"",pos=(470,470),size=(60,60),style=wx.TE_PASSWORD)

        # setting font for side 4 of the cube

        self.box41.SetFont(self.font2)
        self.box42.SetFont(self.font2)
        self.box43.SetFont(self.font2)
        self.box44.SetFont(self.font2)
        self.box45.SetFont(self.font2)
        self.box46.SetFont(self.font2)
        self.box47.SetFont(self.font2)
        self.box48.SetFont(self.font2)
        self.box49.SetFont(self.font2)

        # setting button for side 4

        self.btn9=wx.Button(self.panel,250,"finish",pos=(300,570),size=(100,20))
        self.Bind(wx.EVT_BUTTON,self.final_decrypt,id=250)

    def final_decrypt(self,event):


        self.z1=str(1)+(self.box41.GetValue())+str(2)+(self.box42.GetValue())+str(3)+(self.box43.GetValue())+str(4)+(self.box44.GetValue())+str(5)+(self.box45.GetValue())+str(6)+(self.box46.GetValue())+str(7)+(self.box47.GetValue())+str(8)+(self.box48.GetValue())+str(9)+(self.box49.GetValue())
        #print self.z1
        self.finpas = (str(self.x+self.y+self.z+self.z1))
        print self.finpas
        self.passs=hashlib.md5((self.finpas)).hexdigest()
        self.passs1=hashlib.md5(self.decodefile).hexdigest()
        print self.passs
        self.password_encryption1 = self.passs+self.passs1
        print self.password_encryption1

        print self.password_encryption1
        if self.password_encryption1 in open("Passwords/cps1.DAT").read():

            print self.decodefile
            self.fo=open('EncryptedData/'+self.decodefile+'.ef','r')
            d=self.fo.read()
            print self.fo.read()
            self.datadecode=base64.b64decode(d)
            
            #self.retrive_data.Destroy()
            self.cube_password.Destroy()
            self.file_retrive.Destroy()
            
            self.box41.Destroy()
            self.box42.Destroy()
            self.box43.Destroy()
            self.box44.Destroy()
            self.box45.Destroy()
            self.box46.Destroy()
            self.box47.Destroy()
            self.box48.Destroy()
            self.box49.Destroy()
            self.btn9.Destroy()
            self.p4.Destroy()
            
            self.x=0
            self.y=0
            self.z=0
            self.z1=0

            self.password_encryption1=0

            self.retrive_data=wx.TextCtrl(self.panel,-1,str(self.datadecode),style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER,size=(400,400),pos=(150,150))


            print self.datadecode
            

            self.fo.close()
        else:

            print "wrong password"
            self.wrong_password=wx.StaticText(self.panel,-1,"Access Denied.....",pos=(30,125))
            self.wrong_password.SetBackgroundColour('red')
            

  



            
    def on_paint0(self, event):
        # establish the painting surface
        dc = wx.PaintDC(self.panel)
        dc.SetPen(wx.Pen('black', 1))
        # draw a red rounded-rectangle
        dc.SetBrush(wx.Brush('#F5DEB3'))
        rect = wx.Rect(150,150, 400, 400) 
        dc.DrawRoundedRectangleRect(rect, 8)

    def length(self,event):

        print "hello"            
        
app=wx.App()
frame=cube()
frame.Centre()
frame.Show()
app.MainLoop()
