"""
Hi Lucas,

Here we have a CSV file with our dataset.
Goal here is to read the dataset, clean it by adding relivent infomring (year, average points per year by team), filter it by the teams we want to compare.
I've added comments bellow.
Let me know if you have any questions.

FYI for fun: look at the World Cup winners and their spikes

-Pawl
"""

import pandas as pd                 # Pandas is used to manipulate data 
import matplotlib.pyplot as plt     # Matplotlib library is use to create graphs
import tkinter as tk                # Tkinter creates the window (applacation)
from tkinter import ttk

df = pd.read_csv('ranking_fifa.csv')            # Reads CSV file in the same folder as the program
df['Year'] = df['date'].str[:4].astype(int)     # Taking the Date column and extract the Year and save as an Integer in a new column

average_points_per_team_per_year = df.groupby(['Year', 'team'])['total_points'].mean().reset_index()    # Calculate the average points per year for each team
teams = sorted(average_points_per_team_per_year['team'].unique())                                       # Get a list of all unique teams

# Create tkinker window
root = tk.Tk()
root.title("FIFA Team Comparison")

root.geometry("400x200")

# Create Labels in our App to select two teams
team_1_label = tk.Label(root, text="Select First Team:")
team_1_label.pack(pady=5)
# Assign a variable (team name)
team_1_var = tk.StringVar()
team_1_dropdown = ttk.Combobox(root, textvariable=team_1_var, values=teams)
team_1_dropdown.pack(pady=5)

team_2_label = tk.Label(root, text="Select Second Team:")
team_2_label.pack(pady=5)

team_2_var = tk.StringVar()
team_2_dropdown = ttk.Combobox(root, textvariable=team_2_var, values=teams)
team_2_dropdown.pack(pady=5)

# Create the graph using the inputs from Labels / plot_teams() is a function we created that we can call again
def plot_teams():
    team_1_name = team_1_var.get()
    team_2_name = team_2_var.get()

    if team_1_name and team_2_name:     # If both are True (exist) contiune 
        team_1_data = average_points_per_team_per_year[average_points_per_team_per_year['team'] == team_1_name]
        team_2_data = average_points_per_team_per_year[average_points_per_team_per_year['team'] == team_2_name]

        # Plot the average points per year for both teams
        plt.figure(figsize=(10, 6))

        plt.plot(team_1_data['Year'], team_1_data['total_points'], marker='o', linestyle='-', color='red', label=team_1_name)
        plt.plot(team_2_data['Year'], team_2_data['total_points'], marker='o', linestyle='-', color='blue', label=team_2_name)

        # Title and Labeling graph
        plt.title(f'Average FIFA Points Per Year: {team_1_name} vs {team_2_name}')
        plt.xlabel('Year')
        plt.ylabel('Average Points')
        plt.grid(True)
        plt.legend(loc='upper left')

        plt.show()
    else:
        tk.messagebox.showerror("Input Error", "Please select both teams.") # If a team is missing, show this message 

plot_button = tk.Button(root, text="Plot", command=plot_teams) # On clicking button, run plot_teams function
plot_button.pack(pady=20)

root.mainloop()  # run root (main program)
