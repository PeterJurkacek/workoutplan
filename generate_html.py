# %%
import pandas as pd
# %%

# Read the CSV file
# df = pd.read_csv('your_workout_plan.csv')
df = pd.read_csv('your_workout_plan.csv', sep=';')
df['Warm-up'] = df['Warm-up'].notna()
def to_snake_case(string):
    string = string.strip().lower()
    string = string.replace(" ", "_")
    return string
df['Img'] = 'images/' + df['Exercise'].apply(to_snake_case) + ".png"
df.loc[df['Warm-up'], 'Muscle Group'] = 'warmup'
df['Sets'] = df['Sets'].fillna(0).astype(int) 
# %%
df.to_csv('workout_plan2.csv')
# %%
df['Order']
# %%

html = ''
for day in [1, 2, 3, 4, 5]:
    group = df[df['Order'] == day]
    print(day)
    day_html = f'''
    <div class="header-row-cell">
      <h1>Day {day}</h1>
    </div>
    '''
    html += day_html    
    for index, row in group.iterrows():
        exercise = row['Exercise']
        muscle_group = row['Muscle Group']
        sets = row['Sets']
        reps = row['Reps']
        video_url = row['Video url']
        img = row['Img']
        
        muscle_groups = row['Muscle Group'].split(",")
        icons = ""
        for mg in muscle_groups:
            icon = 'icons/' + to_snake_case(mg) + ".png"
            icons+=f'''<img src="{icon}" alt="{mg} icon">
            '''
    
        excercise_html = f'''
        <div class="exercise">
            <div class="excercise-header-container">
                <div class="excercise-image-container">
                    <img src="{img}" alt="{exercise}">
                </div>
                <a href="{video_url}" target="_blank">
                    <h2>{exercise}</h2>
                </a>
            </div>
            <div class="exercise-icons">
                {icons}
            </div>
            <div class="excercise-body-container">
                <p>{reps}</p>
                <p>Série: {sets}</p>
            </div>
        </div>
        '''
    
        html += excercise_html

# Output the HTML code for all exercises

with open('jou.html', 'w') as f:
    f.write(html)

# %%
