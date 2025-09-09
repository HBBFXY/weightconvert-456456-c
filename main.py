weight, unit = input().split()
weight = float(weight)

if unit == "kg":
    pounds = weight * 2.2046
    print(f"{weight:.3f} kg = {pounds:.3f} pd")
elif unit == "pd":
    kilograms = weight / 2.2046
    print(f"{weight:.3f} pd = {kilograms:.3f} kg")
else:
    print("输入单位错误，请输入 kg 或 pd")

示例1：
10kg
对应的英制重量为22.046磅 
示例2：
10pd 
对应的公制重量为4.535公斤 
  
  
  
  

