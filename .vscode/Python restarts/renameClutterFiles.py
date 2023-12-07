import os

def ren(format):
    l=1
    li=os.listdir("D:/junk folder")
    for i in li:
        if i.endswith(format):
            source=f"D:/junk folder/{i}"
            dest=f"D:/junk folder/{l}.{format}"
            os.rename(source,dest)
            l+=1

ren("bmp")


# st="ritik"
# if st.endswith("tik"):
#     print("true")