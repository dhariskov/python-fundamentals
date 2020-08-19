test = {
    "test1":["1", "2", "3"],
    "test2":["4", "5", "6"]
}

for each in test.values():
    if "1" in each:
        print("OK")
    else:
        print("ne ok")