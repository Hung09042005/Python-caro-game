from tkinter import Tk, Button, Label
from tkinter.font import Font
from copy import deepcopy

class Board:
    def __init__(self, other=None):
        self.player = 'X'
        self.oppoment = 'O'
        self.empty = ' '
        self.size = 9
        self.win_length = 5
        self.fields = {}
        for y in range(self.size):
            for x in range(self.size):
                self.fields[x, y] = self.empty
        if other:
            self.__dict__ = deepcopy(other.__dict__)

    def move(self, x, y):
        board = Board(self)
        board.fields[x, y] = board.player
        board.player, board.oppoment = board.oppoment, board.player
        return board

    def __minimax(self, player, depth=2):
        winner = self.won()
        if winner:
            return (-10000, None) if player else (10000, None)
        if self.tied():
            return (0, None)
        if depth == 0:
            return (self.evaluate(), None)

        if player:
            best = -float('inf'), None
            for (x, y) in self.fields:
                if self.fields[x, y] == self.empty:
                    value = self.move(x, y).__minimax(False, depth - 1)[0]
                    if value > best[0]:
                        best = value, (x, y)
            return best
        else:
            best = float('inf'), None
            for (x, y) in self.fields:
                if self.fields[x, y] == self.empty:
                    value = self.move(x, y).__minimax(True, depth - 1)[0]
                    if value < best[0]:
                        best = value, (x, y)
            return best

    def best(self):
        return self.__minimax(True)[1]

    def tied(self):
        for (x, y) in self.fields:
            if self.fields[x, y] == self.empty:
                return False
        return self.won() is None

    def won(self):
        lines = []
        for y in range(self.size):
            for x in range(self.size - self.win_length + 1):
                lines.append([(x + i, y) for i in range(self.win_length)])
        for x in range(self.size):
            for y in range(self.size - self.win_length + 1):
                lines.append([(x, y + i) for i in range(self.win_length)])
        for x in range(self.size - self.win_length + 1):
            for y in range(self.size - self.win_length + 1):
                lines.append([(x + i, y + i) for i in range(self.win_length)])
        for x in range(self.win_length - 1, self.size):
            for y in range(self.size - self.win_length + 1):
                lines.append([(x - i, y + i) for i in range(self.win_length)])

        for line in lines:
            if all(self.fields[pos] == self.oppoment for pos in line):
                return line
            if all(self.fields[pos] == self.player for pos in line):
                return line
        return None

    def evaluate(self):
        score = 0
        lines = []
        for y in range(self.size):
            for x in range(self.size - self.win_length + 1):
                lines.append([(x + i, y) for i in range(self.win_length)])
        for x in range(self.size):
            for y in range(self.size - self.win_length + 1):
                lines.append([(x, y + i) for i in range(self.win_length)])
        for x in range(self.size - self.win_length + 1):
            for y in range(self.size - self.win_length + 1):
                lines.append([(x + i, y + i) for i in range(self.win_length)])
        for x in range(self.win_length - 1, self.size):
            for y in range(self.size - self.win_length + 1):
                lines.append([(x - i, y + i) for i in range(self.win_length)])

        for line in lines:
            line_values = [self.fields[pos] for pos in line]
            if self.oppoment not in line_values:
                count = line_values.count(self.player)
                if count > 0:
                    score += 10 ** count
            if self.player not in line_values:
                count = line_values.count(self.oppoment)
                if count > 0:
                    score -= 10 ** count
        return score

class GUI:
    def __init__(self):
        self.app = Tk()
        self.app.title('Ứng dụng Giải thuật Minimax - XO 9x9')
        self.app.resizable(width=False, height=False)
        self.app.configure(bg='#E6F2FF')
        self.board = Board()
        self.font = Font(family="Helvetica", size=16, weight='bold')
        self.buttons = {}

        for (x, y) in self.board.fields:
            handler = lambda x=x, y=y: self.move(x, y)
            button = Button(self.app, command=handler, font=self.font, width=2, height=1)
            button.grid(row=y, column=x)
            self.buttons[x, y] = button

        reset_button = Button(self.app, text='Reset', command=self.reset)
        reset_button.grid(row=self.board.size + 1, column=0, columnspan=self.board.size, sticky="WE")

        # Thêm label thông báo
        self.status = Label(self.app, text='Đang chơi...', font=self.font)
        self.status.grid(row=self.board.size + 2, column=0, columnspan=self.board.size)

        self.update()

    def reset(self):
        self.board = Board()
        self.update()
        self.status.config(text='Đang chơi...', fg='black')

    def move(self, x, y):
        self.app.config(cursor="watch")
        self.app.update()

        if self.board.fields[x, y] != self.board.empty or self.board.won():
            return

        self.board = self.board.move(x, y)
        self.update()

        if not self.board.won() and not self.board.tied():
            move = self.board.best()
            if move:
                self.board = self.board.move(*move)
                self.update()

        self.app.config(cursor="")

    def update(self):
        for (x, y) in self.board.fields:
            text = self.board.fields[x, y]
            self.buttons[x, y]['text'] = text
            self.buttons[x, y]['disabledforeground'] = 'black'
            self.buttons[x, y]['state'] = 'normal' if text == self.board.empty else 'disabled'

        winner_line = self.board.won()
        if winner_line:
            winner_symbol = self.board.fields[winner_line[0]]
            for (x, y) in winner_line:
                self.buttons[x, y]['disabledforeground'] = 'red'
            for (x, y) in self.buttons:
                self.buttons[x, y]['state'] = 'disabled'
            if winner_symbol == 'X':
                self.status.config(text='Bạn thắng!', fg='green')
            else:
                self.status.config(text='AI thắng!', fg='red')
        elif self.board.tied():
            self.status.config(text='Hòa!', fg='blue')
        else:
            self.status.config(text='Đang chơi...', fg='black')

        for (x, y) in self.board.fields:
            self.buttons[x, y].update()

    def mainloop(self):
        self.app.mainloop()

if __name__ == '__main__':
    GUI().mainloop()
