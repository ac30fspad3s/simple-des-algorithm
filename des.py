import math

def shift(st, steps):  #циклический сдвиг
    lst = []
    lst.extend(st)
    if steps < 0:       # - влево
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:              # вправо
        for i in range(steps):
            lst.insert(0, lst.pop())
    return lst

def xor(st1, st2): #xor
    st3 = []
    for i in range(len(st1)):
        st3.append(st1[i]^st2[i])
    return st3

def permutation(st, perm): #перестановка списка st по индексам из списка perm
    buff = []
    for i in perm:
        buff.append(st[i])
    st.clear()
    st.extend(buff)


def rl(st): # разбиение списка на 2
    left_st = []
    right_st = []
    for i in range(int(len(st)/2)):
        left_st.append(st[i])
    for i in range(int(len(st)/2), len(st)):
        right_st.append(st[i])
    return left_st, right_st 

def keys(key): # формирование раундовых ключей
    p10=[]
    p10_left=[]
    p10_right=[]
    key1 = []
    key2 = []
 
    permutation(key,[2,4,1,6,3,9,0,8,7,5]) #перестановка 35274101986
    lr_keys = rl(key)
    p10_left.extend(lr_keys[0])
    p10_right.extend(lr_keys[1])
    key1 = shift(p10_left,-1) + shift(p10_right,-1)
    key2 = shift(p10_left,-3) + shift(p10_right,-3)
   # print(key2)
    permutation(key1, [5,2,6,3,7,4,9,8]) # перестановка 637485109
    permutation(key2, [5,2,6,3,7,4,9,8]) # перестановка 637485109
  
    return key1,key2

def F(st_, key): #преобразование F
    st = []
    st.extend(st_)
    permutation(st, [3,0,1,2,1,2,3,0])
    st_lr = rl(xor(st,key))
    st_left = st_lr[0]
    st_right = st_lr[1]

    #блоки s1 и s2 записанные в виде матриц, элементы матрицы записаны в виде бинарного списка
    matrix_s1 = [ [[0,1],[0,0],[1,1],[1,0]] , [[1,1],[1,0],[0,1],[0,0]] , [[0,0],[1,0],[0,1],[1,1]] , [[1,1],[0,1],[1,1],[0,1]] ]
    matrix_s2 = [ [[0,1],[0,1],[1,0],[1,1]] , [[1,0],[0,0],[0,1],[1,1]] , [[1,1],[0,0],[0,1],[0,0]] , [[1,0],[0,1],[0,0],[1,1]] ]

    #выбор элементов матриц
    coloumn_s1 = int(str(st_left[1])+str(st_left[2]), base=2)
    coloumn_s2 = int(str(st_right[1])+str(st_right[2]), base=2)
    line_s1 = int(str(st_left[0])+str(st_left[3]), base=2)    
    line_s2 = int(str(st_right[0])+str(st_right[3]), base=2)   
    
    result = matrix_s1[line_s1][coloumn_s1]  +  matrix_s2[line_s2][coloumn_s2]
    permutation(result ,[1,3,2,0]) # перестановка 2431
    return result
    
def des(st, key):

   
    k = keys(key)
    k1 = k[0]
    k2 = k[1]
    permutation(st, [1,5,2,0,3,7,4,6]) #начальная перестановка 26314857   
    st_lr = rl(st)
    round1_st_left = xor(F(st_lr[1],k1), st_lr[0])
    round1_st_right = (st_lr[1])
    round2_st_left = xor(F(round1_st_left, k2), round1_st_right)
    round2_st_right = round1_st_left
    result = round2_st_left + round2_st_right
    permutation(result, [3,0,2,4,6,1,7,5]) # конечная перестановка 41357286
    return result

def main():
   
# входные и выходные данные, ключ представленны в виде бинарного списк

    input1 = [0,0,1,0,1,1,1,0]
    key1 = [1,0,0,1,1,1,1,1,0,1]

    print("input  : ", input1)
    print("key    : ", key1)
    print("output : ", des(input1, key1))
    
main()
