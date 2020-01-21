
def main():

    try:

        individualsName = input("Hello, what is your name?\n")

        fullGreeting = "Hello, " + individualsName + "!"

        print(fullGreeting)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()