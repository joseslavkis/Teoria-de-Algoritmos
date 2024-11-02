def candidato(arr):
    if len(arr)==1:
        return arr[0]
    if len(arr)==0:
        return None

    vector_nuevo=[]
    for i in range(0,len(arr)-1,2):
        if arr[i]==arr[i+1]:
            vector_nuevo.append(arr[i])
 
    repetido=candidato(vector_nuevo)
    if repetido is not None:
        return repetido    

    ult_ele=None
    if len(arr)%2!=0:
        ult_ele=arr[-1]
    if ult_ele is not None and arr.count(ult_ele)>(len(arr)*(2/3)):
        return ult_ele
    return None

def mas_de_dos_tercios(arr):
    posible_num=candidato(arr)
    if posible_num is None:
        return False
    if arr.count(posible_num)>(len(arr) * (2/3)):
        return True
    return False