# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from tkinter import *
import tkinter.messagebox as tkmb
import tkinter.filedialog as fd
import gui_landing
import sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/barakakautsar/Desktop/Kripto_1/assets/frame1")

sys.path.append("/Users/barakakautsar/Desktop/Kripto_1")
import vigenereExtended

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class vigenereExtended(Frame):
    def __init__(self, master): 
        Frame.__init__(self, master, width = 526, height = 687)

        #functions
        def encrypt_pressed(plaintext,key):
            plaintext = plaintext.replace(" ", "")
            if (plaintext.isalpha() == False):
                tkmb.showinfo("Invalid Input!",  "Please only input letters for the plaintext.")
            elif (key.isalpha() == False):
                tkmb.showinfo("Invalid Input!",  "Please only input letters for the key.")
            else:
                self.hasilCipher["text"]= vigenereExtended.encrypt(plaintext,key)

        def upload_pressed(type):
            filetypes = [('text files', '*.txt')]
            f = fd.askopenfile(filetypes=filetypes)
            plaintext = ""
            for line in f.readlines():
                plaintext += line.strip() + ""
            if (type =="encrypt"):
                self.entry_1.insert('1.0', plaintext)
            if (type == "decrypt"):
                self.entry_4.insert('1.0', plaintext)  

        def decrypt_pressed(cipher,key):
            cipher = cipher.replace(" ", "")
            if (cipher.isalpha() == False):
                tkmb.showinfo("Invalid Input!",  "Please only input letters for the cipher.")
            elif (key.isalpha() == False):
                tkmb.showinfo("Invalid Input!",  "Please only input letters for the key.")
            else:
                self.hasilPlaintext["text"]= vigenereExtended.decrypt(cipher,key)             

        def save_pressed(type):
            filename = ""
            if filename == "":
                filename = fd.asksaveasfilename(defaultextension=".txt")
            if filename != "":
                if (type == "encryption") and (self.hasilCipher.cget("text")!=""):
                    with open(filename, "w") as file:
                        file.write("".join(self.hasilCipher.cget("text")))
                        tkmb.showinfo("File Saved!",  "File Saved!")
                if (type == "decryption") and self.hasilPlaintext.cget("text")!="":
                    with open(filename, "w") as file:
                        file.write("".join(self.hasilPlaintext.cget("text")))
                        tkmb.showinfo("File Saved!",  "File Saved!")

        def groupbyFive (string): #group of 5 characters
            string = string.upper()
            string = string.replace(" ","")
            string = ' '.join(string[i:i+5] for i in range(0, len(string), 5))
            return(string)

        def group_pressed(type):
            if (type == "encryption") and (self.hasilCipher.cget("text")!=""):
                self.hasilCipher["text"]= groupbyFive(self.hasilCipher.cget("text"))
            if (type == "decryption") and self.hasilPlaintext.cget("text")!="":
                self.hasilPlaintext["text"]= groupbyFive(self.hasilPlaintext.cget("text"))


        #tkinter elements
        self.canvas = Canvas(
            bg = "#FFFFFF",
            height = 687,
            width = 526,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_text(
            263,
            27.08807373046875,
            anchor="n",
            text="Vigenere Cipher Extended",
            fill="#000000",
            font=("HKGrotesk BoldLegacy", 20 * -1)
        )

        self.canvas.create_text(
            103.74162292480469,
            77.80621337890625,
            anchor="nw",
            text="Encrypt",
            fill="#000000",
            font=("HKGrotesk BoldLegacy", 23 * -1)
        )

        self.canvas.create_text(
            103.74162292480469,
            116.99749755859375,
            anchor="nw",
            text="Plaintext",
            fill="#000000",
            font=("HKGrotesk Regular", 11 * -1)
        )

        self.canvas.create_text(
            103.74162292480469,
            180.3951416015625,
            anchor="nw",
            text="Key",
            fill="#000000",
            font=("HKGrotesk Regular", 11 * -1)
        )

        self.canvas.create_text(
            103.74162292480469,
            296.8162841796875,
            anchor="nw",
            text="Cipher",
            fill="#000000",
            font=("HKGrotesk Regular", 11 * -1)
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            78.85569763183594,
            91.04278564453125,
            image=self.image_image_1
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: encrypt_pressed(self.entry_1.get("1.0",END).strip(),self.entry_2.get("1.0",END).strip()),
            relief="flat"
        )
        self.button_1.place(
            x=205.75416564941406,
            y=254.7433319091797,
            width=118.72650146484375,
            height=37.462249755859375
        )
        

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            264.82928466796875,
            152.1543731689453,
            image=self.entry_image_1
        )
        self.entry_1 = Text(
            font=("HKGrotesk Regular", 11 * -1),
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=103.7416124343872,
            y=140,
            width=300,
            height=30
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            264.82928466796875,
            215.55203247070312,
            image=self.entry_image_2
        )
        self.entry_2 = Text(
            font=("HKGrotesk Regular", 11 * -1),
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=103.7416124343872,
            y=200,
            width=300,
            height=30
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            264.82928466796875,
            331.3967876434326,
            image=self.entry_image_3
        )
        self.hasilCipher = Label(
            text = "",
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.hasilCipher.place(
            x=103.7416124343872,
            y=314.682861328125,
            width=322.1753444671631,
            height=31.427852630615234
        )

        self.button_image = PhotoImage(
            file=relative_to_assets("Union.png"))
        self.button_bagi = Button(
            image=self.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: group_pressed("encryption"),
            relief="flat"
        )
        self.button_bagi.place(
            x=380,
            y=322.9999694824219,
            width=14.877685546875,
            height=14.87823486328125
        )       

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: upload_pressed("encrypt"),
            relief="flat"
        )
        self.button_2.place(
            x=409.77687072753906,
            y=145.0,
            width=14.877685546875,
            height=14.87823486328125
        )

        self.canvas.create_text(
            103.74162292480469,
            376.3515319824219,
            anchor="nw",
            text="Decrypt",
            fill="#000000",
            font=("HKGrotesk BoldLegacy", 23 * -1)
        )

        self.canvas.create_text(
            103.74162292480469,
            415.5428161621094,
            anchor="nw",
            text="Cipher",
            fill="#000000",
            font=("HKGrotesk Regular", 11 * -1)
        )

        self.canvas.create_text(
            103.74162292480469,
            478.9404296875,
            anchor="nw",
            text="Key",
            fill="#000000",
            font=("HKGrotesk Regular", 11 * -1)
        )

        self.canvas.create_text(
            103.74162292480469,
            595.3616333007812,
            anchor="nw",
            text="Plaintext",
            fill="#000000",
            font=("HKGrotesk Regular", 11 * -1)
        )
        
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_decrypt = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:decrypt_pressed(self.entry_4.get("1.0",END).strip(),self.entry_5.get("1.0",END).strip()),
            relief="flat"
        )
        self.button_decrypt.place(
            x=205.75416564941406,
            y=553.2886352539062,
            width=118.72650146484375,
            height=37.462249755859375
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            264.82928466796875,
            450.6996765136719,
            image=self.entry_image_4
        )
        self.entry_4 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=103.7416124343872,
            y=433.9857482910156,
            width=322.1753444671631,
            height=31.4278564453125
        )

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            264.82928466796875,
            514.0972900390625,
            image=self.entry_image_5
        )
        self.entry_5 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place(
            x=103.7416124343872,
            y=497.38336181640625,
            width=322.1753444671631,
            height=31.4278564453125
        )

        self.entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            264.82928466796875,
            629.942138671875,
            image=self.entry_image_6
        )
        self.hasilPlaintext = Label(
            text="",
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.hasilPlaintext.place(
            x=103.7416124343872,
            y=613.2282104492188,
            width=322.1753444671631,
            height=31.4278564453125
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: save_pressed("decryption"),
            relief="flat"
        )
        self.button_4.place(
            x=409.94410705566406,
            y=622.0380859375,
            width=15.23187255859375,
            height=15.231903076171875
        )    

        self.button_bagi1 = Button(
            image=self.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: group_pressed("decryption"),
            relief="flat"
        )
        self.button_bagi1.place(
            x=380,
            y=622.0380859375,
            width=14.877685546875,
            height=14.87823486328125
        )     

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: save_pressed("encryption"),
            relief="flat"
        )
        self.button_5.place(
            x=409.77674865722656,
            y=322.9999694824219,
            width=15.23187255859375,
            height=15.231905937194824
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: upload_pressed("decrypt"),
            relief="flat"
        )
        self.button_6.place(
            x=410.77687072753906,
            y=444.0,
            width=14.877685546875,
            height=14.87823486328125
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            78.36326599121094,
            390.8590393066406,
            image=self.image_image_2
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.button_7 = Button(
            master,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.master.switch_frame(gui_landing.Landing),
            relief="flat"
        )
        self.button_7.place(
            x=8.776870727539062,
            y=16.0,
            width=91.90768432617188,
            height=29.0
        )

