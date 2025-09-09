data = input().strip()      # 读取输入，比如 "10kg" 或 "10pd"
weight = float(data[:-2])   # 数字部分
unit = data[-2:]            # 单位部分

def truncate(num, n):
    """截断保留 n 位小数"""
    return int(num * (10**n)) / (10**n)

if unit == "kg":
    pounds = truncate(weight * 2.2046, 3)
    print(f"对应的英制重量为{pounds:.3f}磅")
elif unit == "pd":
    kilograms = truncate(weight / 2.2046, 3)
    print(f"对应的公制重量为{kilograms:.3f}公斤")
else:
    print("输入单位错误，请输入 kg 或 pd")


  
  
  

