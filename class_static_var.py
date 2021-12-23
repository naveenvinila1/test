class csstudent:
    stream="cse"
    def __init__(self,name,no):
        self.name=name
        self.no=no
st=csstudent("sai",1)
st2=csstudent("baba",2)
print(st.stream)
print(st.name)
print(csstudent.stream)
st2.stream="mec"
print(st2.stream)