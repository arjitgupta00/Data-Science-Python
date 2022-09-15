# from tkinter import *
from tkinter import messagebox
import requests
import webbrowser
from functools import partial
from style_NewsAp import *
from WeatherApp import WeatherApp

def get_weather():
    start = WeatherApp.start_weather()
    return start

class NewsApp:
    def __init__(self, ap):
        self.app = ap
        self.app.title("News App by Arjit")
        self.app.geometry("1920x1080")

        self.NewsCatButton = []
        self.NewsCat = ['general', 'entertainment', 'business', 'sports', 'technology', 'health']

        self.title = Label(self.app, text="NewsApp", font=('rockwell bold', 30),
                           bg=blue, fg=fg_color,
                           relief=GROOVE, bd=12, pady=2)
        self.title.pack(fill=X)
        f1 = LabelFrame(self.app, text="Category", bg=blue, fg=fg_color,
                        font=('roboto slab', 20, 'bold'), relief=GROOVE, bd=10)
        f1.place(x=0, y=80, width=300, relheight=0.88)

        for i in range(len(self.NewsCat)):
            b = Button(f1, text=self.NewsCat[i].capitalize(), font=('roboto slab', 14, 'bold'),
                       bd=7, width=20, height=2, bg=light_blue, fg=fg_color)
            b.grid(row=i, column=0, padx=10, pady=5)
            b.bind('<Button-1>', self.newsarea)

        f2 = Frame(self.app, relief=GROOVE, bd=7)
        f2.place(x=310, y=80, relwidth=.69, relheight=.88)
        newstitle = Label(f2, text="News Area", bg=light_blue, fg=fg_color, bd=7,
                          relief=GROOVE, font=('roboto slab', 20, 'bold'))
        newstitle.pack(fill=X)
        scroll_y = Scrollbar(f2, orient=VERTICAL)
        self.textarea = Text(f2, yscrollcommand=scroll_y.set, font=('Lora bold', 15),
                             bg=blue, fg=fg_color)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.insert(END, "\n\t\n\t\n\t\n\t\n\t\n\t\n\t\n\t\n\t\n\t\
        Please select any category to show headlines\n\n\n\tPlease be patient, it depends on your internet connection")
        self.textarea.pack(fill=X)

        self.b2 = Button(f2, text='Check Weather'.upper(), font=('rockwell bold', 20),
                         bg=blue, fg='black', width=20, bd=7, command=get_weather)
        self.b2.place(x=0, y=545, relwidth=1, relheight=0.1)

    def newsarea(self, event):
        t_ype = 'general'
        print(t_ype)
        t_ype = event.widget.cget('text').lower()
        apikey = '01d29fec3c5148598c655ddc42cb0af6'
        news_url = f'https://newsapi.org/v2/top-headlines?country=in&category={t_ype}&apiKey={apikey}'
        self.textarea.delete("1.0", END)
        self.textarea.insert(END, '\nRead the Latest News provided by our NewsApp\n\n')
        self.textarea.insert(END, '-------------------------------------------------\n\n')
        try:
            articles = (requests.get(news_url).json())['articles']
            if articles != 0:
                for i in range(len(articles)):
                    self.textarea.insert(END, f"{articles[i]['title']}\n")
                    self.textarea.insert(END, f"{articles[i]['description']}\n")
                    self.textarea.insert(END, f"{articles[i]['content']}\n")
                    hyperlink = HyperlinkManager(self.textarea)
                    self.textarea.insert(END, "read more...", hyperlink.add(partial(webbrowser.open,
                                                                                    articles[i]['url'])))
                    self.textarea.insert(END, '\n-------------------------------------------------\n')
                    self.textarea.insert(END, '-------------------------------------------------\n\n')
            else:
                self.textarea.insert(END, "Sorry, no news available")

        except Exception as e:
            messagebox.showerror("ERROR, cannot connect to the internet or some issues with the NewsApp.")
            print(e)


app = Tk()
app.configure(bg=fg_color)
NewsApp(app)
app.state("zoomed")
pic = PhotoImage(file='icon\\newsappicon.png')
app.iconphoto(FALSE, pic)
app.mainloop()
