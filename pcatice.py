from socket import J1939_IDLE_ADDR


jumin = "891228-1058521"
print("성별" +jumin[7] )   #첫자리가 0
print("연도" +jumin[0:2])  # 0~2 직전까지
print("월" + jumin[2:4])
print("날짜" + jumin[4:6])
print("주민번호 : " +jumin[:6])    #처음부터 6까지
print("주민번호 뒷자리 : " + jumin[7:14])  #7부터 끝까지

print("주민번호 뒷자리 뒤에서 부터" +jumin[-7:])

python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper())

print(python.replace("Python" , "JaVa"))

print(jumin.lower())
print(jumin.upper())
print(jumin.replace ("89" , "ad"))

print(python.index("n"))
index = python.index("n")
print(index)