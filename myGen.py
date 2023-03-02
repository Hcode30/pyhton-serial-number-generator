"""
myGen can be used to Generates a random char or int
using the random_element function and essentially
is used to Generates a Serial number consists of ints and chars
you can choose the base struct of the gen using get function
you can choose the separator also
"""


from string import ascii_letters, digits
from random import randint


class generator():
    def random_element():
        """
        returns a random char or integer
        """
        alpha = ascii_letters + digits * \
            randint(1, 3)  # Increasing The Chances Of getting an integer in return
        num = len(alpha)
        random_num = randint(0, num - 1)
        return alpha[random_num]

    def __part(count, any_List):
        for i in range(count):
            any_List.append(generator.random_element())
        return ("".join(any_List))

    def get(* args, separator="-"):
        """
        Choose How To Struct Your Serial number
        You Can Add int arguments like:
        'generator.get(4,2,3)=> xxxx-xx-xxx'
        or you can add an iterable as an argument
        """
        iters = [list, tuple, set]
        if (len(args) == 2 or len(args) == 1) and type(args[0]) in iters:
            if len(args) == 2:
                separator = args[1]
                my_iter1 = args[0]
            else:
                my_iter1 = args[0]

            serial = []
            for letter in my_iter1:
                generator.__part(letter, serial)
                serial.append(f"{separator}")
            serial[-1] = ""
        else:
            if type(args[-1]) != int:
                separator = args[-1]
            my_iter1 = args
            my_iter2 = []
            serial = []
            for p in filter(lambda valid: type(valid) == int, my_iter1):
                my_iter2.append(p)
            for letter in my_iter2:
                generator.__part(letter, serial)
                serial.append(f"{separator}")
            serial[-1] = ""

        return "".join(serial)

    def genBulk(* args, separator="-", quantity=1):
        """
        get bulk serial numbers by specifying quantity 
        in the end , How To Use It : 
        'generator.bulk(struct iterator,separator,quantity)'
        Example: generator.bulk([4, 2, 6],"=",2)
            91Y6=aB=JDn9Iz
            3Mzn=Wg=Ko1TeK
        """
        separator = args[1]
        quantity = args[2]
        for serial in range(quantity):
            print(f"{generator.get(* args[0], separator)}")


# Examples:
# print(generator.get((4, 2, 6))) # ex uvWn-g2-0K72TS
# print(generator.get((4, 2, 6, 13), " ^ ")) # ex ie1f ^ dJ ^ JhdR7T ^ lre66EZYan7Ki
# generator.genBulk([4, 2, 6], "__", 6) # ex PTAm__T6__uc22Lc
# generator.genBulk([4, 2, 6], "=", 2) # ex    uaMX2__1X__ok3CsB      SFSg__SH__Is0412
# print(generator.get(4, 2, 6, 1, 3)) # ex JHaz__rA__hwSGIk    CUi6__vD__Q242dP   79wU__fg__0qdTc4 
# print(generator.random_element()) # ex C
