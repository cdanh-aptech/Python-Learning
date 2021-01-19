
def main():
    getTong = lambda a, b: a + b

    print(getTong(10, 30))

    def helloName(name):
        return f"Hello {name}"

    print(helloName('Duy Anh'))

    getName = lambda name: f"I am {name}"

    print(getName('Duy Anh'))

if __name__ == "__main__":
    main()