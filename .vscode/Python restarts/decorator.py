def greet(fx):
    def mfx():
        print("this is decorator")
        fx()
    return mfx

@greet  
def hell():
    print("this is hell function" )
    # pass

hell()
# greet()