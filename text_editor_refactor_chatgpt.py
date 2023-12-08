import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

class DragonTextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Dragon Text Editor")
        self.master.rowconfigure(0, minsize=600)
        self.master.columnconfigure(1, minsize=800)

        self.txt_edit = tk.Text(self.master)
        self.frame_buttons = tk.Frame(self.master, relief=tk.RAISED)
        self.btn_open = tk.Button(self.frame_buttons, text="Open File", command=self.open_file)
        self.btn_save = tk.Button(self.frame_buttons, text="Save As", command=self.save_file)

        self.btn_open.grid(column=0, row=0, sticky="ew", padx=5, pady=5)
        self.btn_save.grid(column=0, row=1, sticky="ew", padx=5)

        self.frame_buttons.grid(column=0, row=0, sticky="ns")
        self.txt_edit.grid(column=1, row=0, sticky="nsew")

    def open_file(self):
        filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

        if not filepath:
            return

        self.txt_edit.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            self.txt_edit.insert(tk.END, text)

        self.master.title(f'Dragon Text Editor - {filepath}')

    def save_file(self):
        filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

        if not filepath:
            return

        with open(filepath, "w") as output_file:
            text = self.txt_edit.get(1.0, tk.END)
            output_file.write(text)

        self.master.title(f'Dragon Text Editor - {filepath}')

if __name__ == "__main__":
    root = tk.Tk()
    app = DragonTextEditor(root)
    root.mainloop()
