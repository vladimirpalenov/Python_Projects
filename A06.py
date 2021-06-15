# Assignment 6

# imports
import pickle
import tkinter


class GenomicData:
    def __init__(self):
        file = open("genome_counts.dat", "rb")
        self.genome_data = pickle.load(file)
        file.close()


class GENOME_UI:
    def __init__(self):
        self.__CANVAS_WIDTH = 320  # Canvas  width
        self.__CANVAS_HEIGHT = 240  # Canvas  height
        self.__genomes = GenomicData()
        self.__data = self.__genomes.genome_data
        self.__name = "sars_cov_2"
        self.__names = []  # name of genome (key  from  dictionary)
        for k in self.__data:
            self.__names.append(k)
        # Create  the  main  window.
        self.main_window = None
        self.canvas = None

    def close_window(self):
        self.main_window.destroy()

    def set_genome(self, name):
        self.__name = name

    def get_names(self):
        return self.__names

    def draw_piechart(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Aminoacid Pie Chart")
        # Create  the  Canvas  widget.
        self.canvas = tkinter.Canvas(self.main_window, width=self.__CANVAS_WIDTH, height=self.__CANVAS_HEIGHT)
        self.__X1 = 60  # Upper -left X of  bounding  rectangle
        self.__Y1 = 20  # Upper -left Y of  bounding  rectangle
        self.__X2 = 260  # Lower -right X of  bounding  rectangle
        self.__Y2 = 220  # Lower -right Y of  bounding  rectangle

        # Todo A6: get the  name of the  genome  entered
        # set the  slice  color  and  slice  extent (width)
        # from  the  self.__data  member  variable
        startPoint = 0

        # accessing AGTC data from the dictionary and saving it in variables
        a = self.__data[self.__name][0]
        g = self.__data[self.__name][1]
        t = self.__data[self.__name][2]
        c = self.__data[self.__name][3]
        # the total number of amino acids in the virus (100%)
        total = a + g + t + c
        extentA = a / total * 360
        extentG = g / total * 360
        extentT = t / total * 360
        extentC = c / total * 360

        # Todo A6 - create  the pie  chart
        # your  code  for  drawing  the pie  charts  goes  here
        # use  program  13-19 as an  example  for how to use
        # the  create_arc  method  of the  tkinter
        # canvas  drawing  object
        #
        # Todo A6 draw  the  arcs
        # draw  slice 1 of A’s
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, self.__Y2, start=startPoint, extent=extentA, fill='green')
        startPoint = startPoint + extentA
        # draw  slice 2 of G’s
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, self.__Y2, start=startPoint, extent=extentG, fill='red')
        startPoint = startPoint + extentG
        # draw  slice 3 of T’s
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, self.__Y2, start=startPoint, extent=extentT, fill='blue')
        startPoint = startPoint + extentT
        # draw  slice 4 of C’s
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, self.__Y2, start=startPoint, extent=extentC, fill='orange')
        #startPoint = 0
        # Optional  Todo A6: create  figure  title  and  slice  labels
        # optional  figure  title  using  create_text
        self.canvas.create_text(160, 8, text=self.__name)
        # optional  lines to  labels  using  create_line  and  create_text
        self.canvas.pack()
        tkinter.mainloop()


# Create  an  instance  of the  Genome  UI class.
while True:
    print("Close  the  figure  window  to  create  another  pie  chart  or exit")
    genome_ui = GENOME_UI()
    names = genome_ui.get_names()
    print("Choose a genome  name to view  the  AGTC  frequency  pie  chart")
    for name in names:
        print(name)
    name = input()
    genome_ui.set_genome(name)
    # Create  an  instance  of the  GENOME\_UI  class.
    genome_ui.draw_piechart()
    response = input("Do you  want to see  another  figure (yes or no)? ")
    if response == "no":
        print("goodbye")
        break
