from tkinter import *

from chalenge import Chalenge

BACKGROUND_COLOR = '#3AA6B9'
CHALENGE_COLOR = '#C1ECE4'
BUTTON_COLOR = '#FF9EAA'
TYPING_COLOR = '#FFD0D0'


def timekeeping():
    def point_calculate():
        typing_zone.grid_forget()
        wrongـnumber = 0
        character_number = 0
        wrong_character = 0
        writed_text = typing_zone.get(1.0, "end-1c")
        print(writed_text)
        writed_text_list = writed_text.split(' ')
        selected_text_list = selected_text.split(' ')
        for index, word in enumerate(writed_text_list):
            character_number += len(word)
            if selected_text_list[index] != word:
                wrongـnumber += 1
                wrong_character += len(selected_text_list[index])

        result_msg = f'You typed CPM={character_number}, wr {wrong_character}, WPM={character_number / 5} and {wrongـnumber} wrong Wort'
        status_label.config(text=result_msg)

    typing_zone = Text(root, width=95, height=10, bg=TYPING_COLOR)
    typing_zone.grid(row=1, column=0, pady=20, padx=20)
    status_label.config(text='You are in a challenge')
    start_button.config(text='Started')
    flip_timer = root.after(10000, func=point_calculate)


chalenge = Chalenge()
test_is_running = True
while test_is_running:
    root = Tk()
    root.title('Typing Speed Test')
    root.geometry('900x700')
    root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
    selected_text = chalenge.text_selection()
    test_text = Label(root, text=selected_text, bg=CHALENGE_COLOR, width=95, height=10)
    test_text.grid(row=0, column=0, pady=20, padx=20)
    status_label = Label(root, text='The challenge awaits you')
    status_label.grid(row=2, column=0, pady=20, padx=20)
    start_button = Button(root, text='Start', fg=TYPING_COLOR, bg=BUTTON_COLOR, highlightthickness=0,
                          command=timekeeping)
    start_button.grid(row=3, column=0, pady=20, padx=20)

    root.mainloop()
