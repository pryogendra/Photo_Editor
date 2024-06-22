import shutil
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.widget import MDWidget
import cv2 as cv
import numpy as np
import os
import pyautogui  #used for revolution of the system

size = pyautogui.size()
Window.size=(size[0]-50,size[1]-50)

global active
active = 'A1'

class Chooser_Root(Widget):
    Builder.load_file("file_chooser.kv")

    def selected(self, filename):
        try:
            f = open("demo.txt", "w")
            f.write(filename[0])
            f.close()
            self.ids.box_layout.remove_widget(self.ids.img)
            Root.Slided([0,1])
        except Exception as e:
            pass


class Root(MDWidget):
    Builder.load_file("Photo_Editor.kv")
    dialog = None

    def Slided(self, *args):
        global x
        global active
        x = args[1]

        try:
            f = open("demo.txt", "r")
            content=f.read()
            self.ids.real_img.source=str(content)
        except:
            pass

        if active == 'A1':
            self.Blur_Image()
        elif active == 'A2':
            self.Blur_Image()
        elif active == 'A3':
            self.Zero_Threshold()
        elif active == 'A4':
            self.Binary_Threshold()
        elif active == 'A5':
            self.Canny_Edge()
        elif active == 'A6':
            self.Grediant()
        #elif active == 'A7':
        #    self.Blur_Image()
        elif active == 'A8':
            self.Splitting()
        elif active == 'A9':
            self.Gray()

    def Blur_Image(self):
        global x
        path = self.ids.real_img.source
        img = cv.imread(path)
        d = 2 * x + 1
        kernel = np.ones((d, d), 'float32') / (d ** 2)  # creating a blank page
        img1 = cv.filter2D(img, -1, kernel)
        temp_image = f'Temp_Img/temp{active}{x}.png'
        cv.imwrite(temp_image, img1)  # saving image
        self.ids.temp_img.source = temp_image

    def Zero_Threshold(self):
        global x
        path = self.ids.real_img.source
        img = cv.imread(path)
        ret, img1 = cv.threshold(img, x, 255, cv.THRESH_TOZERO)
        temp_image = f'Temp_Img/temp{active}{x}.png'
        cv.imwrite(temp_image, img1)  # saving image
        self.ids.temp_img.source = temp_image

    def Binary_Threshold(self):
        global x
        path = self.ids.real_img.source
        img = cv.imread(path)
        ret, img1 = cv.threshold(img, x, 255, cv.THRESH_BINARY)
        temp_image = f'Temp_Img/temp{active}{x}.png'
        cv.imwrite(temp_image, img1)  # saving image
        self.ids.temp_img.source = temp_image

    def Canny_Edge(self):
        global x
        path = self.ids.real_img.source
        img = cv.imread(path)
        img1 = cv.Canny(img, x, x)
        temp_image = f'Temp_Img/temp{active}{x}.png'
        cv.imwrite(temp_image, img1)  # saving image
        self.ids.temp_img.source = temp_image

    def Grediant(self):
        global x
        path = self.ids.real_img.source
        img = cv.imread(path)
        img1 = cv.Laplacian(img.copy(), 8)
        temp_image = f'Temp_Img/temp{active}{x}.png'
        cv.imwrite(temp_image, img1)  # saving image
        self.ids.temp_img.source = temp_image
        self.ids.slider.disabled = True

    def Splitting(self):
        global x
        path = self.ids.real_img.source
        img = cv.imread(path)
        b, g, r = cv.split(img)
        img1 = np.vstack([r, g, b])
        temp_image = f'Temp_Img/temp{active}{x}.png'
        cv.imwrite(temp_image, img1)  # saving image
        self.ids.temp_img.source = temp_image
        self.ids.slider.disabled = True

    def Gray(self):
        global x
        path = self.ids.real_img.source
        img = cv.imread(path)
        img1 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        temp_image = f'Temp_Img/temp{active}{x}.png'
        cv.imwrite(temp_image, img1)  # saving image
        self.ids.temp_img.source = temp_image
        self.ids.slider.disabled = True

    def A1(self):
        global active
        active = 'A1'
        self.ids.A1.size_hint = .1, 1
        self.ids.A2.size_hint = .1, .5
        self.ids.A3.size_hint = .1, .5
        self.ids.A4.size_hint = .1, .5
        self.ids.A5.size_hint = .1, .5
        self.ids.A6.size_hint = .1, .5
        #self.ids.A7.size_hint = .1, .5
        self.ids.A8.size_hint = .1, .5
        self.ids.A9.size_hint = .1, .5
        self.ids.slider.disabled = False
        if os.path.exists("Temp_Img"):
            shutil.rmtree("Temp_Img")
            os.mkdir("Temp_Img")
        else:
            os.mkdir("Temp_Img")

    def A2(self):
        global active
        active = 'A2'
        #self.ids.A1.size_hint = .1, .5
        self.ids.A2.size_hint = .1, 1
        self.ids.A3.size_hint = .1, .5
        self.ids.A4.size_hint = .1, .5
        self.ids.A5.size_hint = .1, .5
        self.ids.A6.size_hint = .1, .5
        #self.ids.A7.size_hint = .1, .5
        self.ids.A8.size_hint = .1, .5
        self.ids.A9.size_hint = .1, .5
        self.ids.slider.disabled = False
        if os.path.exists("Temp_Img"):
            shutil.rmtree("Temp_Img")
            os.mkdir("Temp_Img")
        else:
            os.mkdir("Temp_Img")

    def A3(self):
        global active
        active = 'A3'
        #self.ids.A1.size_hint = .1, .5
        self.ids.A2.size_hint = .1, .5
        self.ids.A3.size_hint = .1, 1
        self.ids.A4.size_hint = .1, .5
        self.ids.A5.size_hint = .1, .5
        self.ids.A6.size_hint = .1, .5
        #self.ids.A7.size_hint = .1, .5
        self.ids.A8.size_hint = .1, .5
        self.ids.A9.size_hint = .1, .5
        self.ids.slider.disabled = False
        if os.path.exists("Temp_Img"):
            shutil.rmtree("Temp_Img")
            os.mkdir("Temp_Img")
        else:
            os.mkdir("Temp_Img")

    def A4(self):
        global active
        active = 'A4'
        #self.ids.A1.size_hint = .1, .5
        self.ids.A2.size_hint = .1, .5
        self.ids.A3.size_hint = .1, .5
        self.ids.A4.size_hint = .1, 1
        self.ids.A5.size_hint = .1, .5
        self.ids.A6.size_hint = .1, .5
        #self.ids.A7.size_hint = .1, .5
        self.ids.A8.size_hint = .1, .5
        self.ids.A9.size_hint = .1, .5
        self.ids.slider.disabled = False
        if os.path.exists("Temp_Img"):
            shutil.rmtree("Temp_Img")
            os.mkdir("Temp_Img")
        else:
            os.mkdir("Temp_Img")

    def A5(self):
        global active
        active = 'A5'
        #self.ids.A1.size_hint = .1, .5
        self.ids.A2.size_hint = .1, .5
        self.ids.A3.size_hint = .1, .5
        self.ids.A4.size_hint = .1, .5
        self.ids.A5.size_hint = .1, 1
        self.ids.A6.size_hint = .1, .5
        #self.ids.A7.size_hint = .1, .5
        self.ids.A8.size_hint = .1, .5
        self.ids.A9.size_hint = .1, .5
        self.ids.slider.disabled = False
        if os.path.exists("Temp_Img"):
            shutil.rmtree("Temp_Img")
            os.mkdir("Temp_Img")
        else:
            os.mkdir("Temp_Img")

    def A6(self):
        global active
        active = 'A6'
        #self.ids.A1.size_hint = .1, .5
        self.ids.A2.size_hint = .1, .5
        self.ids.A3.size_hint = .1, .5
        self.ids.A4.size_hint = .1, .5
        self.ids.A5.size_hint = .1, .5
        self.ids.A6.size_hint = .1, 1
        #self.ids.A7.size_hint = .1, .5
        self.ids.A8.size_hint = .1, .5
        self.ids.A9.size_hint = .1, .5
        self.ids.slider.disabled = False
        if os.path.exists("Temp_Img"):
            shutil.rmtree("Temp_Img")
            os.mkdir("Temp_Img")
        else:
            os.mkdir("Temp_Img")

    def A7(self):
        global active
        active = 'A7'
        self.ids.A1.size_hint = .1, .5
        self.ids.A2.size_hint = .1, .5
        self.ids.A3.size_hint = .1, .5
        self.ids.A4.size_hint = .1, .5
        self.ids.A5.size_hint = .1, .5
        self.ids.A6.size_hint = .1, .5
        self.ids.A7.size_hint = .1, 1
        self.ids.A8.size_hint = .1, .5
        self.ids.A9.size_hint = .1, .5
        self.ids.slider.disabled = False
        if os.path.exists("Temp_Img"):
            shutil.rmtree("Temp_Img")
            os.mkdir("Temp_Img")
        else:
            os.mkdir("Temp_Img")

    def A8(self):
        global active
        active = 'A8'
        #self.ids.A1.size_hint = .1, .5
        self.ids.A2.size_hint = .1, .5
        self.ids.A3.size_hint = .1, .5
        self.ids.A4.size_hint = .1, .5
        self.ids.A5.size_hint = .1, .5
        self.ids.A6.size_hint = .1, .5
        #self.ids.A7.size_hint = .1, .5
        self.ids.A8.size_hint = .1, 1
        self.ids.A9.size_hint = .1, .5
        self.ids.slider.disabled = False
        if os.path.exists("Temp_Img"):
            shutil.rmtree("Temp_Img")
            os.mkdir("Temp_Img")
        else:
            os.mkdir("Temp_Img")

    def A9(self):
        global active
        active = 'A9'
        #self.ids.A1.size_hint = .1, .5
        self.ids.A2.size_hint = .1, .5
        self.ids.A3.size_hint = .1, .5
        self.ids.A4.size_hint = .1, .5
        self.ids.A5.size_hint = .1, .5
        self.ids.A6.size_hint = .1, .5
        #self.ids.A7.size_hint = .1, .5
        self.ids.A8.size_hint = .1, .5
        self.ids.A9.size_hint = .1, 1
        self.ids.slider.disabled = False
        if os.path.exists("Temp_Img"):
            shutil.rmtree("Temp_Img")
            os.mkdir("Temp_Img")
        else:
            os.mkdir("Temp_Img")

    def Save_Image(self, obj):
        try:
            img = self.ids.temp_img.source
            img1 = cv.imread(img)
            newImage = img1.copy()
            img = img.replace('Temp_Img/', '')
            cv.imwrite(img, newImage)
            self.dialog.dismiss()
        except:
            pass

    def show_dialog(self):
        img = self.ids.temp_img.source
        img = img.replace('Temp_Img/', '')
        if not self.dialog:
            self.dialog = MDDialog(
                title='Image saved as',
                text=img,
                buttons=[
                    TextInput(multiline=False, size_hint=(.5, .5)),
                    MDFlatButton(text='Cancel', text_color=self.theme_cls.primary_color, on_release=self.close_dialog),
                    MDRectangleFlatButton(text='OK', text_color=self.theme_cls.primary_color,
                                          on_release=self.Save_Image)
                ]
            )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()  #close the box


class MainApp(MDApp):
    title = 'Photo Editor'

    def build(self):
        #self.theme_cls.primary_palette = 'Blue'
        self.screen = Screen()
        self.theme_cls.theme_style = 'Dark'
        self.screen.add_widget(Root())
        return self.screen

    def File_Chooser(self):
        self.screen.add_widget(Chooser_Root())


if __name__ == '__main__':
    MainApp().run()
