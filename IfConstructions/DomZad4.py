number = float(input())
input_metric = str(input())
output_metric = str(input())

if input_metric == "mm" and output_metric == "cm":
    print(f"{number/10:.3f}")
elif input_metric == "mm" and output_metric == "m" :
    print(f"{number / 1000:.3f}")
elif input_metric == "cm" and output_metric == "mm":
    print(f"{number * 10:.3f}")
elif input_metric == "cm" and output_metric == "m":
    print(f"{number / 100:.3f}")
elif input_metric == "m" and output_metric == "mm":
    print(f"{number * 1000:.3f}")
elif input_metric == "m" and output_metric == "cm" :
    print(f"{number * 100:.3f}")

