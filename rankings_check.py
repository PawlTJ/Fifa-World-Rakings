import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

df = pd.read_csv('ranking_fifa.csv')
df['Year'] = df['date'].str[:4].astype(int)

average_points_per_team_per_year = df.groupby(['Year', 'team'])['total_points'].mean().reset_index() # Calculate the average points per year for each team
teams = sorted(average_points_per_team_per_year['team'].unique()) # Get a list of all unique teams

# Create tkinker window
root = tk.Tk()
root.title("FIFA Team Comparison")

root.geometry("400x200")

team_1_label = tk.Label(root, text="Select First Team:")
team_1_label.pack(pady=5)

team_1_var = tk.StringVar()
team_1_dropdown = ttk.Combobox(root, textvariable=team_1_var, values=teams)
team_1_dropdown.pack(pady=5)

team_2_label = tk.Label(root, text="Select Second Team:")
team_2_label.pack(pady=5)

team_2_var = tk.StringVar()
team_2_dropdown = ttk.Combobox(root, textvariable=team_2_var, values=teams)
team_2_dropdown.pack(pady=5)


def plot_teams():
    team_1_name = team_1_var.get()
    team_2_name = team_2_var.get()

    if team_1_name and team_2_name:
        team_1_data = average_points_per_team_per_year[average_points_per_team_per_year['team'] == team_1_name]
        team_2_data = average_points_per_team_per_year[average_points_per_team_per_year['team'] == team_2_name]

        # Plot the average points per year for both teams
        plt.figure(figsize=(10, 6))

        plt.plot(team_1_data['Year'], team_1_data['total_points'], marker='o', linestyle='-', color='red', label=team_1_name)
        plt.plot(team_2_data['Year'], team_2_data['total_points'], marker='o', linestyle='-', color='blue', label=team_2_name)

        plt.title(f'Average FIFA Points Per Year: {team_1_name} vs {team_2_name}')
        plt.xlabel('Year')
        plt.ylabel('Average Points')
        plt.grid(True)
        plt.legend(loc='upper left')

        plt.show()
    else:
        tk.messagebox.showerror("Input Error", "Please select both teams.")

plot_button = tk.Button(root, text="Plot", command=plot_teams)
plot_button.pack(pady=20)

root.mainloop()
