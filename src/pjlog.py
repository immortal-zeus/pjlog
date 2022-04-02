import math
class log():
    ''' A simple Class of Logarithm with helpful functions. Base 10 is default.  '''
    Base = 0
    Argument = 0
    Characteristic = 0
    Mantissa = 0

    def __init__(self,value , base = 10 ):
        if base == 'e' or base == 'E':
            self.Argument = value
            self.Base = 2.718
            self.__find_char_man__(self.Argument, self.Base)

        else:
            if type(base)== int or type(base)==float:
                base = float(base)
                if base ==1 or base <1:
                    raise Exception("LogBase has to be Greater than one.")

                if value <=0:
                    raise ValueError("Outside Log domain")

                self.Argument = value
                self.Base = base
                self.__find_char_man__(self.Argument, self.Base)

            else:
                raise TypeError("Base has to be a Number. ")

    def __find_char_man__(self, value , base):
        '''
        Function to Calculate Characteristic and Mantissa of Logarithm.
        :param value: Arugument of Logarithm
        :param base: Base of Logarithm
        :return: None
        '''
        temp_log = math.log(value, base)
        if value%base == 0 :
            self.Characteristic = round(temp_log)
            self.Mantissa = float(0)
        else:
            self.Mantissa , self.Characteristic = math.modf(temp_log)

    def __add__(self, other):
        if self.Base == other.Base:
            return log(self.Argument * other.Argument, self.Base)
        else:
            print("Due to difference in log bases, Please enter in which Base the answer should be in : ")
            temp_base = float(input())
            sum_temp_base = (math.log(self.Argument, temp_base) / math.log(self.Base, temp_base)) + (math.log(other.Argument, temp_base) / math.log(other.Base, temp_base))
            return log(math.pow(temp_base,sum_temp_base) , temp_base)

    def __sub__(self, other):
        if self.Base == other.Base :
            return log(self.Argument / other.Argument, self.Base)
        else:
            print("Due to difference in log bases, Please enter in which Base the answer should be in : ")
            temp_base = float(input())
            sum_temp_base = (math.log(self.Argument, temp_base) / math.log(self.Base, temp_base)) - (math.log(other.Argument, temp_base) / math.log(other.Base, temp_base))
            return log(math.pow(temp_base, sum_temp_base), temp_base)

    def __mul__(self, other):
        if self.Base == other.Base:
            temp_mul_val = (self.Characteristic + self.Mantissa) * (other.Characteristic + other.Mantissa)
            return log(math.pow(self.Base, temp_mul_val), self.Base)
        else:
            print("Due to difference in log bases, Please enter in which Base the answer should be in : ")
            temp_base = float(input())
            temp_mul_val = (self.Characteristic + self.Mantissa) * (other.Characteristic + other.Mantissa)
            return log(math.pow(temp_base, temp_mul_val) , temp_base)

    def __truediv__(self, other):
        if self.Base == other.Base:
            temp_mul_val = (self.Characteristic + self.Mantissa) / (other.Characteristic + other.Mantissa)
            return log(math.pow(self.Base, temp_mul_val), self.Base)
        else:
            print("Due to difference in log bases, Please enter in which Base the answer should be in : ")
            temp_base = float(input())
            temp_mul_val = (self.Characteristic + self.Mantissa) / (other.Characteristic + other.Mantissa)
            return log(math.pow(temp_base, temp_mul_val) , temp_base)

    def __radd__(self, other):
        raise Exception("Will implemented in future versions.")

    def __rsub__(self, other):
        raise Exception("Will implemented in future versions.")

    def __rmul__(self, other):
        raise Exception("Will implemented in future versions.")

    def __rtruediv__(self, other):
        raise Exception("Will implemented in future versins.")

    def __floordiv__(self, other):
        if self.Base == other.Base:
            temp_mul_val = (self.Characteristic) // (other.Characteristic)
            return log(math.pow(self.Base, temp_mul_val), self.Base)
        else:
            print("Due to difference in log bases, Please enter in which Base the answer should be in : ")
            temp_base = float(input())
            temp_mul_val = (self.Characteristic) // (other.Characteristic)
            return log(math.pow(temp_base, temp_mul_val), temp_base)

    def __str__(self):
        return f"Argument : {self.Argument}" +"\n"+ f"Base : {self.Base}"+"\n"+ f"Characteristic : {self.Characteristic}" +"\n"+ f"Mantissa : {self.Mantissa}"

    def __repr__(self):
        return f"Lof({self.Argument} , {self.Base})"

    def __lt__(self, other):
        return (self.Characteristic + self.Mantissa) < (other.Characteristic + other.Mantissa)

    def __le__(self, other):
        return (self.Characteristic + self.Mantissa) <= (other.Characteristic + other.Mantissa)

    def __eq__(self, other):
        return (self.Characteristic + self.Mantissa) == (other.Characteristic + other.Mantissa)

    def __ne__(self, other):
        return (self.Characteristic + self.Mantissa) != (other.Characteristic + other.Mantissa)

    def __gt__(self, other):
        return (self.Characteristic + self.Mantissa) > (other.Characteristic + other.Mantissa)

    def __ge__(self, other):
        return (self.Characteristic + self.Mantissa) >= (other.Characteristic + other.Mantissa)

    def Lmultiple(self, value):
        '''
        Function to multiple a number(Int/Float) with Logarithm.
        :param value: Argument of the Logarithm
        :return: log object
        '''
        return log(math.pow(self.Argument, value), self.Base)

    def Lbase_change(self,base):
        '''
        Function to Change the base of Logarithm.
        :param base: Base of the Logarithm
        :return: log object
        '''
        base_change = math.log(self.Argument, base) / math.log(self.Base, base)
        return log(math.pow(base, base_change), base)

    def Lget_value(self):
        '''
        Funtion to Calculate the Logarithm.
        :return: Float
        '''
        return self.Characteristic+self.Mantissa



