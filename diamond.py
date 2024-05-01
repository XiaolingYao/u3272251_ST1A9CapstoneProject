import numpy as np

class Diamond:
    def __init__(self, carat, cut, color, clarity, x, y, z):
        self.__carat = carat
        self.__cut = cut
        self.__color = color
        self.__clarity = clarity
        self.__x = x
        self.__y = y
        self.__z = z
        self.__cutStand = {'Unknown': 0, 'Fair': 1, 'Good': 2, 'Very Good': 3, 'Premium': 4, 'Ideal': 5}
        self.__colorStand = {'Unknown': 0, 'J': 1, 'I': 2, 'H': 3, 'G': 4, 'F': 5, 'E': 6, 'D': 7}
        self.__clarityStand = {'Unknown': 0, 'I1': 1, 'SI2': 2, 'SI1': 3, 'VS2': 4, 'VS1': 5, 'VVS2': 6, 'VVS1': 7, 'IF': 8}

    @property
    def carat(self):
        return self.__carat

    @carat.setter
    def carat(self, new_carat):
        if (not isinstance(new_carat, (float, int))) or new_carat <= 0:
            raise ValueError('Please enter the Value > 0')
        else:
            self.__carat = new_carat

    @property
    def cut(self):
        return self.__cut

    @cut.setter
    def cut(self, new_cut):
        self.__cut = new_cut

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    @property
    def clarity(self):
        return self.__clarity

    @clarity.setter
    def clarity(self, new_clarity):
        self.__clarity = new_clarity

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        self.__x = new_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        self.__y = new_y

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, new_z):
        self.__z = new_z

    def __str__(self):
        return f'This diamond is {self.__x}*{self.__y}*{self.__z}(mm), weight: {self.__carat} carat.\nLevels of this diamond: cut-{self.__cut}, color-{self.__color}, clarity-{self.__clarity}\n'

    __repr__ = __str__

    # Method to convert the diamond's info into predictable data type and transformation.
    # Order: log_carat, cut, color, clarity, x, y, z
    # Type: numpy array
    def predictionData(self):
        return np.array([[np.log10(self.__carat), self.__cutStand[self.__cut],
                          self.__colorStand[self.__color], self.__clarityStand[self.__clarity],
                          self.__x, self.__y, self.__z]])

    def info(self):
        return f'This diamond is {self.__x}*{self.__y}*{self.__z}(mm), weight: {self.__carat} carat.\nLevels of this diamond: cut-{self.__cut}, color-{self.__color}, clarity-{self.__clarity}\n'
