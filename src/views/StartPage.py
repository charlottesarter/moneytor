import tkinter as tk

# Create the main window
window = tk.Tk()

# Define the frames for the buttons and the pages
buttons_frame = tk.Frame(window)
pages_frame = tk.Frame(window)

# Create the buttons
button1 = tk.Button(buttons_frame, text="Page 1", command=lambda: raise_frame(1))
button2 = tk.Button(buttons_frame, text="Page 2", command=lambda: raise_frame(2))
button3 = tk.Button(buttons_frame, text="Page 3", command=lambda: raise_frame(3))

# Place the buttons on the buttons frame
button1.pack()
button2.pack()
button3.pack()

# Create the frames for the pages
page1 = tk.Frame(pages_frame)
page2 = tk.Frame(pages_frame)
page3 = tk.Frame(pages_frame)

# Add widgets to the frames for the pages
label1 = tk.Label(page1, text="This is page 1")
label1.pack()

label2 = tk.Label(page2, text="This is page 2")
label2.pack()

label3 = tk.Label(page3, text="This is page 3")
label3.pack()

# Create a function to raise the desired frame
def raise_frame(frame_number):
    if frame_number == 1:
        page1.tkraise()
    elif frame_number == 2:
        page2.tkraise()
    elif frame_number == 3:
        page3.tkraise()

# Place the frames on the main window
buttons_frame.pack()
pages_frame.pack()

# Start with page 1 raised
raise_frame(1)

# Start the main event loop
window.mainloop()
