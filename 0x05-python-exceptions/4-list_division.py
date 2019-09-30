#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final = []
    for x in range(list_length):
        try:
            new = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            print("division by 0")
            new = 0
        except TypeError:
            print("wrong type")
            new = 0
        except IndexError:
            print("out of range")
            new = 0
        except:
            new = 0
        finally:
            final.append(new)
    return final
