# %%
import pandas as pd
# %%

# Read the CSV file
# df = pd.read_csv('your_workout_plan.csv')
df = pd.read_csv('/Users/pj/Downloads/your_workout_plan.csv', sep=';')
df['Warm-up'] = df['Warm-up'].notna()
def to_snake_case(string):
    string = string.strip().lower()
    string = string.replace(" ", "_")
    return string
df['Img'] = 'images/' + df['Exercise'].apply(to_snake_case) + ".png"
df.loc[df['Warm-up'], 'Muscle Group'] = 'warmup'
df['Sets'] = df['Sets'].fillna(0).astype(int) 
df['Order'] = df.index
# %%
df.to_csv('workout_plan2.csv')
# %%

# %%

html = ''
for day in df['Day'].unique():
    group = df[df['Day'] == day]
    print(day)
    day_html = f'''
    <div class="header-row-cell">
      <h1>{day}</h1>
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
                <a href="{video_url}">
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
