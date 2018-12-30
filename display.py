import Tkinter as tk
import time
import requests

def Draw(w, h):
    global text_power_total
    global text_power_p1
    global text_power_p2
    global text_power_p3
    global text_variable1
    global text_variable2
    global text_variable3

    b = 3

    frame1=tk.Frame(root,relief='solid',bd=1)
    frame1.place(x=b,y=b,width=w-b*2,height=h-b*2)
    tk.Label(frame1, text='smart4pi').pack()

    frame2 = tk.Frame(frame1,width=w,height=h,relief='solid',bd=1)
    frame2.place(y=15, x=1, width=w-b*2-b*2, height=h-b*2-b*2-13)

    text_power_total=tk.Label(frame2,text='HELLO')
    text_power_total.pack(anchor="w")
    text_power_p1=tk.Label(frame2,text='HELLO')
    text_power_p1.pack(anchor="w")
    text_power_p2=tk.Label(frame2,text='HELLO')
    text_power_p2.pack(anchor="w")
    text_power_p3=tk.Label(frame2,text='HELLO')
    text_power_p3.pack(anchor="w")

    text_variable1=tk.Label(frame2,text='HELLO')
    text_variable1.pack(anchor="w")
    text_variable2=tk.Label(frame2,text='HELLO')
    text_variable2.pack(anchor="w")
    text_variable3=tk.Label(frame2,text='HELLO')
    text_variable3.pack(anchor="w")

def GetValueFromREST(type, phaseno):
    resp = requests.get("http://localhost:1080/api/all/%s/now" % type)
    if resp.status_code != 200:
        return (0.0, "")
    if "datasets" in resp.json():
        for dataset in resp.json()["datasets"]:
            if "phases" in dataset:
                for phase in dataset["phases"]:
                    if not "phase" in phase:
                        continue
                    if not "values" in phase:
                        continue
                    if len(phase["values"]) == 0:
                        continue
                    if int(phase["phase"]) == phaseno:
                        return (float(phase["values"][0]["data"]), phase["values"][0]["unity"])
    return (0.0, "")

def RefresherPower():
    global text_power_total
    global text_power_p1
    global text_power_p2
    global text_power_p3

    try:
        power = 0.0
        p, u = GetValueFromREST("power", 1)
        text_power_p1.configure(text="P1    %.3f %s" % (p, u) )
        power += p

        p, u = GetValueFromREST("power", 2)
        text_power_p2.configure(text="P2    %.3f %s" % (p, u) )
        power += p

        p, u = GetValueFromREST("power", 3)
        text_power_p3.configure(text="P3    %.3f %s" % (p, u) )
        power += p

        text_power_total.configure(text="Total %.3f W" % power)
    except:
        pass
    root.after(1000, RefresherPower) # every second...

def RefresherVoltageP1():
    global text_variable1

    try:
        p, u = GetValueFromREST("voltage", 1)
        text_variable1.configure(text="P1    %.3f %s" % (p, u) )

    except:
        pass
    root.after(1000, RefresherVoltageP2) # every second...

def RefresherVoltageP2():
    global text_variable1

    try:
        p, u = GetValueFromREST("voltage", 2)
        text_variable1.configure(text="P2    %.3f %s" % (p, u) )

    except:
        pass
    root.after(1000, RefresherVoltageP3) # every second...

def RefresherVoltageP3():
    global text_variable1

    try:
        p, u = GetValueFromREST("voltage", 3)
        text_variable1.configure(text="P3    %.3f %s" % (p, u) )

    except:
        pass
    root.after(1000, RefresherVoltageP1) # every second...


def RefresherFrequencyP1():
    global text_variable2

    try:
        p, u = GetValueFromREST("frequency", 1)
        text_variable2.configure(text="P1    %.3f %s" % (p, u) )

    except:
        pass
    root.after(1000, RefresherFrequencyP2) # every second...

def RefresherFrequencyP2():
    global text_variable2

    try:
        p, u = GetValueFromREST("frequency", 2)
        text_variable2.configure(text="P2    %.3f %s" % (p, u) )

    except:
        pass
    root.after(1000, RefresherFrequencyP3) # every second...

def RefresherFrequencyP3():
    global text_variable2

    try:
        p, u = GetValueFromREST("frequency", 3)
        text_variable2.configure(text="P3    %.3f %s" % (p, u) )

    except:
        pass
    root.after(1000, RefresherCosPiP1) # every second...

def RefresherCosPiP1():
    global text_variable2

    try:
        p, u = GetValueFromREST("cosphi", 1)
        text_variable2.configure(text="P1    %.3f %s phi" % (p, u) )

    except:
        pass
    root.after(1000, RefresherCosPiP2) # every second...

def RefresherCosPiP2():
    global text_variable2

    try:
        p, u = GetValueFromREST("cosphi", 2)
        text_variable2.configure(text="P2    %.3f %s phi" % (p, u) )

    except:
        pass
    root.after(1000, RefresherCosPiP3) # every second...

def RefresherCosPiP3():
    global text_variable2

    try:
        p, u = GetValueFromREST("cosphi", 3)
        text_variable2.configure(text="P3    %.3f %s phi" % (p, u) )

    except:
        pass
    root.after(1000, RefresherFrequencyP1) # every second...

root=tk.Tk()
root.attributes("-fullscreen", True)
Draw(160, 128)
RefresherPower()
RefresherVoltageP1()
RefresherFrequencyP1()
root.mainloop()
