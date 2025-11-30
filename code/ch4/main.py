# main.py

def hello(name:str=None):
    if name is None:
        return "Hello World!"
    else:
        return f"Hello {name}!"

if __name__ == "__main__":
    print(hello("小白"))
