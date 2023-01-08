import tkinter as tk

WIDTH = 500
HEIGHT = 500

window = tk.Tk()
canvas = tk.Canvas(width = WIDTH, height = HEIGHT, bg = "linen")
canvas.pack()

x = WIDTH // 2
y = HEIGHT // 2
x0 = x
y0 = y

step = 1
stepSize = 20
stepOrder = 1
state = 0
turnCounter = 0
numberCounter = (WIDTH // stepSize - 1) * (HEIGHT // stepSize - 1)

def isPrime2(step):
    if step == 1:
        return False
    elif step == 2:
        return True

    for i in range(2, int(step ** 0.5)):
        if step % i == 0:
            return False
    return True

def isPrime(n):
    if n == 1:
        return False
    elif n == 3 or n == 5 or n == 2:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    else:
        k = 1
        while 6 * k + 5 < int(n ** 0.5):
            if n % (6 * k + 5) == 0 or n % (6 * k + 1) == 0:
                return False
            k += 1
        return True


def draw(step):
    if isPrime(step) == True:
        canvas.create_oval(x - stepSize / 4, y - stepSize / 4, x + stepSize / 4, y + stepSize / 4, fill = "black")
        #canvas.create_text(x, y, text = str(step), fill = "black")
    #canvas.create_text(x, y, text = str(step), fill = "black")
    #canvas.create_rectangle(x - stepSize/2, y - stepSize / 2, x + stepSize / 2, y + stepSize / 2)
    canvas.create_line(x0, y0, x, y, fill = "black")
    #canvas.create_oval(x - stepSize / 4, y - stepSize / 4, x + stepSize / 4, y + stepSize / 4, fill = "black")



for i in range(numberCounter):
    draw(step)
    x0 = x
    y0 = y
    if state == 0:
        x += stepSize
    elif state == 1:
        y -= stepSize
    elif state == 2:
        x -= stepSize
    elif state == 3:
        y += stepSize

    if step % stepOrder == 0:
        state = (state + 1) % 4
        turnCounter += 1
        if turnCounter % 2 == 0:
            stepOrder += 1
    step += 1







window.mainloop()
