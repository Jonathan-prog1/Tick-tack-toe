from graphics import Window,EntryWithPlaceholder

def main():
    win = Window(800, 800)
    
    entry = EntryWithPlaceholder(win.get_root(), placeholder='Player 1', font_size=14)
    entry2 = EntryWithPlaceholder(win.get_root(), placeholder='Player 2', font_size=14)
    entry.pack()
    entry2.pack()
    win.make_window()
    print("Thank you for playing")

main()