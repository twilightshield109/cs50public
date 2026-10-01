def convert(msg):
    msg = msg.replace(":)", "🙂")
    msg = msg.replace(":(", "🙁")
    return msg

def main():
    msg = input("Send a message below:")
    print(convert(msg))

main()
