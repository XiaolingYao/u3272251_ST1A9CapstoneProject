from model import boxcoxY_XGBPredictor
from diamond import Diamond
import tkinter as tk
import tkinter.messagebox

# GUI validation for Diamond Predictor
class diamondPredictorGUI():
    __diamond = Diamond(carat = 0.2, cut = 'Unknown', color = 'Unknown', clarity = 'Unknown', x = 0.0, y = 0.0, z = 0.0)
    __XGBModel = boxcoxY_XGBPredictor('u3272251XGB.pkl')
    __cutStand = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
    __colorStand = ['J', 'I', 'H', 'G', 'F', 'E', 'D']
    __clarityStand = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']

    def __init__(self):
        self.root = tk.Tk()
        # GUI title
        self.root.title("Diamond Price Predictor")

        # GUI window size
        self.root.geometry("600x450")  # Width x Height

        # Disable resizing the GUI
        self.root.resizable(False, False)

        # Set Tkinter variable for later retrieving
        self.carat = tk.StringVar()
        self.x = tk.StringVar()
        self.y = tk.StringVar()
        self.z = tk.StringVar()
        self.cut = tk.StringVar()
        self.color = tk.StringVar()
        self.clarity = tk.StringVar()

        # Widgets: Label to display the title
        self.lblTitle = tk.Label(self.root, text='Diamond Price Predictor', bg = '#ebfeff' , font = ("Calibri", 20, "bold"))
        self.lblTitle.grid(row = 0 , column = 0, columnspan = 9, padx = 5, pady = 10)

        # Widgets: Labels for required data input sections
        self.lblSubTitles = ['Diamond Carat:', 'Diamond Size:', 'Diamond Cut:', 'Diamond Color:', 'Diamond Clarity:']
        self.indexlbl = 1
        for lbl in self.lblSubTitles:
            self.label = tk.Label(self.root, text = lbl, font = ("Calibri", 16, "bold"))
            self.label.grid(row = self.indexlbl, column = 0 , padx = 5, pady = 1, sticky = 'E')
            self.indexlbl += 1

        # Widget: Entry Carat
        self.entCarat = tk.Entry(self.root, textvariable = self.carat, width = 20, )
        self.entCarat.grid(row = 1, column = 1, columnspan = 8, padx = 1, pady = 1, sticky = 'W')

        # Widgets: Label and Entry x (width), y (length), z(depth) in the same row
        self.framexyz = tk.Frame(self.root)
        self.framexyz.grid(row = 2, column = 1, columnspan = 8, padx = 1, pady = 1, sticky = 'W')

        self.lblxyz = ['Width:', 'Length:', 'Depth:', '(mm)']
        self.indexlbl = 1
        for lbl in self.lblxyz:
            self.label = tk.Label(self.framexyz, text=lbl)
            self.label.grid(row = 0, column = self.indexlbl, padx = 1, pady = 1)
            self.indexlbl += 2

        self.entx = tk.Entry(self.framexyz, textvariable = self.x, width=3)
        self.enty = tk.Entry(self.framexyz, textvariable = self.y, width=3)
        self.entz = tk.Entry(self.framexyz, textvariable = self.z, width=3)
        self.entx.grid(row = 0, column = 2, padx = 1, pady = 1, sticky = 'W')
        self.enty.grid(row = 0, column = 4, padx = 1, pady = 1, sticky = 'W')
        self.entz.grid(row = 0, column = 6, padx = 1, pady = 1, sticky = 'W')

        # Widget: Check Bottons for cut
        self.frameCut = tk.Frame(self.root)
        self.frameCut.grid(row = 3, column = 1, columnspan = 8, padx = 1, pady = 1, sticky = 'W')
        self.chkbindex = 1
        for chkbkey in self.__cutStand:
            self.chkbCut = tk.Checkbutton(self.frameCut, text = chkbkey, variable = self.cut, onvalue = chkbkey, offvalue = '')
            self.chkbCut.grid(row = 0, column = self.chkbindex, padx = 1, pady = 1, sticky = 'W')
            self.chkbindex += 1


        # Widget: Check Bottons for color
        self.frameColor = tk.Frame(self.root)
        self.frameColor.grid(row = 4, column = 1, columnspan = 8, padx = 1, pady = 1, sticky = 'W')
        self.chkbindex = 1
        for chkbkey in self.__colorStand:
            self.chkbColor = tk.Checkbutton(self.frameColor, text = chkbkey, variable = self.color, onvalue = chkbkey, offvalue = '')
            self.chkbColor.grid(row = 0, column = self.chkbindex, padx = 1, pady = 1, sticky = 'W')
            self.chkbindex += 1


        # Widget: Check Bottons for clarity
        self.frameClarity = tk.Frame(self.root)
        self.frameClarity.grid(row = 5, column = 1, columnspan = 8, padx = 1, pady = 1, sticky = 'W')
        self.chkbindex = 1
        for chkbkey in self.__clarityStand:
            self.chkbClarity = tk.Checkbutton(self.frameClarity, text = chkbkey, variable=self.clarity, onvalue = chkbkey, offvalue = '')
            self.chkbClarity.grid(row = 0, column = self.chkbindex, padx = 1, pady = 1, sticky = 'W')
            self.chkbindex += 1


        # Widget: Predict the Price of Diamond (Button)
        self.btnPrint = tk.Button(self.root, text = "Predict the Price", command = self.predictGUI)
        self.btnPrint.grid(row = 6, column = 1, columnspan = 3, padx = 5, pady = 5)

        # Widget: Quit the GUI program (Button)
        self.btnQuit = tk.Button(self.root, text = "Quit", command = self.root.destroy)
        self.btnQuit.grid(row= 6 , column = 4, columnspan = 2, padx = 5, pady = 5)

        # Widget: Prediction Display
        self.lblPredict = tk.Label(self.root, text = 'Prediction Result', font = ("Calibri", 16, "bold"))
        self.lblPredict.grid(row = 7, column = 0, padx = 5, pady = 5, sticky = 'E')
        self.textPrediction = tk.Text(self.root, height = 10, bg = '#ebfeff')
        self.textPrediction.grid(row = 8, column = 0, columnspan = 9, padx = 5, pady = 5, sticky = 'NSWE')

        # Wait in the main loop until event handler click
        tk.mainloop()

    # Call when clicking the Predict Button on GUI
    def predictGUI(self):
        # Empty the text widget
        self.textPrediction.delete('1.0', 'end')

        # carat, width, length, and depth are required
        if not (self.carat.get() == '' or self.x.get() == '' or self.y.get() == '' or self.z.get() == ''):
            # Try converting the input to float, if cannot, terminate here
            try:
                # raise ValueError if input carat <= 0 (set in Diamond)
                self.__diamond.carat = float(self.carat.get())
                self.__diamond.x = float(self.x.get())
                self.__diamond.y = float(self.y.get())
                self.__diamond.z = float(self.z.get())
            except ValueError as Err:
                # Pop the Error
                tk.messagebox.showinfo("Error: ", Err)
                return

            # Remind the Warning for low confident result
            if self.__diamond.carat < 0.2 or self.__diamond.carat > 5:
                tk.messagebox.showinfo("Warning: ",
                                       'Low confidence prediction result when the carat of the diamond is not in range of (0.2 to 5.0)')
            # Remind the Warning for low confident result
            if self.__diamond.x == 0.0 or self.__diamond.y == 0.0 or self.__diamond.z == 0.0:
                tk.messagebox.showinfo("Warning: ",
                                        'Low confidence prediction result when giving far to carat width, length, and depth')

            if self.cut.get() != '':
                self.__diamond.cut = self.cut.get()
            if self.color.get() != '':
                self.__diamond.color = self.color.get()
            if self.clarity.get() != '':
                self.__diamond.clarity = self.clarity.get()

            result_string = '\n' + '=' * 70
            result_string += f'\nThe Predicted Price for Your Diamond: {self.__XGBModel.predict(data=self.__diamond.predictionData())}\n'
            result_string += '-' * 70 + '\n' + self.__diamond.info() + '=' * 70 + '\n'

            self.textPrediction.insert('1.0', result_string)
        else:
            tk.messagebox.showinfo("Warning: ", 'Required Value: carat, width, length, and depth.')

def main():
    diamondPredictor = diamondPredictorGUI()
    diamondPredictor

if __name__ == '__main__':
    main()
