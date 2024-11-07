import customtkinter as ct
import os
from PIL import Image
from tkinter import filedialog
import process_image


class Window(ct.CTk):
    image_path = ""

    def __init__(self):
        super().__init__()
        global image_path
        self.wm_title("Image Processing")
        self.geometry("2000x1200+0+0")
        self.winfo_screenwidth()
        ct.set_appearance_mode("dark")
        ct.set_default_color_theme("blue")
        self.iconbitmap('application-images/app-icon.ico')
        self.finalFrame()


        self.ndwindow()

        self.settings_image = ct.CTkImage(light_image=Image.open(os.path.join("application-images/setting.png")),
                                          dark_image=Image.open(os.path.join("application-images/setting(1).png")), size=(30, 30))

        self.frame = ct.CTkFrame(self, corner_radius=0)
        self.frame.grid(row=0, column=0, sticky="nsew")


        font = font=ct.CTkFont(family="Arial", size=25, weight="bold")

        self.settings_button = ct.CTkButton(self.frame,
                                            image=self.settings_image, hover_color=("gray40", "gray30"),
                                            text="", width=30, height=20, anchor="left" , command=self.set())
        self.settings_button.grid(row=0, column=1, padx=(100, 30), pady=10)
        self.label = ct.CTkLabel(self.frame, compound="right", text="SELECT YOUR IMAGE",font = font, width= 1250)
        self.label.grid(row=0, column=0, padx=(120, 10), pady=(160, 0))

        # Default Image Label
        self.defaultImage = ct.CTkImage(light_image=Image.open(os.path.join("application-images/gallery.png")),
                                        dark_image=Image.open(os.path.join("application-images/gallery.png")), size=(500, 300))
        self.defaultImage_Button = ct.CTkButton(self.frame, text="", image=self.defaultImage, fg_color="transparent",
                                                hover_color=("gray70", "gray30"), corner_radius=0,
                                                command=self.process)
        self.defaultImage_Button.grid(row=1, column=0, padx=(150, 20), pady=65)


    def ndwindow(self):
        global image_path

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # frame00  left frame

        self.frame00 = ct.CTkFrame(self, corner_radius=0)
        self.frame00.grid(row=0, column=0, sticky="nsew")
        self.frame00.grid_rowconfigure(12, weight=1)

        self.frame00_label = ct.CTkLabel(self.frame00, text="Outputs", compound="center",
                                         font=ct.CTkFont(family="Brush Script", size=20, weight="bold"))
        self.frame00_label.grid(padx=20, pady=20)

        self.original_button = ct.CTkButton(self.frame00, corner_radius=12, height=40, border_spacing=10,
                                            text="original",
                                            fg_color="transparent", text_color=("gray10", "gray90"),
                                            hover_color=("gray70", "gray30"),
                                            anchor="wright", command=self.original_button_event,
                                            font=ct.CTkFont(family="Brush Script", size=18, weight="bold"))

        self.original_button.grid(padx=20, pady=20)
        self.wShedseg = ct.CTkButton(self.frame00, corner_radius=12, height=40, border_spacing=10,
                                                text="ADAPTIVE THRESHOLD segmentation",
                                                fg_color="transparent", text_color=("gray10", "gray90"),
                                                hover_color=("gray70", "gray30"),
                                                anchor="wright", command=self.wShedseg_button_event,
                                                font=ct.CTkFont(family="Brush Script", size=18, weight="bold"))

        self.wShedseg.grid(padx=20, pady=20)
        self.threshold_button = ct.CTkButton(self.frame00, corner_radius=12, height=40, border_spacing=10, text="thresholding segmentation",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           anchor="wright", command=self.threshold_button_event,
                                           font=ct.CTkFont(family="Brush Script", size=18, weight="bold"))

        self.threshold_button.grid(padx=20, pady=20)
        self.negative_button = ct.CTkButton(self.frame00, corner_radius=12, height=40, border_spacing=10, text="negative transformation",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           anchor="wright", command=self.negative_button_event,
                                           font=ct.CTkFont(family="Brush Script", size=18, weight="bold"))

        self.negative_button.grid(padx=20, pady=20)
        self.log_button = ct.CTkButton(self.frame00, corner_radius=12, height=40, border_spacing=10, text="log transformation",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           anchor="wright", command=self.log_button_event,
                                           font=ct.CTkFont(family="Brush Script", size=18, weight="bold"))

        self.log_button.grid(padx=20, pady=20)
        self.powerL_button = ct.CTkButton(self.frame00, corner_radius=12, height=40, border_spacing=10, text="power low transformation",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           anchor="wright", command=self.powerL_button_event,
                                           font=ct.CTkFont(family="Brush Script", size=18, weight="bold"))

        self.powerL_button.grid(padx=20, pady=20)


        self.global_Button = ct.CTkButton(self.frame00, text="global transformation", corner_radius=10,
                                        command=self.all, height=30)
        self.global_Button.grid(padx=20, pady=(10, 20))





        self.appearance_mode_menu = ct.CTkOptionMenu(self.frame00, values=["System", "Dark", "Light"],
                                                     command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=10, column=0, padx=20, pady=20, sticky="s")

        self.scaling_optionemenu = ct.CTkOptionMenu(self.frame00, values=["80%", "90%", "100%", "110%", "120%", "150%"],
                                                    command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=11, column=0, padx=20, pady=(10, 20))

        # main frame
        self.main = ct.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main.grid(row=0, column=1, sticky="nsew")
        self.main.grid_rowconfigure(1, weight=1)
        self.main.grid_columnconfigure(0, weight=1)

        self.original_frame = ct.CTkLabel(self.main, text="")
        self.original_frame.grid(row=1, column=0, padx=50, pady=0, sticky="ew")
        self.original_image = ct.CTkImage(Image.open(os.path.join("application-images/img.jpg")), size=(500, 300))
        self.original_image_label = ct.CTkLabel(self.original_frame, text="", image=self.original_image)
        self.original_image_label.grid(row=0, column=0, padx=90, pady=10)

        self.back_Button = ct.CTkButton(self.frame00, text="Home", corner_radius=10,
                                        command=self.home, height=30)
        self.back_Button.grid(row=12, column=0, padx=20, pady=(10, 20))

    def finalFrame(self):

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Column 1: Settings Frame
        self.column1bar = ct.CTkFrame(self, corner_radius=0)
        self.column1bar.grid(row=0, column=0, sticky="nsew")
        self.column1bar.grid_rowconfigure(10, weight=1)

        self.column1bar_label = ct.CTkLabel(self.column1bar, text="Settings", compound="center",
                                            font=ct.CTkFont(family="Brush Script", size=20, weight="bold"))
        self.column1bar_label.grid(padx=20, pady=20)

        self.appearance_mode_menu = ct.CTkOptionMenu(self.column1bar, values=["System", "Dark", "Light"],
                                                     command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        self.scaling_option_menu = ct.CTkOptionMenu(self.column1bar,
                                                    values=["100%", "80%", "90%", "110%", "120%", "150%"],
                                                    command=self.change_scaling_event)
        self.scaling_option_menu.grid(row=7, column=0, padx=20, pady=(10, 20))

        self.back_Button = ct.CTkButton(self.column1bar, text="Home", corner_radius=10,
                                        command=self.home, height=30)
        self.back_Button.grid(row=8, column=0, padx=20, pady=(10, 20))

        # Column 2:  Outputs Frame enhance - seg
        self.enhancement_column = ct.CTkFrame(self, corner_radius=0)
        self.enhancement_column.grid(row=0, column=1, sticky="nsew")
        self.enhancement_column.grid_rowconfigure(4, weight=1)

        self.enhancement_column_label = ct.CTkLabel(self.enhancement_column, text="ENHANCEMENT OUTPUTS",
                                                    compound="center",
                                                    font=ct.CTkFont(family="Brush Script", size=20, weight="bold"))
        self.enhancement_column_label.grid(padx=250, pady=20)
        self.display_image("application-images/img.jpg", self.enhancement_column, row=0, column=1, text ="GRAYSCALE")
        self.display_image("application-images/img.jpg", self.enhancement_column, row=0, column=0, text="ORIGINAL")
        self.display_image('application-images/img.jpg', self.enhancement_column, row=1, column=0, text="ENHANCEMENT")
        self.display_image('application-images/img.jpg', self.enhancement_column, row=1, column=1, text="SEGMENTATION")



        self.enhancement_option_menu = ct.CTkOptionMenu(self.column1bar,
                                                        values=["enhancement","negative", "log"],
                                                        command=self.change_enhance_image, width=200)
        self.enhancement_option_menu.grid(row=1, column=0, pady=(100, 0))

        self.segmentation_option_menu = ct.CTkOptionMenu(self.column1bar,
                                                         values=["segmentation", "adaptive threshold", "thresholding"],
                                                         command=self.change_segmented_image, width=200)
        self.segmentation_option_menu.grid(row=2, column=0, pady=30)

        self.threshold_entry = ct.CTkEntry(self.column1bar , width=50 )
        self.d1_entry = ct.CTkEntry(self.column1bar , width=50 )
        self.d2_entry = ct.CTkEntry(self.column1bar , width=50 )
        self.threshold_entry.bind("<KeyRelease>", self.update_threshold_value)
        self.d1_entry.bind("<KeyRelease>", self.update_d1_value)
        self.d2_entry.bind("<KeyRelease>", self.update_d1_value)
    def display_image(self, image_path, parent_frame, row, column, text):
        image = Image.open(os.path.join(image_path))
        ctk_image = ct.CTkImage(image, size=(500, 300))
        font = ct.CTkFont(family="Brush Script", size=20, weight="bold")
        image_label = ct.CTkLabel(parent_frame, image=ctk_image, text=text, compound="top", font=font, pady=15)
        image_label.grid(row=row, column=column, padx=60, pady=10)


    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ct.set_widget_scaling(new_scaling_float)


    def change_enhance_image(self , new_enhance: str):
        if new_enhance == "negative":
            process_image.negative_transform('application-images/img.jpg')
            path = "enhance/negative.png"
            self.display_image(path , self.enhancement_column, row=1, column=0, text="NEGATIVE TRANSFORMATION (ENHANCEMENT)")
        elif new_enhance == "log":
            process_image.log_transform('application-images/img.jpg')
            path = "enhance/log.png"
            self.display_image(path , self.enhancement_column, row=1, column=0, text="LOG TRANSFORMATION (ENHANCEMENT)")

    def change_segmented_image(self , new_enhance: str):
        if new_enhance == "thresholding":
            process_image.Thresholding('application-images/img.jpg', 125)
            self.threshold_entry.grid(row=3, column=0, padx=30)
            self.d1_entry.grid_forget()
            self.d2_entry.grid_forget()
            path = "seg/thresholding.png"
            self.display_image(path , self.enhancement_column, row=1, column=1, text="THRESHOLDING SEGMENTATION")
        elif new_enhance == "adaptive threshold":
            process_image.global_adaptive_thresholding('application-images/img.jpg' , 11 , 2)
            self.threshold_entry.grid_forget()
            self.d1_entry.grid(row=3, column=0, padx=10)
            self.d2_entry.grid(row=4, column=0, padx=10)

            path = "seg/adaptive_threshold.png"
            self.display_image(path , self.enhancement_column, row=1, column=1, text="ADAPTIVE THRESHOLD SEGMENTATION")


    def change_appearance_mode_event(self, new_appearance_mode):
        ct.set_appearance_mode(new_appearance_mode)

    def original_button_event(self):
        self.original_image = ct.CTkImage(Image.open(os.path.join("application-images/img.jpg")), size=(500, 300))
        self.original_image_label = ct.CTkLabel(self.original_frame, text="", image=self.original_image)
        self.original_image_label.grid(row=0, column=0, padx=90, pady=10)

    def powerL_button_event(self):
        self.original_image = ct.CTkImage(Image.open(os.path.join("enhance/power.png")), size=(500, 300))
        self.original_image_label = ct.CTkLabel(self.original_frame, text="", image=self.original_image)
        self.original_image_label.grid(row=0, column=0, padx=90, pady=10)


    def log_button_event(self):
        self.original_image = ct.CTkImage(Image.open(os.path.join("enhance/log.png")), size=(500, 300))
        self.original_image_label = ct.CTkLabel(self.original_frame, text="", image=self.original_image)
        self.original_image_label.grid(row=0, column=0, padx=90, pady=10)


    def negative_button_event(self):
        self.original_image = ct.CTkImage(Image.open(os.path.join("enhance/negative.png")), size=(500, 300))
        self.original_image_label = ct.CTkLabel(self.original_frame, text="", image=self.original_image)
        self.original_image_label.grid(row=0, column=0, padx=90, pady=10)


    def threshold_button_event(self):
        self.original_image = ct.CTkImage(Image.open(os.path.join("seg/thresholding.png")), size=(500, 300))
        self.original_image_label = ct.CTkLabel(self.original_frame, text="", image=self.original_image)
        self.original_image_label.grid(row=0, column=0, padx=90, pady=10)

    def wShedseg_button_event(self):
        self.original_image = ct.CTkImage(Image.open(os.path.join("seg/adaptive_threshold.png")), size=(500, 300))
        self.original_image_label = ct.CTkLabel(self.original_frame, text="", image=self.original_image)
        self.original_image_label.grid(row=0, column=0, padx=90, pady=10)


    def process(self):
        self.select_image()
        self.select_frame("process")

    def home(self):
        self.select_frame("home")

    def all(self):
        self.select_frame("all")
        self.display_image("enhance/gray.png", self.enhancement_column, row=0, column=1, text ="GRAYSCALE")
        self.display_image("application-images/img.jpg", self.enhancement_column, row=0, column=0, text="ORIGINAL")
        self.display_image('enhance/log.png', self.enhancement_column, row=1, column=0, text="LOG TRANSFORMATION (ENHANCEMENT)")
        self.display_image('seg/thresholding.png', self.enhancement_column, row=1, column=1, text="THRESHOLDING SEGMENTATION")

    def set(self):
        return

    def update_threshold_value(self , event ):
        threshold_text = self.threshold_entry.get()
        if threshold_text.isdigit():
            x = int(threshold_text)
            if 0 <= x <= 256:
                process_image.Thresholding('application-images/img.jpg', x)
                self.threshold_entry.grid(row=3, column=0, padx=10)
                path = "seg/thresholding.png"
                self.display_image(path, self.enhancement_column, row=1, column=1, text="THRESHOLDING SEGMENTATION")
                print(0)


    def update_d1_value(self , event ):
        print(12)
        number1 = self.d1_entry.get()
        number2 = self.d2_entry.get()
        if number1.isdigit() and number2.isdigit():
            x = int(number1)
            y = int(number2)
            if (255 >= x >= 0 != x % 2) and 0 <= y <= 255:
                process_image.global_adaptive_thresholding('application-images/img.jpg', x , y)
                self.d1_entry.grid(row=3, column=0, padx=10)
                self.d2_entry.grid(row=4, column=0, padx=10)
                path = "seg/adaptive_threshold.png"
                self.display_image(path, self.enhancement_column, row=1, column=1, text="ADAPTIVE THRESHOLD SEGMENTATION")
                print(0)


    def select_frame(self, name):
        if name == "home":
            self.frame.grid(row=0, column=0, sticky="nsew")
            self.main.grid_forget()
            self.frame00.grid_forget()
        elif name == "process":
            self.main.grid(row=0, column=1, sticky="nsew")
            self.frame00.grid(row=0, column=0, sticky="nsew")
            self.frame.grid_forget()

        elif name == "all":
            self.column1bar.grid(row = 0 ,column = 0 , sticky = "nsew")
            self.enhancement_column.grid(row = 0 , column =1 , sticky = "nsew" )
            self.frame00.grid_forget()
            self.frame.grid_forget()
            self.main.grid_forget()

    def select_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Image File",
            filetypes=[("Image Files", ("*.png", "*.jpg", "*.jpeg", "*.gif"))]
        )

        if file_path:
            process_image.save_picture(process_image.get_path(file_path))

            self.original_image = ct.CTkImage(Image.open(os.path.join("application-images/img.jpg")), size=(500, 300))
            self.original_image_label = ct.CTkLabel(self.original_frame, text="", image=self.original_image)
            self.original_image_label.grid(row=0, column=0, padx=90, pady=10)


            process_image.log_transform('application-images/img.jpg')
            process_image.negative_transform('application-images/img.jpg')
            process_image.global_adaptive_thresholding('application-images/img.jpg' , 11 , 2)
            process_image.Thresholding('application-images/img.jpg', 125)
            process_image.power_law_transform('application-images/img.jpg')

if __name__ == "__main__":
    app = Window()
    app.mainloop()
