import os,sys,time,random
from colored import fg,bg
import time,random
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

red = fg('light_red')
blue = fg('light_blue')
white = fg('white')
green = fg('light_green')
yellow = fg('light_yellow')
cyan = fg('cyan')
red_bg = bg('light_red')

def loads_load():
  try:
    style_loads = random.choice(['clock','point','moon','earth'])
    spinner = SpinnerColumn(spinner_name=style_loads)
    
    progress = Progress(spinner,"[progress.description]{task.description}",BarColumn(),"[progress.percentage]{task.percentage:>3.0f}%",)
    
    task = progress.add_task("[cyan]Update", total=100)
    
    with progress:
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(random.choice([0.1,0.2,0.05,0.5]))
          
  except KeyboardInterrupt:
    print('[+] canceled')
    exit()

sansZ = """
cd ..
cd Tools-NdyZ
"""
loads_load()
os.system(sansZ)
print(green+' [+] Update Script success'+cyan)
os.system('cat .update.txt')
print(green+red_bg+' [!] use the '+ blue+'python NdyZz.py'+ green+' to run tool'+white)
time.sleep(.3)
os.sys.exit()