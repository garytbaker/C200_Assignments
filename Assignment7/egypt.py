import webbrowser

def egypt(x):
    Input_Name = str(x)
    Name = Input_Name.lower()
    New_Name =""
    for i in range(len(Name)):
        if Name[i] != "e" and Name[i] != "f":
            New_Name += Name[i]
    s="\"\"\" <html> <head></head> \n <body> \n <h2 class=\"text-center\">" + Input_Name +"="+ New_Name +"</h2> \n <img src=\"eglyphTOP.jpg\"><br> \n"
    symbols = {"a":"eglypha.jpg", "b":"eglyphb.jpg", "c":"eglyphc.jpg",
               "d":"eglyphd.jpg", "g":"eglyphg.jpg", "h":"eglyphh.jpg",
               "i":"eglyphi.jpg", "j":"eglyphj.jpg", "k":"eglyphk.jpg",
               "l":"eglyphl.jpg", "m":"eglyphm.jpg", "n":"eglyphn.jpg",
               "o":"eglypho.jpg", "p":"eglyphp.jpg", "q":"eglyphq.jpg",
               "r":"eglyphr.jpg", "s":"eglyphs.jpg", "t":"eglypht.jpg",
               "u":"eglyphu.jpg", "v":"eglyphv.jpg", "w":"eglyphw.jpg",
               "x":"eglyphx.jpg", "y":"eglyphy.jpg", "z":"eglyphz.jpg"}
    for i in range(len(Name)):
        if Name[i] != "e" and Name[i] != "f":
            x = "<img src=" +symbols[Name[i]] +"><br> \n"
            s += x
    s+= "<img src=\"eglyphBOTTOM.jpg\"><br> \n </body></html>\"\"\"" 
    return s


plocation = input("Enter location: ")
f = open(plocation + ".html", "w")
name = input("Name: ")
f.write(egypt(name))
f.close()
webbrowser.open_new_tab(plocation + ".html")