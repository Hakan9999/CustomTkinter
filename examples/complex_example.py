import tkinter
import tkinter.messagebox
import customtkinter
import sys

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 700
    HEIGHT = 500

    def __init__(self):
        super().__init__()

        self.title("CustomTkinter complex example")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        if sys.platform == "darwin":
            self.bind("<Command-q>", self.on_closing)
            self.bind("<Command-w>", self.on_closing)
            self.createcommand('tk::mac::Quit', self.on_closing)

        # ============ create two frames ============

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.grid_columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(5, weight=1)
        self.frame_left.grid_rowconfigure(8, minsize=10)

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="CustomTkinter",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="CTkButton 1",
                                                command=self.button_event,
                                                fg_color=("gray75", "gray30"))  # <- custom tuple-color
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="CTkButton 2",
                                                command=self.button_event,
                                                fg_color=("gray75", "gray30"))  # <- custom tuple-color
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="CTkButton 3",
                                                command=self.button_event,
                                                fg_color=("gray75", "gray30"))  # <- custom tuple-color
        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        self.check_box_1 = customtkinter.CTkCheckBox(master=self.frame_left,
                                                     text="CTkCheckBox")
        self.check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_left,
                                                     text="Dark Mode",
                                                     command=self.change_mode)
        self.check_box_2.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        for i in [0, 1, 2, 3]:
            self.frame_right.rowconfigure(i, weight=1)
        self.frame_right.rowconfigure(6, weight=10)
        self.frame_right.columnconfigure(0, weight=1)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="wens")

        # ============ frame_right -> frame_info ============

        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="CTkLabel: Lorem ipsum dolor sit,\n" +
                                                        "amet consetetur sadipscing elitr,\n" +
                                                        "sed diam nonumy eirmod tempor\n" +
                                                        "invidunt ut labore",
                                                   width=240,
                                                   height=100,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info, width=240)
        self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)

        # ============ frame_right <- ============
        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        fg_color=("white", "gray30"),  # <- custom tuple-color
                                                        text="CTkRadioButton Group:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=0, padx=20, sticky="wes")

        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                      variable=self.radio_var,
                                                      value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="")

        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="")

        #self.radio_button_1.select()
        #self.radio_button_1.deselect()

        self.slider_1 = customtkinter.CTkSlider(master=self.frame_right,
                                                from_=1,
                                                to=0,
                                                number_of_steps=3,
                                                command=self.progressbar.set)
        self.slider_1.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="we")
        self.slider_1.set(0.7)

        self.slider_2 = customtkinter.CTkSlider(master=self.frame_right,
                                                command=self.progressbar.set)
        self.slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")
        self.slider_2.set(0.7)

        self.slider_button_1 = customtkinter.CTkButton(master=self.frame_right,
                                                height=25,
                                                text="CTkButton",
                                                command=self.button_event)
        self.slider_button_1.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.slider_button_2 = customtkinter.CTkButton(master=self.frame_right,
                                                height=25,
                                                text="CTkButton",
                                                command=self.button_event)
        self.slider_button_2.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="CTkEntry")
        self.entry.grid(row=7, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="CTkButton",
                                                command=self.button_event)
        self.button_5.grid(row=7, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        self.progressbar.set(0.5)

    def button_event(self):
        print("Button pressed")

    def change_mode(self):
        if self.check_box_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
