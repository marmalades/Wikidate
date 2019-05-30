import tkinter as tk

HEIGHT = 500
WIDTH = 600


def info_label(entry):
    print("This is date: ", entry)
    import requests

    user_date = entry

    user_date = user_date.replace(" ", "_")
    website_url = requests.get('https://en.wikipedia.org/wiki/Wikipedia:Selected_anniversaries/' + user_date).text

    # TODO: find actual list items in Wikipedia
    # currently feels like a workaround by getting list items that start with 4 digits
    # probably improves speed too?

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(website_url, 'lxml')

    for tag in soup.find_all("li"):
        info = "{0}".format(tag.text)
        # -----> have includes "title="###digits###" to find all elements

        # TODO: add functionality for different years aka weird/early years
        if info[:4].isdigit():
            events = info
            print("\n" + events)


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
button = tk.Button(frame, text="Get info!", command=lambda: info_label(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

# lower frame
lowerFrame = tk.Frame(root, bg='#0033cc', bd=10)
lowerFrame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# label
label = tk.Label(lowerFrame)
label.place(relwidth=1, relheight=1)

root.mainloop()