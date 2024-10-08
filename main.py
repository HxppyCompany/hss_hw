def hype(func):
    def wraper(*args, **kwargs):
        res = [ch for ch in str(func(*args, **kwargs)).lower()]
        for i in range(0, len(res), 2):
            res[i] = res[i].upper()
        return ''.join(res)
    return wraper


@hype
def cout(s: str):
    print(s)


if __name__ == "__main__":
    print(cout("Hello, Wxrld!"))
