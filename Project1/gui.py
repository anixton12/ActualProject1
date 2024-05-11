# gui.py
import tkinter as tk
from Project1 import config
from vote_manager import record_vote, validate_voter_id

def setup_window():
    window = tk.Tk()
    window.title("Voting App")
    window.geometry('500x400')
    window.configure(bg='#f0f0f0')

    title_label = tk.Label(window, text="VOTING APPLICATION", font=('Arial', 16, 'bold'), bg='#f0f0f0')
    title_label.pack(pady=(20, 10))

    voter_id_frame = tk.Frame(window, bg='#f0f0f0')
    voter_id_frame.pack(pady=10)
    tk.Label(voter_id_frame, text="Enter Voter ID (numbers only):", bg='#f0f0f0').pack(side=tk.LEFT, padx=10)
    voter_id_entry = tk.Entry(voter_id_frame)
    voter_id_entry.pack(side=tk.RIGHT)

    status_label = tk.Label(window, text="", bg='#f0f0f0')
    status_label.pack(pady=(5, 20))

    votes = {}

    for id, name in config.CANDIDATES.items():
        btn = tk.Button(window, text=name,
                        command=lambda id=id: vote(id, voter_id_entry.get(), window, status_label, votes))
        btn.pack(pady=5, padx=20, fill=tk.X)

    return window

def vote(candidate_id: int, voter_id: str, window, status_label, votes):
    if validate_voter_id(voter_id):
        result = record_vote(voter_id, candidate_id, votes)
        if result == "already_voted":
            status_label.config(text="You have already voted.", fg='red')
        else:
            status_label.config(text=f"You voted for {config.CANDIDATES[candidate_id]}.", fg='green')
    else:
        status_label.config(text="Invalid Voter ID. Please enter a valid numeric ID.", fg='red')

def main():
    window = setup_window()
    window.mainloop()

if __name__ == "__main__":
    main()






