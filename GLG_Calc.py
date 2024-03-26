while True:
    x = input("What is the original rate?")
    try:
            y = (float(x)*1.177)
            print("With our rate included: $",y)
            print("Their cut: $", round(y,1)*.85)
            print("Our cut: $", round(y,1)*.15)
            print(760*.85)
            break
    except ValueError:
        pass
## Needs work above