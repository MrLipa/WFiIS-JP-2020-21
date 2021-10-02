print("##########1##########")
import random
try:
    k = [[random.randrange(100) for _ in range(3)] for _ in range(3)]
    print(k)  # ([89, 69, 58], (31, 60, 39], [65, 81, 19]
    s = 0
    for el in k:
        if all(x % 2 for x in el):
            break
        s+=len(list(filter(lambda x: x%2,el)))/len(list(filter(lambda x: not x%2,el)))
    else:
        print('s1=',s)
except:
    print('wyjatek')
else:
    print('s2=',s)


print()
print("##########2##########")
import sys
x,y=1,2
try:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    x //= y
except ZeroDivisionError:
    print('y = 0!')
except IndexError:
    print('wywolanie: ./ prog a b')
except ValueError:
    print('wywolanie: ./ prog liczba1 liczba2')
else:
    print(x)
finally:
    print(x/y)


print()
print("##########3##########")
import sys
x,y=1,2
try:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    x //= y
except ZeroDivisionError:
    print('y = 0!')
except IndexError:
    print('wywolanie: ./ prog a b')
except ValueError:
    print('wywolanie: ./ prog liczba1 liczba2')
else:
    print(x)
finally:
    x,y=1,2
    print(x/y)


print()
print("##########4##########")
import sys
try:
    print (eval(sys.argv [0]. format (sys. argv [1])))
except:
    print ('wyjatek')


print()
print("##########5##########")
import sys
x,y=1,2
try:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    x //= y
except ZeroDivisionError:
    print('y = 0!')
except IndexError:
    print('wywolanie: ./ prog a b')
except ValueError:
    print('wywolanie: ./ prog liczba1 liczba2')
else:
    print(x)
finally:
    print(x/y)


print()
print("##########6##########")
class W:
    pass
raise W


print()
print("##########7##########")
# try:
#     x=int ('3.')
# except:
#     print('all')
# except ValueError:
#     print ('ValueError')


print()
print("##########8##########")
def fun(p):
    import math
    assert p>0
    return math.sqrt (p)
try:
    fun(-9)
except AssertionError:
    print ('AssertionError')
except ValueError:
    print ('ValueBrror')


print()
print("##########9##########")
import sys
x,y=1,2
try:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    x //= y
except ZeroDivisionError:
    print('y = 0!')
except IndexError:
    print('wywolanie: ./ prog a b')
except ValueError:
    print('wywolanie: ./ prog liczba1 liczba2')
else:
    print(x)
finally:
    print(x/y)


print()
print("##########10##########")
def fun(p):
    import math
    if p<0:
        raise ValueError('p<0')
    return math. sqrt (p)
try:
    try:
        print (fun(-9))
    except ValueError:
        raise
        print ('ValueError')
except:
    print ('all')