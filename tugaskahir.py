

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Ngoding\Tkinter-Designer-master\Jekprojek\10\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1233x879")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 879,
    width = 1233,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1233.0,
    883.0,
    fill="#FFFFFF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    242.0,
    111.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=83.0,
    y=96.0,
    width=318.0,
    height=29.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    617.254150390625,
    111.10128021240234,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=458.254150390625,
    y=95.60128021240234,
    width=318.0,
    height=29.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    242.0,
    163.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=83.0,
    y=148.0,
    width=318.0,
    height=29.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    617.254150390625,
    163.10128784179688,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=458.254150390625,
    y=147.60128784179688,
    width=318.0,
    height=29.0
)

canvas.create_text(
    82.745849609375,
    75.39871978759766,
    anchor="nw",
    text="Nama",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    458.0,
    75.0,
    anchor="nw",
    text="Nama",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    82.745849609375,
    127.31259155273438,
    anchor="nw",
    text="Club",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    458.0,
    126.91387176513672,
    anchor="nw",
    text="Club",
    fill="#000000",
    font=("Inter", 14 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    111.745849609375,
    273.62518310546875,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    487.0,
    273.2264709472656,
    image=image_image_2
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    177.0,
    273.88916015625,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=148.0,
    y=254.38916015625,
    width=58.0,
    height=37.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    552.254150390625,
    273.4904479980469,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=523.254150390625,
    y=253.99044799804688,
    width=58.0,
    height=37.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    177.0,
    273.88916015625,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=148.0,
    y=254.38916015625,
    width=58.0,
    height=37.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    552.254150390625,
    273.4904479980469,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=523.254150390625,
    y=253.99044799804688,
    width=58.0,
    height=37.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    177.0,
    224.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    552.254150390625,
    223.60128784179688,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    242.0,
    224.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    617.254150390625,
    223.60128784179688,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    307.0,
    224.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    682.254150390625,
    223.60128784179688,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    372.0,
    224.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    747.254150390625,
    223.60128784179688,
    image=image_image_10
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    177.0,
    323.5,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=148.0,
    y=304.0,
    width=58.0,
    height=37.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    552.254150390625,
    323.1012878417969,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=523.254150390625,
    y=303.6012878417969,
    width=58.0,
    height=37.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    177.0,
    373.11083984375,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(
    x=148.0,
    y=353.61083984375,
    width=58.0,
    height=37.0
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    552.254150390625,
    372.7121276855469,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_12.place(
    x=523.254150390625,
    y=353.2121276855469,
    width=58.0,
    height=37.0
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    177.0,
    422.7216796875,
    image=entry_image_13
)
entry_13 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_13.place(
    x=148.0,
    y=403.2216796875,
    width=58.0,
    height=37.0
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    552.254150390625,
    422.3229675292969,
    image=entry_image_14
)
entry_14 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_14.place(
    x=523.254150390625,
    y=402.8229675292969,
    width=58.0,
    height=37.0
)

entry_image_15 = PhotoImage(
    file=relative_to_assets("entry_15.png"))
entry_bg_15 = canvas.create_image(
    177.0,
    472.33251953125,
    image=entry_image_15
)
entry_15 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_15.place(
    x=148.0,
    y=452.83251953125,
    width=58.0,
    height=37.0
)

entry_image_16 = PhotoImage(
    file=relative_to_assets("entry_16.png"))
entry_bg_16 = canvas.create_image(
    552.254150390625,
    471.9338073730469,
    image=entry_image_16
)
entry_16 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_16.place(
    x=523.254150390625,
    y=452.4338073730469,
    width=58.0,
    height=37.0
)

entry_image_17 = PhotoImage(
    file=relative_to_assets("entry_17.png"))
entry_bg_17 = canvas.create_image(
    242.0,
    274.5,
    image=entry_image_17
)
entry_17 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_17.place(
    x=213.0,
    y=255.0,
    width=58.0,
    height=37.0
)

entry_image_18 = PhotoImage(
    file=relative_to_assets("entry_18.png"))
entry_bg_18 = canvas.create_image(
    617.254150390625,
    274.1012878417969,
    image=entry_image_18
)
entry_18 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_18.place(
    x=588.254150390625,
    y=254.60128784179688,
    width=58.0,
    height=37.0
)

entry_image_19 = PhotoImage(
    file=relative_to_assets("entry_19.png"))
entry_bg_19 = canvas.create_image(
    242.0,
    274.5,
    image=entry_image_19
)
entry_19 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_19.place(
    x=213.0,
    y=255.0,
    width=58.0,
    height=37.0
)

entry_image_20 = PhotoImage(
    file=relative_to_assets("entry_20.png"))
entry_bg_20 = canvas.create_image(
    617.254150390625,
    274.1012878417969,
    image=entry_image_20
)
entry_20 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_20.place(
    x=588.254150390625,
    y=254.60128784179688,
    width=58.0,
    height=37.0
)

entry_image_21 = PhotoImage(
    file=relative_to_assets("entry_21.png"))
entry_bg_21 = canvas.create_image(
    242.0,
    324.11083984375,
    image=entry_image_21
)
entry_21 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_21.place(
    x=213.0,
    y=304.61083984375,
    width=58.0,
    height=37.0
)

entry_image_22 = PhotoImage(
    file=relative_to_assets("entry_22.png"))
entry_bg_22 = canvas.create_image(
    617.254150390625,
    323.7121276855469,
    image=entry_image_22
)
entry_22 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_22.place(
    x=588.254150390625,
    y=304.2121276855469,
    width=58.0,
    height=37.0
)

entry_image_23 = PhotoImage(
    file=relative_to_assets("entry_23.png"))
entry_bg_23 = canvas.create_image(
    242.0,
    373.7216796875,
    image=entry_image_23
)
entry_23 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_23.place(
    x=213.0,
    y=354.2216796875,
    width=58.0,
    height=37.0
)

entry_image_24 = PhotoImage(
    file=relative_to_assets("entry_24.png"))
entry_bg_24 = canvas.create_image(
    617.254150390625,
    373.3229675292969,
    image=entry_image_24
)
entry_24 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_24.place(
    x=588.254150390625,
    y=353.8229675292969,
    width=58.0,
    height=37.0
)

entry_image_25 = PhotoImage(
    file=relative_to_assets("entry_25.png"))
entry_bg_25 = canvas.create_image(
    242.0,
    423.33251953125,
    image=entry_image_25
)
entry_25 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_25.place(
    x=213.0,
    y=403.83251953125,
    width=58.0,
    height=37.0
)

entry_image_26 = PhotoImage(
    file=relative_to_assets("entry_26.png"))
entry_bg_26 = canvas.create_image(
    617.254150390625,
    422.9338073730469,
    image=entry_image_26
)
entry_26 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_26.place(
    x=588.254150390625,
    y=403.4338073730469,
    width=58.0,
    height=37.0
)

entry_image_27 = PhotoImage(
    file=relative_to_assets("entry_27.png"))
entry_bg_27 = canvas.create_image(
    242.0,
    472.943359375,
    image=entry_image_27
)
entry_27 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_27.place(
    x=213.0,
    y=453.443359375,
    width=58.0,
    height=37.0
)

entry_image_28 = PhotoImage(
    file=relative_to_assets("entry_28.png"))
entry_bg_28 = canvas.create_image(
    617.254150390625,
    472.5446472167969,
    image=entry_image_28
)
entry_28 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_28.place(
    x=588.254150390625,
    y=453.0446472167969,
    width=58.0,
    height=37.0
)

entry_image_29 = PhotoImage(
    file=relative_to_assets("entry_29.png"))
entry_bg_29 = canvas.create_image(
    307.0,
    274.5,
    image=entry_image_29
)
entry_29 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_29.place(
    x=278.0,
    y=255.0,
    width=58.0,
    height=37.0
)

entry_image_30 = PhotoImage(
    file=relative_to_assets("entry_30.png"))
entry_bg_30 = canvas.create_image(
    682.254150390625,
    274.1012878417969,
    image=entry_image_30
)
entry_30 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_30.place(
    x=653.254150390625,
    y=254.60128784179688,
    width=58.0,
    height=37.0
)

entry_image_31 = PhotoImage(
    file=relative_to_assets("entry_31.png"))
entry_bg_31 = canvas.create_image(
    307.0,
    274.5,
    image=entry_image_31
)
entry_31 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_31.place(
    x=278.0,
    y=255.0,
    width=58.0,
    height=37.0
)

entry_image_32 = PhotoImage(
    file=relative_to_assets("entry_32.png"))
entry_bg_32 = canvas.create_image(
    682.254150390625,
    274.1012878417969,
    image=entry_image_32
)
entry_32 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_32.place(
    x=653.254150390625,
    y=254.60128784179688,
    width=58.0,
    height=37.0
)

entry_image_33 = PhotoImage(
    file=relative_to_assets("entry_33.png"))
entry_bg_33 = canvas.create_image(
    307.0,
    324.11083984375,
    image=entry_image_33
)
entry_33 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_33.place(
    x=278.0,
    y=304.61083984375,
    width=58.0,
    height=37.0
)

entry_image_34 = PhotoImage(
    file=relative_to_assets("entry_34.png"))
entry_bg_34 = canvas.create_image(
    682.254150390625,
    323.7121276855469,
    image=entry_image_34
)
entry_34 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_34.place(
    x=653.254150390625,
    y=304.2121276855469,
    width=58.0,
    height=37.0
)

entry_image_35 = PhotoImage(
    file=relative_to_assets("entry_35.png"))
entry_bg_35 = canvas.create_image(
    307.0,
    373.7216796875,
    image=entry_image_35
)
entry_35 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_35.place(
    x=278.0,
    y=354.2216796875,
    width=58.0,
    height=37.0
)

entry_image_36 = PhotoImage(
    file=relative_to_assets("entry_36.png"))
entry_bg_36 = canvas.create_image(
    682.254150390625,
    373.3229675292969,
    image=entry_image_36
)
entry_36 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_36.place(
    x=653.254150390625,
    y=353.8229675292969,
    width=58.0,
    height=37.0
)

entry_image_37 = PhotoImage(
    file=relative_to_assets("entry_37.png"))
entry_bg_37 = canvas.create_image(
    307.0,
    423.33251953125,
    image=entry_image_37
)
entry_37 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_37.place(
    x=278.0,
    y=403.83251953125,
    width=58.0,
    height=37.0
)

entry_image_38 = PhotoImage(
    file=relative_to_assets("entry_38.png"))
entry_bg_38 = canvas.create_image(
    682.254150390625,
    422.9338073730469,
    image=entry_image_38
)
entry_38 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_38.place(
    x=653.254150390625,
    y=403.4338073730469,
    width=58.0,
    height=37.0
)

entry_image_39 = PhotoImage(
    file=relative_to_assets("entry_39.png"))
entry_bg_39 = canvas.create_image(
    307.0,
    472.943359375,
    image=entry_image_39
)
entry_39 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_39.place(
    x=278.0,
    y=453.443359375,
    width=58.0,
    height=37.0
)

entry_image_40 = PhotoImage(
    file=relative_to_assets("entry_40.png"))
entry_bg_40 = canvas.create_image(
    682.254150390625,
    472.5446472167969,
    image=entry_image_40
)
entry_40 = Entry(
    bd=0,
    bg="#B4B4B4",
    fg="#000716",
    highlightthickness=0
)
entry_40.place(
    x=653.254150390625,
    y=453.0446472167969,
    width=58.0,
    height=37.0
)

entry_image_41 = PhotoImage(
    file=relative_to_assets("entry_41.png"))
entry_bg_41 = canvas.create_image(
    372.0,
    274.5,
    image=entry_image_41
)
entry_41 = Entry(
    bd=0,
    bg="#7CFF7C",
    fg="#000716",
    highlightthickness=0
)
entry_41.place(
    x=343.0,
    y=255.0,
    width=58.0,
    height=37.0
)

entry_image_42 = PhotoImage(
    file=relative_to_assets("entry_42.png"))
entry_bg_42 = canvas.create_image(
    747.254150390625,
    274.1012878417969,
    image=entry_image_42
)
entry_42 = Entry(
    bd=0,
    bg="#7CFF7C",
    fg="#000716",
    highlightthickness=0
)
entry_42.place(
    x=718.254150390625,
    y=254.60128784179688,
    width=58.0,
    height=37.0
)

entry_image_43 = PhotoImage(
    file=relative_to_assets("entry_43.png"))
entry_bg_43 = canvas.create_image(
    372.0,
    274.5,
    image=entry_image_43
)
entry_43 = Entry(
    bd=0,
    bg="#7CFF7C",
    fg="#000716",
    highlightthickness=0
)
entry_43.place(
    x=343.0,
    y=255.0,
    width=58.0,
    height=37.0
)

entry_image_44 = PhotoImage(
    file=relative_to_assets("entry_44.png"))
entry_bg_44 = canvas.create_image(
    747.254150390625,
    274.1012878417969,
    image=entry_image_44
)
entry_44 = Entry(
    bd=0,
    bg="#7CFF7C",
    fg="#000716",
    highlightthickness=0
)
entry_44.place(
    x=718.254150390625,
    y=254.60128784179688,
    width=58.0,
    height=37.0
)

entry_image_45 = PhotoImage(
    file=relative_to_assets("entry_45.png"))
entry_bg_45 = canvas.create_image(
    372.0,
    324.11083984375,
    image=entry_image_45
)
entry_45 = Entry(
    bd=0,
    bg="#7CFF7C",
    fg="#000716",
    highlightthickness=0
)
entry_45.place(
    x=343.0,
    y=304.61083984375,
    width=58.0,
    height=37.0
)

entry_image_46 = PhotoImage(
    file=relative_to_assets("entry_46.png"))
entry_bg_46 = canvas.create_image(
    747.254150390625,
    323.7121276855469,
    image=entry_image_46
)
entry_46 = Entry(
    bd=0,
    bg="#7CFF7C",
    fg="#000716",
    highlightthickness=0
)
entry_46.place(
    x=718.254150390625,
    y=304.2121276855469,
    width=58.0,
    height=37.0
)

entry_image_47 = PhotoImage(
    file=relative_to_assets("entry_47.png"))
entry_bg_47 = canvas.create_image(
    372.0,
    373.7216796875,
    image=entry_image_47
)
entry_47 = Entry(
    bd=0,
    bg="#7CFF7C",
    fg="#000716",
    highlightthickness=0
)
entry_47.place(
    x=343.0,
    y=354.2216796875,
    width=58.0,
    height=37.0
)

entry_image_48 = PhotoImage(
    file=relative_to_assets("entry_48.png"))
entry_bg_48 = canvas.create_image(
    747.254150390625,
    373.3229675292969,
    image=entry_image_48
)
entry_48 = Entry(
    bd=0,
    bg="#7CFF7C",
    fg="#000716",
    highlightthickness=0
)
entry_48.place(
    x=718.254150390625,
    y=353.8229675292969,
    width=58.0,
    height=37.0
)

entry_image_49 = PhotoImage(
    file=relative_to_assets("entry_49.png"))
entry_bg_49 = canvas.create_image(
    372.0,
    423.33251953125,
    image=entry_image_49
)
entry_49 = Entry(
    bd=0,
    bg="#7CFF7C",
    fg="#000716",
    highlightthickness=0
)
entry_49.place(
    x=343.0,
    y=403.83251953125,
    width=58.0,
    height=37.0
)

entry_image_50 = PhotoImage(
    file=relative_to_assets("entry_50.png"))
entry_bg_50 = canvas.create_image(
    747.254150390625,
    422.9338073730469,
    image=entry_image_50
)
entry_50 = Entry(
    bd=0,
    bg="#7CFF7C",
    fg="#000716",
    highlightthickness=0
)
entry_50.place(
    x=718.254150390625,
    y=403.4338073730469,
    width=58.0,
    height=37.0
)

entry_image_51 = PhotoImage(
    file=relative_to_assets("entry_51.png"))
entry_bg_51 = canvas.create_image(
    372.0,
    472.943359375,
    image=entry_image_51
)
entry_51 = Entry(
    bd=0,
    bg="#7CFF7C",
    fg="#000716",
    highlightthickness=0
)
entry_51.place(
    x=343.0,
    y=453.443359375,
    width=58.0,
    height=37.0
)

entry_image_52 = PhotoImage(
    file=relative_to_assets("entry_52.png"))
entry_bg_52 = canvas.create_image(
    747.254150390625,
    472.5446472167969,
    image=entry_image_52
)
entry_52 = Entry(
    bd=0,
    bg="#7CFF7C",
    fg="#000716",
    highlightthickness=0
)
entry_52.place(
    x=718.254150390625,
    y=453.0446472167969,
    width=58.0,
    height=37.0
)

entry_image_53 = PhotoImage(
    file=relative_to_assets("entry_53.png"))
entry_bg_53 = canvas.create_image(
    371.45934677124023,
    519.7767124176025,
    image=entry_image_53
)
entry_53 = Entry(
    bd=0,
    bg="#5D5D5D",
    fg="#000716",
    highlightthickness=0
)
entry_53.place(
    x=342.23779296875,
    y=500.0,
    width=58.44310760498047,
    height=37.55342483520508
)

entry_image_54 = PhotoImage(
    file=relative_to_assets("entry_54.png"))
entry_bg_54 = canvas.create_image(
    746.7134971618652,
    519.3780002593994,
    image=entry_image_54
)
entry_54 = Entry(
    bd=0,
    bg="#5D5D5D",
    fg="#000716",
    highlightthickness=0
)
entry_54.place(
    x=717.491943359375,
    y=499.6012878417969,
    width=58.44310760498047,
    height=37.55342483520508
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    111.745849609375,
    323.0669860839844,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    487.0,
    322.66827392578125,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    111.745849609375,
    372.5087585449219,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    487.0,
    372.11004638671875,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    111.745849609375,
    421.9505615234375,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    487.0,
    421.5518493652344,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    111.745849609375,
    471.3923645019531,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    487.0,
    470.99365234375,
    image=image_image_18
)

canvas.create_text(
    288.0,
    513.0,
    anchor="nw",
    text="Total",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    663.254150390625,
    512.6012573242188,
    anchor="nw",
    text="Total",
    fill="#000000",
    font=("Inter", 14 * -1)
)

image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    616.0,
    32.0,
    image=image_image_19
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click(X),
    relief="flat"
)
button_1.place(
    x=309.0126953125,
    y=713.19775390625,
    width=91.98705291748047,
    height=60.566192626953125
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=684.266845703125,
    y=712.7990112304688,
    width=91.98705291748047,
    height=60.566192626953125
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=82.745849609375,
    y=569.816650390625,
    width=91.98705291748047,
    height=60.566192626953125
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=458.0,
    y=569.4179077148438,
    width=91.98705291748047,
    height=60.566192626953125
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=195.87939453125,
    y=569.816650390625,
    width=91.98705291748047,
    height=60.566192626953125
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=571.133544921875,
    y=569.4179077148438,
    width=91.98705291748047,
    height=60.566192626953125
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=309.0126953125,
    y=569.816650390625,
    width=91.98705291748047,
    height=60.566192626953125
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=684.266845703125,
    y=569.4179077148438,
    width=91.98705291748047,
    height=60.566192626953125
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=82.745849609375,
    y=641.5071411132812,
    width=91.98705291748047,
    height=60.566192626953125
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=458.0,
    y=641.1083984375,
    width=91.98705291748047,
    height=60.566192626953125
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=195.87939453125,
    y=640.2711791992188,
    width=91.98705291748047,
    height=61.80223846435547
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=571.133544921875,
    y=639.8724365234375,
    width=91.98705291748047,
    height=61.80223846435547
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_13 clicked"),
    relief="flat"
)
button_13.place(
    x=307.95556640625,
    y=641.5071411132812,
    width=93.04436492919922,
    height=60.56622314453125
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_14 clicked"),
    relief="flat"
)
button_14.place(
    x=683.209716796875,
    y=641.1083984375,
    width=93.04436492919922,
    height=60.56622314453125
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_15 clicked"),
    relief="flat"
)
button_15.place(
    x=82.745849609375,
    y=713.19775390625,
    width=91.98705291748047,
    height=60.566192626953125
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_16 clicked"),
    relief="flat"
)
button_16.place(
    x=458.0,
    y=712.7990112304688,
    width=91.98705291748047,
    height=60.566192626953125
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_17 clicked"),
    relief="flat"
)
button_17.place(
    x=195.87939453125,
    y=713.19775390625,
    width=91.98705291748047,
    height=61.80223846435547
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_18 clicked"),
    relief="flat"
)
button_18.place(
    x=571.133544921875,
    y=712.7990112304688,
    width=91.98705291748047,
    height=61.80223846435547
)

image_image_20 = PhotoImage(
    file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(
    1022.743896484375,
    400.46730041503906,
    image=image_image_20
)
window.resizable(False, False)
window.mainloop()
