data = input().strip()      # 例如 "10kg" 或 "10pd"
weight = float(data[:-2])   # 数字部分
unit = data[-2:]            # 单位部分

if unit == "kg":
    pounds = weight * 2.2046
    print(f"对应的英制重量为{pounds:.3f}pd")
elif unit == "pd":
    kilograms = weight / 2.2046
    print(f"对应的公制重量为{kilograms:.3f}kg")
else:
    print("输入单位错误，请输入 kg 或 pd")


  
  
  

