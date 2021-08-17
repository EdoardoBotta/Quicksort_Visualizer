import tkinter as t
from random import sample, choice

#"Run with median" to be implemented (The median of the list is always chosen as pivot)

class MainWindow:
    def __init__(self):
        self.window = t.Tk()
        self.window.title('Quicksort algorithm')
        self.window.geometry('350x200')

        self.l = []
        self.c = 0

        self.lbl = t.Label(self.window, text = 'Insert numbers:')
        self.lbl.grid(column = 0, row = 0)

        self.canvas = t.Canvas(self.window, width = 2000, height = 550, bg = 'black')
        self.canvas.grid(columnspan = 2000, rowspan = 550)

        self.line = self.canvas.create_line(0, 530, 2000, 530, fill = 'black')

        self.start = t.Button(self.window, text = 'Run Algorithm', command = self.run)
        self.start.grid(column = 5, row = 0)

        self.enter = t.Entry(self.window, width = 10)
        self.enter.grid(column = 1, row = 0, padx = 10, pady = 10)

        self.btn = t.Button(self.window, text = 'ADD', bg = 'yellow', fg = 'blue', command = self.addnumbers)
        self.btn.grid(column = 2, row = 0)

        self.gen = t.Button(self.window, text = 'Generate list', command = self.generator)
        self.gen.grid(column = 3, row = 0)

        self.wc = t.Button(self.window, text = 'Worst case', command = lambda : self.generator(True))
        self.wc.grid(column = 4, row = 0)

        self.randomizer = t.Button(self.window, text = 'Run Randomized', command = lambda: self.run(True))
        self.randomizer.grid(column = 6, row = 0)

        self.clear = t.Button(self.window, text = 'Clear', command = self.clear_all)
        self.clear.grid(column = 7, row = 0)

        self.counter = t.Label(self.window, text = f'{self.c}')
        self.counter.grid(column = 8, row = 0)

    def addnumbers(self):
        number = self.enter.get()
        if not number.isdecimal():
            self.enter.delete(0, t.END)
            return
        number = int(number)
        c = Number(number, len(self.l), self)
        self.l.append(c)
        self.enter.delete(0, t.END)

    def generator(self, worst_case = False):
        if worst_case:
            for i in range(256, 0, -1):
                self.l.append(Number(i, len(self.l), self))
        else:
            for i in sample(range(265),256-len(self.l)):
                self.l.append(Number(i, len(self.l), self))

    def clear_all(self):
        self.c = 0
        self.counter.config(text=f'{self.c}')
        for i in self.l:
            self.canvas.delete(i.rectangle)
            self.canvas.delete(i.text)
        self.l.clear()

    def color_all(self, color):
        for i in self.l:
            i.color(color)

    def update_counter(self):
        self.c += 1
        self.counter.config(text=f'{self.c}')

    def run(self, randomized = False):
        quicksort(self.l, 0, len(self.l)-1, randomized)
        self.window.after(250, lambda: self.color_all('red'))

class Number:
    def __init__(self, number, pos, window):
        self.rectangle = window.canvas.create_rectangle(pos*5, 530 - 2*number, 5*(pos+1), 530, fill = 'red')
        self.text = window.canvas.create_text((5*(pos + 1), 540), text = f'{number}', font =('Purisa', 2))
        self.number = number
        self.pos = pos + 1
        self.win = window

    def swap(self, other):
        xd = self.pos - other.pos
        if xd == 0:
            return

        self.win.canvas.move(self.rectangle, -xd*5, 0)
        self.win.canvas.move(other.rectangle, xd*5, 0)

        self.win.canvas.move(self.text, -xd*5, 0)
        self.win.canvas.move(other.text, xd*5, 0)

        self.pos -= xd
        other.pos += xd

        self.win.window.update()

    def color(self, color):
        self.win.canvas.itemconfig(self.rectangle, fill = color)

    def __repr__(self):
        return f'#{self.number}'

    def __le__(self, other):
        if not isinstance(other, Number):
            raise Exception('other must be a Number')
        return self.number <= other.number



def choose_pivot(l, p, r, randomized = False):
    if randomized:
        x = choice(l[p:r+1])
        c = l.index(x)
        l[r], l[c] = l[c], l[r]
        l[r].color('yellow')
        l[r].swap(l[c])
    else:
        x = l[r]
        l[r].color('yellow')
    return x

# Start Algorithm
def quicksort(l, p, r, randomized = False):
    if p < r:
        q = partition(l, p, r, randomized)
        quicksort(l, p, q-1, randomized)
        quicksort(l, q, r, randomized)
    return l

def partition(l, p, r, randomized = False): # r == len(l) - 1
    x = choose_pivot(l, p, r, randomized)
    i = p - 1

    for j in range(p, r):
        w.update_counter()
        if l[j] <= x:
            i += 1
            l[i].swap(l[j])
            l[i], l[j] = l[j], l[i]
    l[i+1].swap(l[r])
    l[i+1], l[r] = l[r], l[i+1]
    return i + 1
# End Algorithm


if __name__ == "__main__":
    w = MainWindow()
    w.window.mainloop()







# Here is the algorithm:
# def quicksort(l, p, r):
#     if p < r:
#         q = partition(l, p, r)
#         quicksort(l, p, q-1)
#         quicksort(l, q, r)
#     return l

# def partition(l, p, r): # r == len(l) - 1
#     x = l[r]
#     i = p - 1
#     for j in range(p, r):
#         if l[j] <= x:
#             i += 1
#             l[i], l[j] = l[j], l[i]
#     l[i+1], l[r] = l[r], l[i+1]
#     return i + 1
