import tkinter as tk

HEIGHT = 500
WIDTH = 600



# TODO:
# Accept non 4 digit years
# Error handling for entry
# Label scrollbar
# text formatting on output
# Clean up GUI
# Add more functions



def get_info(user_date):
    print("This is date: ", user_date)

    import requests
    user_date = user_date.replace(" ", "_")
    website_url = requests.get('https://en.wikipedia.org/wiki/Wikipedia:Selected_anniversaries/' + user_date).text

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(website_url, 'lxml')

    output = ""
    for tag in soup.find_all("li"):
        if tag.text[:4].isdigit():
            output += "\n" + tag.text

    print(output)
    # label
    out_label = tk.Label(lower_frame, text=output, wraplength=400, justify=tk.LEFT)
    out_label.place(relwidth=1, relheight=1)


# Create GUI elements
root = tk.Tk()
root.title("Wikidate")

# canvas
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# frame
frame = tk.Frame(root, bg='#0033cc', bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# entry
entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

# button
button = tk.Button(frame, text="Get info!", command=lambda: get_info(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)


# lower frame
lower_frame = tk.Frame(root, bg='#0033cc', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# label
out_label = tk.Label(lower_frame)
out_label.place(relwidth=1, relheight=1)

root.mainloop()
