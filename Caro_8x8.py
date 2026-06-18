from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Game XO 8X8')
clicked = True
count = 0
win = False

def disableButtons():
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)
    button10.config(state=DISABLED)
    button11.config(state=DISABLED)
    button12.config(state=DISABLED)
    
    button13.config(state=DISABLED)
    button14.config(state=DISABLED)
    button15.config(state=DISABLED)
    button16.config(state=DISABLED)
    button17.config(state=DISABLED)
    button18.config(state=DISABLED)
    button19.config(state=DISABLED)
    button20.config(state=DISABLED)
    button21.config(state=DISABLED)
    button22.config(state=DISABLED)
    button23.config(state=DISABLED)
    button24.config(state=DISABLED)
    button25.config(state=DISABLED)
    
    button26.config(state=DISABLED)
    button27.config(state=DISABLED)
    button28.config(state=DISABLED)
    button29.config(state=DISABLED)
    button30.config(state=DISABLED)
    button31.config(state=DISABLED)
    button32.config(state=DISABLED)
    button33.config(state=DISABLED)
    button34.config(state=DISABLED)
    button35.config(state=DISABLED)
    button36.config(state=DISABLED)
    button37.config(state=DISABLED)
    
    button38.config(state=DISABLED)
    button39.config(state=DISABLED)
    button40.config(state=DISABLED)
    button41.config(state=DISABLED)
    button42.config(state=DISABLED)
    button43.config(state=DISABLED)
    button44.config(state=DISABLED)
    button45.config(state=DISABLED)
    button46.config(state=DISABLED)
    button47.config(state=DISABLED)
    button48.config(state=DISABLED)
    button49.config(state=DISABLED)
    button50.config(state=DISABLED)
    
    button51.config(state=DISABLED)
    button52.config(state=DISABLED)
    button53.config(state=DISABLED)
    button54.config(state=DISABLED)  
    button55.config(state=DISABLED)
    button56.config(state=DISABLED)
    button57.config(state=DISABLED)
    button58.config(state=DISABLED)
    button59.config(state=DISABLED)
    button60.config(state=DISABLED)
    button61.config(state=DISABLED)
    button62.config(state=DISABLED)
    button63.config(state=DISABLED)
    button64.config(state=DISABLED)


def checkWinner():
    global win
    win = False
    # Player X win conditions
    # Horizontal
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" and button4["text"] == "X" and button5["text"] == "X":
        button1.config(bg="#80ffaa")
        button2.config(bg="#80ffaa")
        button3.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        button5.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button9["text"] == "X" and button10["text"] == "X" and button11["text"] == "X" and button12["text"] == "X" and button13["text"] == "X":
        button9.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button17["text"] == "X" and button18["text"] == "X" and button19["text"] == "X" and button20["text"] == "X" and button21["text"] == "X":
        button17.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button25["text"] == "X" and button26["text"] == "X" and button27["text"] == "X" and button28["text"] == "X" and button29["text"] == "X":
        button25.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button33["text"] == "X" and button34["text"] == "X" and button35["text"] == "X" and button36["text"] == "X" and button37["text"] == "X":
        button33.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button41["text"] == "X" and button42["text"] == "X" and button43["text"] == "X" and button44["text"] == "X" and button45["text"] == "X":
        button41.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button49["text"] == "X" and button50["text"] == "X" and button51["text"] == "X" and button52["text"] == "X" and button53["text"] == "X":
        button49.config(bg="#80ffaa")
        button50.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button57["text"] == "X" and button58["text"] == "X" and button59["text"] == "X" and button60["text"] == "X" and button61["text"] == "X":
        button57.config(bg="#80ffaa")
        button58.config(bg="#80ffaa")
        button59.config(bg="#80ffaa")
        button60.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button2["text"] == "X" and button3["text"] == "X" and button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
        button2.config(bg="#80ffaa")
        button3.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        button5.config(bg="#80ffaa")
        button6.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button10["text"] == "X" and button11["text"] == "X" and button12["text"] == "X" and button13["text"] == "X" and button14["text"] == "X":
        button10.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button18["text"] == "X" and button19["text"] == "X" and button20["text"] == "X" and button21["text"] == "X" and button22["text"] == "X":
        button18.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button26["text"] == "X" and button27["text"] == "X" and button28["text"] == "X" and button29["text"] == "X" and button30["text"] == "X":
        button26.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button34["text"] == "X" and button35["text"] == "X" and button36["text"] == "X" and button37["text"] == "X" and button38["text"] == "X":
        button34.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button42["text"] == "X" and button43["text"] == "X" and button44["text"] == "X" and button45["text"] == "X" and button46["text"] == "X":
        button42.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button50["text"] == "X" and button51["text"] == "X" and button52["text"] == "X" and button53["text"] == "X" and button54["text"] == "X":
        button50.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button58["text"] == "X" and button59["text"] == "X" and button60["text"] == "X" and button61["text"] == "X" and button62["text"] == "X":
        button58.config(bg="#80ffaa")
        button59.config(bg="#80ffaa")
        button60.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        button62.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button3["text"] == "X" and button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" and button7["text"] == "X":
        button3.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        button5.config(bg="#80ffaa")
        button6.config(bg="#80ffaa")
        button7.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button11["text"] == "X" and button12["text"] == "X" and button13["text"] == "X" and button14["text"] == "X" and button15["text"] == "X":
        button11.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button19["text"] == "X" and button20["text"] == "X" and button21["text"] == "X" and button22["text"] == "X" and button23["text"] == "X":
        button19.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button27["text"] == "X" and button28["text"] == "X" and button29["text"] == "X" and button30["text"] == "X" and button31["text"] == "X":
        button27.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button35["text"] == "X" and button36["text"] == "X" and button37["text"] == "X" and button38["text"] == "X" and button39["text"] == "X":
        button35.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button43["text"] == "X" and button44["text"] == "X" and button45["text"] == "X" and button46["text"] == "X" and button47["text"] == "X":
        button43.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button51["text"] == "X" and button52["text"] == "X" and button53["text"] == "X" and button54["text"] == "X" and button55["text"] == "X":
        button51.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button59["text"] == "X" and button60["text"] == "X" and button61["text"] == "X" and button62["text"] == "X" and button63["text"] == "X":
        button59.config(bg="#80ffaa")
        button60.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        button62.config(bg="#80ffaa")
        button63.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" and button7["text"] == "X" and button8["text"] == "X":
        button4.config(bg="#80ffaa")
        button5.config(bg="#80ffaa")
        button6.config(bg="#80ffaa")
        button7.config(bg="#80ffaa")
        button8.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button43["text"] == "X" and button44["text"] == "X" and button45["text"] == "X" and button46["text"] == "X" and button47["text"] == "X":
        button43.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        win = True 
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button20["text"] == "X" and button21["text"] == "X" and button22["text"] == "X" and button23["text"] == "X" and button24["text"] == "X":
        button20.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button28["text"] == "X" and button29["text"] == "X" and button30["text"] == "X" and button31["text"] == "X" and button32["text"] == "X":
        button28.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button36["text"] == "X" and button37["text"] == "X" and button38["text"] == "X" and button39["text"] == "X" and button40["text"] == "X":
        button36.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button44["text"] == "X" and button45["text"] == "X" and button46["text"] == "X" and button47["text"] == "X" and button48["text"] == "X":
        button44.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        button48.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()

    elif button52["text"] == "X" and button53["text"] == "X" and button54["text"] == "X" and button55["text"] == "X" and button56["text"] == "X":
        button52.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        button56.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()

    elif button60["text"] == "X" and button61["text"] == "X" and button62["text"] == "X" and button63["text"] == "X" and button64["text"] == "X":
        button60.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        button62.config(bg="#80ffaa")
        button63.config(bg="#80ffaa")
        button64.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()

    # Vertical
    elif button1["text"] == "X" and button9["text"] == "X" and button17["text"] == "X" and button25["text"] == "X" and button33["text"] == "X":
        button1.config(bg="#80ffaa")
        button9.config(bg="#80ffaa")
        button17.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button2["text"] == "X" and button10["text"] == "X" and button18["text"] == "X" and button26["text"] == "X" and button34["text"] == "X":
        button2.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button3["text"] == "X" and button11["text"] == "X" and button19["text"] == "X" and button27["text"] == "X" and button35["text"] == "X":
        button3.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button4["text"] == "X" and button12["text"] == "X" and button20["text"] == "X" and button28["text"] == "X" and button36["text"] == "X":
        button4.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button5["text"] == "X" and button13["text"] == "X" and button21["text"] == "X" and button29["text"] == "X" and button37["text"] == "X":
        button5.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button6["text"] == "X" and button14["text"] == "X" and button22["text"] == "X" and button30["text"] == "X" and button38["text"] == "X":
        button6.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button7["text"] == "X" and button15["text"] == "X" and button23["text"] == "X" and button31["text"] == "X" and button39["text"] == "X":
        button7.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button8["text"] == "X" and button16["text"] == "X" and button24["text"] == "X" and button32["text"] == "X" and button40["text"] == "X":
        button8.config(bg="#80ffaa")
        button16.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button9["text"] == "X" and button17["text"] == "X" and button25["text"] == "X" and button33["text"] == "X" and button41["text"] == "X":
        button9.config(bg="#80ffaa")
        button17.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        button41.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button10["text"] == "X" and button18["text"] == "X" and button26["text"] == "X" and button34["text"] == "X" and button42["text"] == "X":
        button10.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button11["text"] == "X" and button19["text"] == "X" and button27["text"] == "X" and button35["text"] == "X" and button43["text"] == "X":
        button11.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button12["text"] == "X" and button20["text"] == "X" and button28["text"] == "X" and button36["text"] == "X" and button44["text"] == "X":
        button12.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button13["text"] == "X" and button21["text"] == "X" and button29["text"] == "X" and button37["text"] == "X" and button45["text"] == "X":
        button13.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button14["text"] == "X" and button22["text"] == "X" and button30["text"] == "X" and button38["text"] == "X" and button46["text"] == "X":
        button14.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button15["text"] == "X" and button23["text"] == "X" and button31["text"] == "X" and button39["text"] == "X" and button47["text"] == "X":
        button15.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button16["text"] == "X" and button24["text"] == "X" and button32["text"] == "X" and button40["text"] == "X" and button48["text"] == "X":
        button16.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        button48.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button17["text"] == "X" and button25["text"] == "X" and button33["text"] == "X" and button41["text"] == "X" and button49["text"] == "X":
        button17.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        button41.config(bg="#80ffaa")
        button49.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button18["text"] == "X" and button26["text"] == "X" and button34["text"] == "X" and button42["text"] == "X" and button50["text"] == "X":
        button18.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        button50.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button19["text"] == "X" and button27["text"] == "X" and button35["text"] == "X" and button43["text"] == "X" and button51["text"] == "X":
        button19.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button20["text"] == "X" and button28["text"] == "X" and button36["text"] == "X" and button44["text"] == "X" and button52["text"] == "X":
        button20.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button21["text"] == "X" and button29["text"] == "X" and button37["text"] == "X" and button45["text"] == "X" and button53["text"] == "X":
        button21.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button22["text"] == "X" and button30["text"] == "X" and button38["text"] == "X" and button46["text"] == "X" and button54["text"] == "X":
        button22.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button23["text"] == "X" and button31["text"] == "X" and button39["text"] == "X" and button47["text"] == "X" and button55["text"] == "X":
        button23.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button24["text"] == "X" and button32["text"] == "X" and button40["text"] == "X" and button48["text"] == "X" and button56["text"] == "X":
        button24.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        button48.config(bg="#80ffaa")
        button56.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        

    elif button25["text"] == "X" and button33["text"] == "X" and button41["text"] == "X" and button49["text"] == "X" and button57["text"] == "X":
        button25.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        button41.config(bg="#80ffaa")
        button49.config(bg="#80ffaa")
        button57.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button26["text"] == "X" and button34["text"] == "X" and button42["text"] == "X" and button50["text"] == "X" and button58["text"] == "X":
        button26.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        button50.config(bg="#80ffaa")
        button58.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button27["text"] == "X" and button35["text"] == "X" and button43["text"] == "X" and button51["text"] == "X" and button59["text"] == "X":
        button27.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        button59.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button28["text"] == "X" and button36["text"] == "X" and button44["text"] == "X" and button52["text"] == "X" and button60["text"] == "X":
        button28.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button60.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button29["text"] == "X" and button37["text"] == "X" and button45["text"] == "X" and button53["text"] == "X" and button61["text"] == "X":
        button29.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button30["text"] == "X" and button38["text"] == "X" and button46["text"] == "X" and button54["text"] == "X" and button62["text"] == "X":
        button30.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        button62.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button31["text"] == "X" and button39["text"] == "X" and button47["text"] == "X" and button55["text"] == "X" and button63["text"] == "X":
        button31.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        button63.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button32["text"] == "X" and button40["text"] == "X" and button48["text"] == "X" and button56["text"] == "X" and button64["text"] == "X":
        button32.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        button48.config(bg="#80ffaa")
        button56.config(bg="#80ffaa")
        button64.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        

    # Diagonal
    elif button1["text"] == "X" and button10["text"] == "X" and button19["text"] == "X" and button28["text"] == "X" and button37["text"] == "X":
        button1.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button2["text"] == "X" and button11["text"] == "X" and button20["text"] == "X" and button29["text"] == "X" and button38["text"] == "X":
        button2.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button3["text"] == "X" and button12["text"] == "X" and button21["text"] == "X" and button30["text"] == "X" and button39["text"] == "X":
        button3.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button4["text"] == "X" and button13["text"] == "X" and button22["text"] == "X" and button31["text"] == "X" and button40["text"] == "X":
        button4.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button9["text"] == "X" and button18["text"] == "X" and button27["text"] == "X" and button36["text"] == "X" and button45["text"] == "X":
        button9.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button17["text"] == "X" and button26["text"] == "X" and button35["text"] == "X" and button44["text"] == "X" and button53["text"] == "X":
        button17.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button25["text"] == "X" and button34["text"] == "X" and button43["text"] == "X" and button52["text"] == "X" and button61["text"] == "X":
        button25.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button10["text"] == "X" and button19["text"] == "X" and button28["text"] == "X" and button37["text"] == "X" and button46["text"] == "X":
        button10.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button11["text"] == "X" and button20["text"] == "X" and button29["text"] == "X" and button38["text"] == "X" and button47["text"] == "X":
        button11.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button12["text"] == "X" and button21["text"] == "X" and button30["text"] == "X" and button39["text"] == "X" and button48["text"] == "X":
        button12.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button48.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button18["text"] == "X" and button27["text"] == "X" and button36["text"] == "X" and button45["text"] == "X" and button54["text"] == "X":
        button18.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button26["text"] == "X" and button35["text"] == "X" and button44["text"] == "X" and button53["text"] == "X" and button62["text"] == "X":
        button26.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button62.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button19["text"] == "X" and button28["text"] == "X" and button37["text"] == "X" and button46["text"] == "X" and button55["text"] == "X":
        button19.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button20["text"] == "X" and button29["text"] == "X" and button38["text"] == "X" and button47["text"] == "X" and button56["text"] == "X":
        button20.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        button56.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button28["text"] == "X" and button37["text"] == "X" and button46["text"] == "X" and button55["text"] == "X" and button64["text"] == "X":
        button28.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        button64.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button27["text"] == "X" and button36["text"] == "X" and button45["text"] == "X" and button54["text"] == "X" and button63["text"] == "X":
        button27.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        button63.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()

    elif button8["text"] == "X" and button15["text"] == "X" and button22["text"] == "X" and button29["text"] == "X" and button36["text"] == "X":
        button8.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button15["text"] == "X" and button22["text"] == "X" and button29["text"] == "X" and button36["text"] == "X" and button43["text"] == "X":
        button15.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button22["text"] == "X" and button29["text"] == "X" and button36["text"] == "X" and button43["text"] == "X" and button50["text"] == "X":
        button22.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button50.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button29["text"] == "X" and button36["text"] == "X" and button43["text"] == "X" and button50["text"] == "X" and button57["text"] == "X":
        button29.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button50.config(bg="#80ffaa")
        button57.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button7["text"] == "X" and button14["text"] == "X" and button21["text"] == "X" and button28["text"] == "X" and button35["text"] == "X":
        button7.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button14["text"] == "X" and button21["text"] == "X" and button28["text"] == "X" and button35["text"] == "X" and button42["text"] == "X":
        button14.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button21["text"] == "X" and button28["text"] == "X" and button35["text"] == "X" and button42["text"] == "X" and button49["text"] == "X":
        button21.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        button49.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button6["text"] == "X" and button13["text"] == "X" and button20["text"] == "X" and button27["text"] == "X" and button34["text"] == "X":
        button6.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button13["text"] == "X" and button20["text"] == "X" and button27["text"] == "X" and button34["text"] == "X" and button41["text"] == "X":
        button13.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button41.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button5["text"] == "X" and button12["text"] == "X" and button19["text"] == "X" and button26["text"] == "X" and button33["text"] == "X":
        button5.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button16["text"] == "X" and button23["text"] == "X" and button30["text"] == "X" and button37["text"] == "X" and button44["text"] == "X":
        button16.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button23["text"] == "X" and button30["text"] == "X" and button37["text"] == "X" and button44["text"] == "X" and button51["text"] == "X":
        button23.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button30["text"] == "X" and button37["text"] == "X" and button44["text"] == "X" and button51["text"] == "X" and button58["text"] == "X":
        button30.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        button58.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button24["text"] == "X" and button31["text"] == "X" and button38["text"] == "X" and button45["text"] == "X" and button52["text"] == "X":
        button24.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button31["text"] == "X" and button38["text"] == "X" and button45["text"] == "X" and button52["text"] == "X" and button59["text"] == "X":
        button31.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button59.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        
    elif button32["text"] == "X" and button39["text"] == "X" and button46["text"] == "X" and button53["text"] == "X" and button60["text"] == "X":
        button32.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button60.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()

    # Player 2 win conditions
    # Horizontal
    if button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" and button4["text"] == "O" and button5["text"] == "O":
        button1.config(bg="#80ffaa")
        button2.config(bg="#80ffaa")
        button3.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        button5.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button9["text"] == "O" and button10["text"] == "O" and button11["text"] == "O" and button12["text"] == "O" and button13["text"] == "O":
        button9.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button17["text"] == "O" and button18["text"] == "O" and button19["text"] == "O" and button20["text"] == "O" and button21["text"] == "O":
        button17.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button25["text"] == "O" and button26["text"] == "O" and button27["text"] == "O" and button28["text"] == "O" and button29["text"] == "O":
        button25.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button33["text"] == "O" and button34["text"] == "O" and button35["text"] == "O" and button36["text"] == "O" and button37["text"] == "O":
        button33.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button41["text"] == "O" and button42["text"] == "O" and button43["text"] == "O" and button44["text"] == "O" and button45["text"] == "O":
        button41.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button49["text"] == "O" and button50["text"] == "O" and button51["text"] == "O" and button52["text"] == "O" and button53["text"] == "O":
        button49.config(bg="#80ffaa")
        button50.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button57["text"] == "O" and button58["text"] == "O" and button59["text"] == "O" and button60["text"] == "O" and button61["text"] == "O":
        button57.config(bg="#80ffaa")
        button58.config(bg="#80ffaa")
        button59.config(bg="#80ffaa")
        button60.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    elif button2["text"] == "O" and button3["text"] == "O" and button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
        button2.config(bg="#80ffaa")
        button3.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        button5.config(bg="#80ffaa")
        button6.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button10["text"] == "O" and button11["text"] == "O" and button12["text"] == "O" and button13["text"] == "O" and button14["text"] == "O":
        button10.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button18["text"] == "O" and button19["text"] == "O" and button20["text"] == "O" and button21["text"] == "O" and button22["text"] == "O":
        button18.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button26["text"] == "O" and button27["text"] == "O" and button28["text"] == "O" and button29["text"] == "O" and button30["text"] == "O":
        button26.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button34["text"] == "O" and button35["text"] == "O" and button36["text"] == "O" and button37["text"] == "O" and button38["text"] == "O":
        button34.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button42["text"] == "O" and button43["text"] == "O" and button44["text"] == "O" and button45["text"] == "O" and button46["text"] == "O":
        button42.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button50["text"] == "O" and button51["text"] == "O" and button52["text"] == "O" and button53["text"] == "O" and button54["text"] == "O":
        button50.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button58["text"] == "O" and button59["text"] == "O" and button60["text"] == "O" and button61["text"] == "O" and button62["text"] == "O":
        button58.config(bg="#80ffaa")
        button59.config(bg="#80ffaa")
        button60.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        button62.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    elif button3["text"] == "O" and button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" and button7["text"] == "O":
        button3.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        button5.config(bg="#80ffaa")
        button6.config(bg="#80ffaa")
        button7.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button11["text"] == "O" and button12["text"] == "O" and button13["text"] == "O" and button14["text"] == "O" and button15["text"] == "O":
        button11.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button19["text"] == "O" and button20["text"] == "O" and button21["text"] == "O" and button22["text"] == "O" and button23["text"] == "O":
        button19.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button27["text"] == "O" and button28["text"] == "O" and button29["text"] == "O" and button30["text"] == "O" and button31["text"] == "O":
        button27.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button35["text"] == "O" and button36["text"] == "O" and button37["text"] == "O" and button38["text"] == "O" and button39["text"] == "O":
        button35.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button43["text"] == "O" and button44["text"] == "O" and button45["text"] == "O" and button46["text"] == "O" and button47["text"] == "O":
        button43.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
          
    elif button51["text"] == "O" and button52["text"] == "O" and button53["text"] == "O" and button54["text"] == "O" and button55["text"] == "O":
        button51.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button59["text"] == "O" and button60["text"] == "O" and button61["text"] == "O" and button62["text"] == "O" and button63["text"] == "O":
        button59.config(bg="#80ffaa")
        button60.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        button62.config(bg="#80ffaa")
        button63.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" and button7["text"] == "O" and button8["text"] == "O":
        button4.config(bg="#80ffaa")
        button5.config(bg="#80ffaa")
        button6.config(bg="#80ffaa")
        button7.config(bg="#80ffaa")
        button8.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button43["text"] == "O" and button44["text"] == "O" and button45["text"] == "O" and button46["text"] == "O" and button47["text"] == "O":
        button43.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
         
    elif button20["text"] == "O" and button21["text"] == "O" and button22["text"] == "O" and button23["text"] == "O" and button24["text"] == "O":
        button20.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    elif button28["text"] == "O" and button29["text"] == "O" and button30["text"] == "O" and button31["text"] == "O" and button32["text"] == "O":
        button28.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    elif button36["text"] == "O" and button37["text"] == "O" and button38["text"] == "O" and button39["text"] == "O" and button40["text"] == "O":
        button36.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    elif button44["text"] == "O" and button45["text"] == "O" and button46["text"] == "O" and button47["text"] == "O" and button48["text"] == "O":
        button44.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        button48.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    elif button52["text"] == "O" and button53["text"] == "O" and button54["text"] == "O" and button55["text"] == "O" and button56["text"] == "O":
        button52.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        button56.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    elif button60["text"] == "O" and button61["text"] == "O" and button62["text"] == "O" and button63["text"] == "O" and button64["text"] == "O":
        button60.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        button62.config(bg="#80ffaa")
        button63.config(bg="#80ffaa")
        button64.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    # Vertical
    elif button1["text"] == "O" and button9["text"] == "O" and button17["text"] == "O" and button25["text"] == "O" and button33["text"] == "O":
        button1.config(bg="#80ffaa")
        button9.config(bg="#80ffaa")
        button17.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button2["text"] == "O" and button10["text"] == "O" and button18["text"] == "O" and button26["text"] == "O" and button34["text"] == "O":
        button2.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button3["text"] == "O" and button11["text"] == "O" and button19["text"] == "O" and button27["text"] == "O" and button35["text"] == "O":
        button3.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button4["text"] == "O" and button12["text"] == "O" and button20["text"] == "O" and button28["text"] == "O" and button36["text"] == "O":
        button4.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button5["text"] == "O" and button13["text"] == "O" and button21["text"] == "O" and button29["text"] == "O" and button37["text"] == "O":
        button5.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button6["text"] == "O" and button14["text"] == "O" and button22["text"] == "O" and button30["text"] == "O" and button38["text"] == "O":
        button6.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button7["text"] == "O" and button15["text"] == "O" and button23["text"] == "O" and button31["text"] == "O" and button39["text"] == "O":
        button7.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button8["text"] == "O" and button16["text"] == "O" and button24["text"] == "O" and button32["text"] == "O" and button40["text"] == "O":
        button8.config(bg="#80ffaa")
        button16.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        win = True 
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    elif button9["text"] == "O" and button17["text"] == "O" and button25["text"] == "O" and button33["text"] == "O" and button41["text"] == "O":
        button9.config(bg="#80ffaa")
        button17.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        button41.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button10["text"] == "O" and button18["text"] == "O" and button26["text"] == "O" and button34["text"] == "O" and button42["text"] == "O":
        button10.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button11["text"] == "O" and button19["text"] == "O" and button27["text"] == "O" and button35["text"] == "O" and button43["text"] == "O":
        button11.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button12["text"] == "O" and button20["text"] == "O" and button28["text"] == "O" and button36["text"] == "O" and button44["text"] == "O":
        button12.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button13["text"] == "O" and button21["text"] == "O" and button29["text"] == "O" and button37["text"] == "O" and button45["text"] == "O":
        button13.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button14["text"] == "O" and button22["text"] == "O" and button30["text"] == "O" and button38["text"] == "O" and button46["text"] == "O":
        button14.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button15["text"] == "O" and button23["text"] == "O" and button31["text"] == "O" and button39["text"] == "O" and button47["text"] == "O":
        button15.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button16["text"] == "O" and button24["text"] == "O" and button32["text"] == "O" and button40["text"] == "O" and button48["text"] == "O":
        button16.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        button48.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    elif button17["text"] == "O" and button25["text"] == "O" and button33["text"] == "O" and button41["text"] == "O" and button49["text"] == "O":
        button17.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        button41.config(bg="#80ffaa")
        button49.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button18["text"] == "O" and button26["text"] == "O" and button34["text"] == "O" and button42["text"] == "O" and button50["text"] == "O":
        button18.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        button50.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button19["text"] == "O" and button27["text"] == "O" and button35["text"] == "O" and button43["text"] == "O" and button51["text"] == "O":
        button19.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button20["text"] == "O" and button28["text"] == "O" and button36["text"] == "O" and button44["text"] == "O" and button52["text"] == "O":
        button20.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button21["text"] == "O" and button29["text"] == "O" and button37["text"] == "O" and button45["text"] == "O" and button53["text"] == "O":
        button21.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button22["text"] == "O" and button30["text"] == "O" and button38["text"] == "O" and button46["text"] == "O" and button54["text"] == "O":
        button22.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button23["text"] == "O" and button31["text"] == "O" and button39["text"] == "O" and button47["text"] == "O" and button55["text"] == "O":
        button23.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button24["text"] == "O" and button32["text"] == "O" and button40["text"] == "O" and button48["text"] == "O" and button56["text"] == "O":
        button24.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        button48.config(bg="#80ffaa")
        button56.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()


    elif button25["text"] == "O" and button33["text"] == "O" and button41["text"] == "O" and button49["text"] == "O" and button57["text"] == "O":
        button25.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        button41.config(bg="#80ffaa")
        button49.config(bg="#80ffaa")
        button57.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button26["text"] == "O" and button34["text"] == "O" and button42["text"] == "O" and button50["text"] == "O" and button58["text"] == "O":
        button26.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        button50.config(bg="#80ffaa")
        button58.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button27["text"] == "O" and button35["text"] == "O" and button43["text"] == "O" and button51["text"] == "O" and button59["text"] == "O":
        button27.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        button59.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button28["text"] == "O" and button36["text"] == "O" and button44["text"] == "O" and button52["text"] == "O" and button60["text"] == "O":
        button28.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button60.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button29["text"] == "O" and button37["text"] == "O" and button45["text"] == "O" and button53["text"] == "O" and button61["text"] == "O":
        button29.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button30["text"] == "O" and button38["text"] == "O" and button46["text"] == "O" and button54["text"] == "O" and button62["text"] == "O":
        button30.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        button62.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button31["text"] == "O" and button39["text"] == "O" and button47["text"] == "O" and button55["text"] == "O" and button63["text"] == "O":
        button31.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        button63.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button32["text"] == "O" and button40["text"] == "O" and button48["text"] == "O" and button56["text"] == "O" and button64["text"] == "O":
        button32.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        button48.config(bg="#80ffaa")
        button56.config(bg="#80ffaa")
        button64.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    # Diagonal
    elif button1["text"] == "O" and button10["text"] == "O" and button19["text"] == "O" and button28["text"] == "O" and button37["text"] == "O":
        button1.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button2["text"] == "O" and button11["text"] == "O" and button20["text"] == "O" and button29["text"] == "O" and button38["text"] == "O":
        button2.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button3["text"] == "O" and button12["text"] == "O" and button21["text"] == "O" and button30["text"] == "O" and button39["text"] == "O":
        button3.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button4["text"] == "O" and button13["text"] == "O" and button22["text"] == "O" and button31["text"] == "O" and button40["text"] == "O":
        button4.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    elif button9["text"] == "O" and button18["text"] == "O" and button27["text"] == "O" and button36["text"] == "O" and button45["text"] == "O":
        button9.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button17["text"] == "O" and button26["text"] == "O" and button35["text"] == "O" and button44["text"] == "O" and button53["text"] == "O":
        button17.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button25["text"] == "O" and button34["text"] == "O" and button43["text"] == "O" and button52["text"] == "O" and button61["text"] == "O":
        button25.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button10["text"] == "O" and button19["text"] == "O" and button28["text"] == "O" and button37["text"] == "O" and button46["text"] == "O":
        button10.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button11["text"] == "O" and button20["text"] == "O" and button29["text"] == "O" and button38["text"] == "O" and button47["text"] == "O":
        button11.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button12["text"] == "O" and button21["text"] == "O" and button30["text"] == "O" and button39["text"] == "O" and button48["text"] == "O":
        button12.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button48.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button18["text"] == "O" and button27["text"] == "O" and button36["text"] == "O" and button45["text"] == "O" and button54["text"] == "O":
        button18.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button26["text"] == "O" and button35["text"] == "O" and button44["text"] == "O" and button53["text"] == "O" and button62["text"] == "O":
        button26.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button62.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button19["text"] == "O" and button28["text"] == "O" and button37["text"] == "O" and button46["text"] == "O" and button55["text"] == "O":
        button19.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button20["text"] == "O" and button29["text"] == "O" and button38["text"] == "O" and button47["text"] == "O" and button56["text"] == "O":
        button20.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        button56.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button28["text"] == "O" and button37["text"] == "O" and button46["text"] == "O" and button55["text"] == "O" and button64["text"] == "O":
        button28.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        button64.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button27["text"] == "O" and button36["text"] == "O" and button45["text"] == "O" and button54["text"] == "O" and button63["text"] == "O":
        button27.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        button63.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    elif button8["text"] == "O" and button15["text"] == "O" and button22["text"] == "O" and button29["text"] == "O" and button36["text"] == "O":
        button8.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button15["text"] == "O" and button22["text"] == "O" and button29["text"] == "O" and button36["text"] == "O" and button43["text"] == "O":
        button15.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button22["text"] == "O" and button29["text"] == "O" and button36["text"] == "O" and button43["text"] == "O" and button50["text"] == "O":
        button22.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button50.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button29["text"] == "O" and button36["text"] == "O" and button43["text"] == "O" and button50["text"] == "O" and button57["text"] == "O":
        button29.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button50.config(bg="#80ffaa")
        button57.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button7["text"] == "O" and button14["text"] == "O" and button21["text"] == "O" and button28["text"] == "O" and button35["text"] == "O":
        button7.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button14["text"] == "O" and button21["text"] == "O" and button28["text"] == "O" and button35["text"] == "O" and button42["text"] == "O":
        button14.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button21["text"] == "O" and button28["text"] == "O" and button35["text"] == "O" and button42["text"] == "O" and button49["text"] == "O":
        button21.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        button49.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button6["text"] == "O" and button13["text"] == "O" and button20["text"] == "O" and button27["text"] == "O" and button34["text"] == "O":
        button6.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button13["text"] == "O" and button20["text"] == "O" and button27["text"] == "O" and button34["text"] == "O" and button41["text"] == "O":
        button13.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button41.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button5["text"] == "O" and button12["text"] == "O" and button19["text"] == "O" and button26["text"] == "O" and button33["text"] == "O":
        button5.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button16["text"] == "O" and button23["text"] == "O" and button30["text"] == "O" and button37["text"] == "O" and button44["text"] == "O":
        button16.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button23["text"] == "O" and button30["text"] == "O" and button37["text"] == "O" and button44["text"] == "O" and button51["text"] == "O":
        button23.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button30["text"] == "O" and button37["text"] == "O" and button44["text"] == "O" and button51["text"] == "O" and button58["text"] == "O":
        button30.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        button58.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button24["text"] == "O" and button31["text"] == "O" and button38["text"] == "O" and button45["text"] == "O" and button52["text"] == "O":
        button24.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button31["text"] == "O" and button38["text"] == "O" and button45["text"] == "O" and button52["text"] == "O" and button59["text"] == "O":
        button31.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button59.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        
    elif button32["text"] == "O" and button39["text"] == "O" and button46["text"] == "O" and button53["text"] == "O" and button60["text"] == "O":
        button32.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button60.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

def checkDraw():
    global count, win
    
    if count == 64 and win == False:
        messagebox.showerror("OX Game", "DRAW!!")
        start()

def buttonClicked(button):
    global clicked, count
    if button["text"] == " " and clicked == True:
        button["text"] = "X"
        clicked = False
        count += 1
        checkWinner()
        checkDraw
    elif button["text"] == " " and clicked == False:
        button["text"] = "O"
        clicked = True
        count += 1
        checkWinner()
        checkDraw()
    else:
        messagebox.showerror("OX Game", "LỖI!! Vui lòng chọn lại")

def start():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16, button17, button18, button19, button20, button21, button22, button23, button24, button25, button26, button27, button28, button29, button30, button31, button32, button33, button34, button35, button36, button37, button38, button39, button40, button41, button42, button43, button44, button45, button46, button47, button48, button49, button50, button51, button52, button53, button54, button55, button56, button57, button58, button59, button60, button61, button62, button63, button64
    global clicked, count
    clicked = True
    count = 0

    # Create buttons
    button1 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button1))
    button2 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button2))
    button3 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button3))
    button4 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button4))
    button5 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button5))

    button6 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button6))
    button7 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button7))
    button8 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button8))
    button9 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button9))
    button10 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button10))

    button11 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button11))
    button12 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button12))
    button13 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button13))
    button14 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button14))
    button15 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button15))

    button16 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button16))
    button17 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button17))
    button18 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button18))
    button19 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button19))
    button20 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button20))

    button21 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button21))
    button22 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button22))
    button23 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button23))
    button24 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button24))
    button25 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button25))

    button26 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button26))
    button27 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button27))
    button28 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button28))
    button29 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button29))
    button30 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button30))

    button31 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button31))
    button32 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button32))
    button33 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button33))
    button34 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button34))
    button35 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button35))
    button36 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button36))

    button37 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button37))
    button38 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button38))
    button39 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button39))
    button40 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button40))
    button41 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button41))
    button42 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button42))

    button43 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button43))
    button44 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button44))
    button45 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button45))
    button46 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button46))
    button47 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button47))
    button48 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button48))

    button49 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button49))
    button50 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button50))
    button51 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button51))
    button52 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button52))
    button53 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button53))
    button54 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button54))

    button55 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button55))
    button56 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button56))
    button57 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button57))
    button58 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button58))
    button59 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button59))
    button60 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button60))

    button61 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button61))
    button62 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button62))
    button63 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button63))
    button64 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, command=lambda: buttonClicked(button64))


    # Xây dựng layout 6x6
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=0, column=3)
    button5.grid(row=0, column=4)
    button6.grid(row=0, column=5)
    button7.grid(row=0, column=6)
    button8.grid(row=0, column=7)

    button9.grid(row=1, column=0)
    button10.grid(row=1, column=1)
    button11.grid(row=1, column=2)
    button12.grid(row=1, column=3)
    button13.grid(row=1, column=4)
    button14.grid(row=1, column=5)
    button15.grid(row=1, column=6)
    button16.grid(row=1, column=7)

    button17.grid(row=2, column=0)
    button18.grid(row=2, column=1)
    button19.grid(row=2, column=2)
    button20.grid(row=2, column=3)
    button21.grid(row=2, column=4)
    button22.grid(row=2, column=5)
    button23.grid(row=2, column=6)
    button24.grid(row=2, column=7)

    button25.grid(row=3, column=0)
    button26.grid(row=3, column=1)
    button27.grid(row=3, column=2)
    button28.grid(row=3, column=3)
    button29.grid(row=3, column=4)
    button30.grid(row=3, column=5)
    button31.grid(row=3, column=6)
    button32.grid(row=3, column=7)

    button33.grid(row=4, column=0)
    button34.grid(row=4, column=1)
    button35.grid(row=4, column=2)
    button36.grid(row=4, column=3)
    button37.grid(row=4, column=4)
    button38.grid(row=4, column=5)
    button39.grid(row=4, column=6)
    button40.grid(row=4, column=7)

    button41.grid(row=5, column=0)
    button42.grid(row=5, column=1)
    button43.grid(row=5, column=2)
    button44.grid(row=5, column=3)
    button45.grid(row=5, column=4)
    button46.grid(row=5, column=5)
    button47.grid(row=5, column=6)
    button48.grid(row=5, column=7)

    button49.grid(row=6, column=0)
    button50.grid(row=6, column=1)
    button51.grid(row=6, column=2)
    button52.grid(row=6, column=3)
    button53.grid(row=6, column=4)
    button54.grid(row=6, column=5)
    button55.grid(row=6, column=6)
    button56.grid(row=6, column=7)

    button57.grid(row=7, column=0)
    button58.grid(row=7, column=1)
    button59.grid(row=7, column=2)
    button60.grid(row=7, column=3)
    button61.grid(row=7, column=4)
    button62.grid(row=7, column=5)
    button63.grid(row=7, column=6)
    button64.grid(row=7, column=7)

# Tạo menu trò chơi
gameMenu = Menu(root)
root.config(menu = gameMenu)
# Tạo menu tùy chọn trò chơi
optionMenu = Menu(gameMenu, tearoff=False)
gameMenu.add_cascade(label="Options", menu=optionMenu)
optionMenu.add_command(label="Restart Game", command=start)
#root.iconbitmap('pyc.ico')
start()
root.mainloop()