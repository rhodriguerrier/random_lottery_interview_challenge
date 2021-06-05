from typing import List
import random
import tkinter as tk


number_colouring = {
    "grey": [1, 9],
    "blue": [10, 19],
    "pink": [20, 29],
    "green": [30, 39],
    "yellow": [40, 49]
}


class LotteryApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Random Lottery Number Generator")
        self.geometry("400x200")
        self.resizable(False, False)

        # Initialise layout structure
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(side="top", fill="both", expand=True)
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=1)
        self.main_frame.rowconfigure(2, weight=1)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.columnconfigure(2, weight=1)

        title_label = tk.Label(self.main_frame, text="Generate Random Lottery Numbers", font=("Helvetic", 12))
        title_label.grid(row=0, column=1)

        # Dropdown widget, default set to 6 but can toggle to 7
        self.n_lottery_nums = tk.IntVar(self)
        self.n_lottery_nums.set(6)
        n_lottery_choice = tk.OptionMenu(self.main_frame, self.n_lottery_nums, 6, 7)
        n_lottery_choice.grid(row=1, column=1)

        # Button to trigger function to generate and display numbers
        gen_button = tk.Button(
            self.main_frame,
            text="Generate Numbers",
            command=self.generate_n_display
        )
        gen_button.grid(row=2, column=1)

        # Frame for lottery number labels
        self.sub_frame = tk.Frame(self.main_frame)
        self.sub_frame.grid(row=3, column=1, pady=10)
    
    def clear_numbers(self):
        # Clears all lottery numbers when generating new ones
        for widget in self.sub_frame.winfo_children():
            widget.destroy()
    
    def generate_n_display(self):
        self.clear_numbers()
        no_of_nums = self.n_lottery_nums.get()
        nums = sorted(random.sample(range(1, 50), no_of_nums))
        for i in range(no_of_nums):
            temp_widget = tk.Label(self.sub_frame, bg=self.get_colours(nums[i]), text=str(nums[i]))
            temp_widget.grid(row=4, column=i)
    
    def get_colours(self, lottery_num):
        # Returns a string colour name to use in lottery number label
        for colour in number_colouring:
            if number_colouring[colour][0] <= lottery_num <= number_colouring[colour][1]:
                return colour


if __name__ == "__main__":
    app = LotteryApp()
    app.mainloop()
