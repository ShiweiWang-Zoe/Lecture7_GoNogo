##go no go

#Hi, I’m trying to adapt a GO/NOGO protocol from Price et al., 2016. Food-specific response inhibition,
#dietary restraint and snack intake in lean and overweight/obese adults.
#The task consists in 50 trials (40 go and 10 no-go). During go trials the 
#subject should press a key as fast as possible. During no-go trials, no key should be pressed. 
#Each trial is composed by an image presented for 750ms and was separated by a blank screen for 500 ms 
#and preceded by a fixation cross for 500 ms. The sequence of go/nogo stimuli are predetermined. 
#Two set of images are used: 10 go images (each one is presented 4 times) and 10 no-go images 
#(each one is presented one time). Image order should be randomized across subjects.
# we are going to change for anorexia nervosa intervention

import pandas as pd
from psychopy.gui import DlgFromDict
from psychopy.visual import Window, TextStim, ImageStim, Rect, TextBox, DotStim
from psychopy.core import Clock, quit, wait
from psychopy.event import Mouse
from psychopy.hardware.keyboard import Keyboard
from psychopy import event, data
import random
from psychopy.visual import Circle

exp_info = {'participant_nr': '', 'age': '21'}
dlg = DlgFromDict(exp_info)

p_name= exp_info['participant_nr']

# Initialize a fullscreen window with my monitor (HD format) size
# and my monitor specification called "samsung" from the monitor center
#win = Window(size=(1200, 800), fullscr=False)
win = Window(size=(1200, 800), fullscr=False, color='black', units='pix')

# Also initialize a mouse, although we're not going to use it
mouse = Mouse(visible=False)

#initialize a visual cue
go_circle = Circle(
    win,
    radius=40,
    fillColor='green',
    lineColor='green',
    pos=(0, 250),
    units='pix'
)

go_text = TextStim(
    win,
    text='GO',
    color='white',
    height=30,
    pos=(0, 250),
    units='pix'
)

nogo_circle = Circle(
    win,
    radius=50,
    fillColor='red',
    lineColor='red',
    pos=(0, 250),
    units='pix'
)

nogo_text = TextStim(
    win,
    text='NO GO',
    color='white',
    height=24,
    pos=(0, 250),
    units='pix'
)



# Initialize a (global) clock
clock = Clock()
#f_list = f"/Users/emilylloyd/Downloads/Food-Choice-Task-MRI git/lists/HF_LF_60.csv"
f_list = r"D:/AAA programming for psychology/HF_LF_60.csv"
foods = pd.read_csv(f_list)
hf = foods[foods['fat']==1]
lf = foods[foods['fat']==0]
lf = lf.sample(frac=0.4)
hf = hf.sample(frac=0.4)
trial_foods=pd.concat([lf,lf,lf,hf])
trial_foods = trial_foods.sample(frac=1)
kb=Keyboard()

instructions = TextStim(
    win,
    text=(
        "Welcome to the Go/No-Go task.\n\n"
        "Press the SPACE bar as quickly as possible when you see a GO cue (a green circle that says Go).\n"
        "Do NOT press anything when you see a NO GO cue (a red circle that says No GO).\n\n"
        "Press SPACE to preceed to the experiment."
    ),
    color='white',
    height=28,
    wrapWidth=900
)

instructions.draw()
win.flip()

while True:
    keys = kb.getKeys(['space', 'escape'], waitRelease=False)
    if keys:
        if keys[0].name == 'escape':
            win.close()
            quit()
        elif keys[0].name == 'space':
            break


for i in range(0,len(trial_foods)):
    trial=trial_foods.iloc[i]
    print(trial)
    t=TextStim(win,"+")
    t.draw()
    win.flip()
    wait(0.5)
    #path = "/Users/emilylloyd/Downloads/Food-Choice-Task-MRI git/stimuli/" + trial.food
    path = "D:/AAA programming for psychology/Food-Choice-Task-main/stimuli/" + trial.food
    print(trial.fat)
    if trial.fat==1:
        correct = "nogo"

    else: 
        correct = "go"

    im=ImageStim(win, path)
    
    
    
    
    t_clock=Clock()
    response = "nogo"
    rt="NA"
    while t_clock.getTime() < .75:
        im.draw()
        if correct == "go":
            go_circle.draw()
            go_text.draw()
        else:
            nogo_circle.draw()
            nogo_text.draw()
        win.flip()
        keys = kb.getKeys(['space','escape'], waitRelease=False)
        if keys:
            resp = keys[0].name
            rt = keys[0].rt
            if resp == 'escape':
                win.close()
                quit()
            else:
                response = "go"

    win.flip()
    wait(.5)
#    trial_foods['response']=response
#    trial_foods['rt']= rt
#    trial_foods['correct_response']= correct
    trial_foods.loc[i, 'response'] = response
    trial_foods.loc[i, 'rt'] = rt
    trial_foods.loc[i, 'correct_response'] = correct


## tasks
# 1. figure out what is happening in the task & add instructions
#Participants need to inhibit from pressing the key if trial.fat==1 (if they dont press, they response will be correct)
#Participants need to press the key if trial.fat==0 (if they  press, they response will be correct)

# 2. we need to add go-nogo! How would we do that?

    
