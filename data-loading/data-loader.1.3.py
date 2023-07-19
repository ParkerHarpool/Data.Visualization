import tkinter as tk
from tkinter import ttk
import tkcalendar as tkC
from tkcalendar import DateEntry

class TimeCombobox(ttk.Combobox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['values'] = [f"{str(hour).zfill(2)}:{str(minute).zfill(2)}" for hour in range(24) for minute in range(0, 60, 15)]
        self.current(0)

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        style = ttk.Style(self)
        style.theme_use('clam')

        style.configure("TLabel", foreground="black", background="white", padding=10, font=('Helvetica', 11))
        style.configure("TCombobox", padding=5, font=('Helvetica', 11))
        style.configure("TButton", foreground="black", background="#008CBA", padding=10, font=('Helvetica', 11), borderwidth=0)

        self.title("Main Application")
        self.geometry("1920x1080")

        self.paned_window = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=1)

        self.left_frame = ttk.Frame(self.paned_window, width=960)
        self.right_frame = ttk.Frame(self.paned_window, width=960)

        self.paned_window.add(self.left_frame, weight=1)
        self.paned_window.add(self.right_frame, weight=1)

        self.create_left_section()

    def create_left_section(self):
        self.participant_var = tk.StringVar()
        self.start_date_var = tk.StringVar()
        self.end_date_var = tk.StringVar()

        self.checkbox_vars = [tk.IntVar() for _ in range(7)]
        self.checkbox_labels = ["Acc magnitude avg", "Eda avg", "Temp avg", "Movement intensity", "Steps count", "Rest", "On Wrist"]

        ttk.Label(self.left_frame, text="Participant:", style="TLabel").grid(column=0, row=0, padx=20, pady=10)
        self.participant_combobox = ttk.Combobox(self.left_frame, textvariable=self.participant_var, style="TCombobox")
        self.participant_combobox['values'] = ['Participant ' + str(i) for i in range(1, 11)]
        self.participant_combobox.grid(column=1, row=0, sticky='w')

        ttk.Label(self.left_frame, text="Start Date:", style="TLabel").grid(column=0, row=1, padx=20, pady=10)
        self.start_date_entry = DateEntry(self.left_frame, textvariable=self.start_date_var)
        self.start_date_entry.grid(column=1, row=1, sticky='w')

        ttk.Label(self.left_frame, text="Start Time:", style="TLabel").grid(column=0, row=2, padx=20, pady=10)
        self.start_time_entry = TimeCombobox(self.left_frame)
        self.start_time_entry.grid(column=1, row=2, sticky='w')

        ttk.Label(self.left_frame, text="End Date:", style="TLabel").grid(column=0, row=3, padx=20, pady=10)
        self.end_date_entry = DateEntry(self.left_frame, textvariable=self.end_date_var)
        self.end_date_entry.grid(column=1, row=3, sticky='w')

        ttk.Label(self.left_frame, text="End Time:", style="TLabel").grid(column=0, row=4, padx=20, pady=10)
        self.end_time_entry = TimeCombobox(self.left_frame)
        self.end_time_entry.grid(column=1, row=4, sticky='w')

        # Create checkboxes with appropriate labels
        for i, label in enumerate(self.checkbox_labels):
            ttk.Checkbutton(self.left_frame, text=label, variable=self.checkbox_vars[i]).grid(column=0, row=5+i, sticky='w', padx=20, pady=10)

        self.confirm_button = ttk.Button(self.left_frame, text="Confirm", command=self.confirm, style="TButton")
        self.confirm_button.grid(column=1, row=5+7, pady=20)

    def confirm(self):
        participant = self.participant_var.get()
        start_date = self.start_date_var.get()
        start_time = self.start_time_entry.get()
        end_date = self.end_date_var.get()
        end_time = self.end_time_entry.get()
        
        # Get the state of the checkboxes
        checkbox_states = [var.get() for var in self.checkbox_vars]

        print({
            "participant": participant,
            "start_date": start_date,
            "start_time": start_time,
            "end_date": end_date,
            "end_time": end_time,
            "checkbox_states": dict(zip(self.checkbox_labels, checkbox_states))
        })

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()