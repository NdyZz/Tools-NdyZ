import socket
import re
import time,os,random,sys
from datetime import datetime
import requests
import json
from collections import deque
from bs4 import BeautifulSoup
import urllib.parse
import colored
from colored import fg
from rich import print as cetak
from rich.panel import Panel as panel
from rich.console import Console
from rich.columns import Columns
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

console = Console()
banAU = []
ac = []

red = fg('light_red')
blue = fg('light_blue')
yellow = fg('light_yellow')
green = fg('light_green')
white = fg('white')
cyan = fg('cyan')

def banner_scanIp():
  cetak(panel(f"""[bold purple]
[[[[[[]]]]]] [[[[[[]]]]]]     [[[[]]]]     [[[[]]]]    [[]]
[[]]         [[]]            [[]]  [[]]    [[]] [[]]   [[]]
[[[[[[]]]]]] [[]]           [[]]    [[]]   [[]]  [[]]  [[]]
        [[]] [[]]          [[[[[[[]]]]]]]  [[]]   [[]] [[]]
[[[[[[]]]]]] [[[[[[]]]]]] [[]]        [[]] [[]]    [[[[]]]]\n\n[bold red][!] use the exit command to quit[bold white]\n[bold red][!] use the menu command to menu[bold white]
""",width=100,padding=(0,18),title=f"[bold cyan]Port Scanner",style=f"bold purple"))

def banner_checkIp():
  cetak(panel(f"""[bold purple]
[[[[[]]]]] [[]]    [[]] [[[[[[]]]]]] [[[[[]]]]] [[]]    [[]]   [[]] [[[[[[]]]]]]
[[]]       [[]]    [[]] [[]]         [[]]       [[]]  [[]]     [[]] [[]]    [[]]
[[]]       [[[[[[]]]]]] [[[[[[]]]]]] [[]]       [[[[]]]]       [[]] [[[[[[]]]]]]
[[]]       [[]]    [[]] [[]]         [[]]       [[]]  [[]]     [[]] [[]]
[[[[[]]]]] [[]]    [[]] [[[[[[]]]]]] [[[[[]]]]] [[]]    [[]]   [[]] [[]]\n\n[bold red][!] use the exit command to quit[bold white]\n[bold red][!] use the menu command to menu[bold white]
""",width=100,padding=(0,8),title=f"[bold cyan]Check Ip",style=f"bold purple"))

def banner_scraper():
  cetak(panel(f"""[bold purple]
[[[[[]]]]] [[[[[]]]]] [[[[[[]]]]]]     [[[[]]]]     [[[[[[]]]]]] [[[[[]]]]] [[[[[[]]]]]]
[[]]       [[]]       [[]]    [[]]    [[]]  [[]]    [[]]    [[]] [[]]       [[]]    [[]]
[[[[[]]]]] [[]]       [[[[[[]]]]]]   [[]]    [[]]   [[[[[[]]]]]] [[[[[]]]]] [[[[[[]]]]]]
      [[]] [[]]       [[]]  [[]]    [[[[[[[]]]]]]]  [[]]         [[]]       [[]]  [[]]
[[[[[]]]]] [[[[[]]]]] [[]]    [[]] [[]]        [[]] [[]]         [[[[[]]]]] [[]]    [[]]\n\n[bold red][!] use the exit command to quit[bold white]\n[bold red][!] use the menu command to menu[bold white]
""",width=100,padding=(0,5),title=f"[bold cyan]Email Scraper",style=f"bold purple"))
  
def banner(co, my_ip, day):
  file_path = open('/sdcard/.name.txt','r').read()
  name_user, join = file_path.split(',')
  banAU.append(panel(f"""[bold ppurple]
 __    _            ______
|  \  | |    _ __  |___  |____
|   \ | | __| |\ \/ / / /___  |
| |\ \| |/    | \  / / /   / /
| | \   | (_| |_/ / / /___/ /___
|_|  \__|\____|__/ /_____|_____|
\n[bold green][+] Author  : [bold red]NdyZ\n[bold green][+] Contact : [bold red]085346923840\n[bold green][+] Github  : [bold red]https://github.com/NdyZz\n[bold green][+] Date    : [bold red]{day}[bold purple]
        """,width=50,padding=(0,5),title=f"[bold cyan] Version 1.0",style=f"bold purple"))
  banAU.append(panel(f"""[bold ppurple]
 __    _            ______
|  \  | |    _ __  |___  |____
|   \ | | __| |\ \/ / / /___  |
| |\ \| |/    | \  / / /   / /
| | \   | (_| |_/ / / /___/ /___
|_|  \__|\____|__/ /_____|_____|
\n[bold green][+] Name    : [bold red]{name_user}\n[bold green][+] Country : [bold red]{co}\n[bold green][+] My Ip   : [bold red]{my_ip}\n[bold green][+] Join    : [bold red]{join}[bold purple]
        """,width=50,padding=(0,6),title=f"[bold cyan] Profile User",style=f"bold purple"))
  console.print(Columns(banAU))
  
def scan(ipaddress, port, timeouts):
    try:
        soc = socket.socket()
        soc.settimeout(timeouts)
        soc.connect((ipaddress, port))
        service = soc.recv(1024)
        service = service.decode('utf-8')
        service = service.strip('\n')
        print(green + f'Port {str(port)} open {service}')
    except ConnectionRefusedError:
        print(yellow + f'Port {str(port)} closed')
    except UnicodeDecodeError:
        print(red + f'port {str(port)} closed')
    except KeyboardInterrupt:
        sys.exit(red+'\n[!] Cancel'+white)
    except OSError:
        sys.exit(red+'\n[!] Connection Error'+white)
    except:
        sys.exit(red+'\n[!] Error'+white)
    
def scan_domain(hostname):
    ipaddress = socket.gethostbyname(hostname)
    req_url = 'https://geolocation-db.com/jsonp/' + ipaddress
    response = requests.get(req_url)
    geolocation = response.content.decode()
    geolocation = geolocation.split("(")[1].strip(")")
    geolocation = json.loads(geolocation)
          
    print(red+'\n', '='*40)
    print(green + f"'domain name : {hostname}'")
    for k, v in geolocation.items():
      print(green + f"{str(k)} : {str(v)}")
      print(red+'='*40)

def validate_ip_address(ipaddress):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(pattern, ipaddress):
        return True
    else:
        return False

def validate_port(port):
    try:
        port = int(port)
        if 0 <= port <= 65535:
            return True
        else:
            return False
    except ValueError:
        return False

def validate_timeout(timeouts):
  try:
        timeouts = int(timeouts)
        if 1 <= timeouts <= 5:
            return True
        else:
            return False
  except ValueError:
        return False

def port_scanner():
  while True:
    try:
      os.system('clear')
      banner_scanIp()
      
      target = input(cyan+'╰─ ' + blue + 'Target: '+white)
      if target in('menu','Menu','MENU','m','M'):
        banAU.clear()
        main()
      elif target in('exit','Exit','EXIT','ex','Ex','EX'):
        sys.exit(red+'\n[!] Exit'+white)
      else:
        pass
      
      if not validate_ip_address(target):
          print(red + '[!] Alamat IP tidak valid')
          time.sleep(2)
          continue
      
      ports = input(cyan+'╰─ ' + blue + 'Port: '+white)
      
      timeouts = input(cyan+'╰─ ' + blue + 'Time Out: '+white)
      if not validate_timeout(timeouts):
          print(red + '[!] Error[timeout(1-5)]')
          time.sleep(2)
          continue
      
      if ',' in ports:
          portlist = ports.split(',')
          for port in portlist:
              if not validate_port(port):
                  print(red + f'[!] Port tidak valid: {port}')
                  continue
              scan(target, int(port), int(timeouts))
      elif '-' in ports:
          portrange = ports.split('-')
          start = portrange[0]
          end = portrange[1]
          if not validate_port(start) or not validate_port(end):
              print(red + '[!] Port tidak valid')
              time.sleep(2)
              continue
          for port in range(int(start), int(end)+1):
              scan(target, port, int(timeouts))
      elif ports == 'all':
        for port in range(1, 65535+1):
          scan(target, port, int(timeouts))
      else:
          if not validate_port(ports):
              print(red + '[!] Port tidak valid')
              time.sleep(2)
              continue
          scan(target, int(ports), int(timeouts))
      cip = input(cyan+'╰─ ' + blue + 'Menu(y/n)'+white)
      if cip in('menu','Menu','MENU','m','M','y','Y'):
        banAU.clear()
        main()
      elif cip in('exit','Exit','EXIT','ex','Ex','EX'):
        sys.exit(red+'\n[!] Exit'+white)
      else:
        pass
    except KeyboardInterrupt:
      sys.exit(red+'\n[!] Cancel'+white)
    except:
      sys.exit(red+'\n[!] Error'+white)

def check_ip():
  while True:
    try:
      os.system('clear')
      banner_checkIp()
      hostname = input(cyan+'╰─ ' + blue+'domain name: '+white)
      
      if hostname in('menu','Menu','m','M'):
        banAU.clear()
        main()
      elif hostname in('exit','Exit','quit','Quit','ex'):
        sys.exit(red+'\n[!] Exit'+white)
      else:
        pass
      
      if ',' in hostname:
        host = hostname.split(',')
        for hostname in host:
          scan_domain(hostname)
      else:
        scan_domain(hostname)
        
      cip = input(cyan+'╰─ ' + blue + 'Menu(y/n)'+white)
      if cip in('menu','Menu','MENU','m','M','y','Y'):
        banAU.clear()
        main()
      elif cip in('exit','Exit','EXIT','ex','Ex','EX'):
        sys.exit(red+'\n[!] Exit'+white)
      else:
        pass
    except socket.gaierror:
      print(red+'[!] Domain Error')
      time.sleep(.8)
    except requests.exceptions.ConnectionError:
      sys.exit(red+'\n[!] Connection Error'+white)
    except KeyboardInterrupt:
      sys.exit(red+'\n[!] Exit'+white)
    
def email_scraper():
    while True:
      try:
        os.system('clear')
        banner_scraper()
        user_url = str(input(cyan+'╰─ ' + blue+'URL: '+white))
        if user_url in('menu','Menu','m','M'):
          banAU.clear()
          main()
        elif user_url in('exit','Exit','ex','Ex','quit','Quit'):
          sys.exit(red+'\n[!] Exit'+white)
        else:
          pass
        urls = deque([user_url])
        scraped_urls = set()
        emails = set()
        count = 0
        limit = int(input(cyan+'╰─ ' + blue+'limit: '+white))
        
        try:
          while True:
            count += 1
            if count > limit:
              break
            
            if urls:
              url = urls.popleft()
            else:
              print(red+"\n[!] List is empty!")
              break
              
            scraped_urls.add(url)
            parts = urllib.parse.urlsplit(url)
            base_url = f'{parts.scheme}://{parts.netloc}'
            path = url[:url.rfind('/')+1] if '/' in parts.path else url
            
            print(green+'['+white+f'{count}'+green+']'+green+' processing'+ blue+' => '+red+f'{url}')
            
            try:
              response = requests.get(url)
            except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
              continue
        
            new_emails = set(re.findall(r'[a-z0-9\.\-+_]+@\w+\.+[a-z\.]+', response.text, re.I))
            emails.update(new_emails)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            for anchor in soup.find_all('a'):
              link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
              if link.startswith('/'):
                link = base_url + link
              elif not link.startswith('http') or link.startswith('https'):
                link = path + link
              if not link in urls and not link is scraped_urls:
                urls.append(link)
            
        except KeyboardInterrupt:
          print(red+'[-] Closing')
          
        print(green+'\n[!] proccess done\n')
        print(cyan+f'{len(emails)}'+yellow+' emails \n','='*40)
        for mail in emails:
          print('  '+mail)
        print('\n')
        cin = input(cyan+'╰─ ' + blue + 'Save(y/n): '+white)
        if cin in('y','Y'):
          named = datetime.now().strftime("%d-%b-%Y %H:%M")
          with open(f'outputNdyZz/{named}', 'w') as f:
            for mail in emails:
              f.write(str(mail))
          banAU.clear()
          main()
        elif cin in('n','N'):
          banAU.clear()
          main()
        elif cin in('exit','Exit','EXIT','ex','Ex','EX'):
          sys.exit(red+'\n[!] Exit'+white)
        else:
          pass
      except ValueError:
        pass

def login():
  if not os.path.isfile('/sdcard/.name.txt'):
    name_user = input(cyan+'╰─ ' + yellow+' your name '+red+'(ENTER to skip) : '+white)
    join = datetime.now().strftime("%d-%b-%Y %H:%M")
    with open('/sdcard/.name.txt', 'w') as f:
      if name_user == '':
        ac.append('n')
        f.write(f'-,-')
        name_user = 'Login'
        load_load(name_user)
      else:
        ac.append('y')
        f.write(f'{name_user},{join}')
        name_user = f'Login as {name_user}'
        load_load(name_user)
  else:
    file_path = open('/sdcard/.name.txt','r').read()
    name_user, join = file_path.split(',')
    if name_user == '-':
      ac.append('n')
      name_user = 'Login'
      load_load(name_user)
      pass
    else:
      ac.append('y')
      name_user = f'Login as {name_user}'
      load_load(name_user)
      pass

def load_load(name_user):
  try:
    progress = Progress(TextColumn(f'[cyan]{name_user}'),SpinnerColumn('point'),)
    task = progress.add_task("",total=20)
    
    with progress:
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(0.1)
  except KeyboardInterrupt:
    sys.exit(red+'\n[!] Cancel'+white)
    
def main():
  os.system('clear')
  while True:
    os.system('clear')
    day = datetime.now().strftime("%d-%b-%Y %H:%M")
    tex = ['pilih yang bener asu','pilih yang bener ngntd','pilih yang bener ajg']
    if 'y' in ac:
      try:
        os.system('clear')
        co = requests.get("http://ip-api.com/json/").json()["country"]
        my_ip = requests.get("http://ip-api.com/json/").json()["query"]
        banner(co, my_ip, day)
      except requests.exceptions.ConnectionError:
        sys.exit(red+'\n[!] Connection Error'+white)
      except:
        sys.exit(red+'\n[!] Error'+white)
    elif 'n' in ac:
      try:
        os.system('clear')
        co = '-'
        my_ip = '-'
        banner(co, my_ip, day)
      except requests.exceptions.ConnectionError:
        sys.exit(red+'\n[!] Connection Error'+white)
      except:
        sys.exit(red+'\n[!] Error'+white)
        
    cetak(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Check IP[bold white] [/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Port Scanner[bold white]\n[bold white][[bold cyan]03[/][bold white]][/] [bold white]Email Scraper[bold white]\n[bold white][[bold cyan]04[/][bold white]][/] [bold white]Update Tools[bold white]\n[bold white][[bold cyan]05[/][bold white]][/] [bold white]Logout[bold white]\n\n[bold red][+] use the exit command to quit[bold white]',width=40,title=f"[bold cyan]Menu",style=f"bold purple"))
    
    input_menu = input(cyan+'╰─ ' + white+'Opsi : ')
    if input_menu in('1','01'):
      check_ip()
    elif input_menu in('2','02'):
      port_scanner()
    elif input_menu in('3','03'):
      email_scraper()
    elif input_menu in('exit','quit'):
      sys.exit(red+'\n[!] Exit'+white)
    elif input_menu in('4','04'):
      os.system('python .update.py')
      exit()
    elif input_menu in('5','05'):
      os.system('rm /sdcard/.name.txt')
      sys.exit(red+'\n[!] Logout'+white)
    else:
      print(red + f'[!] {random.choice(tex)}')
      time.sleep(1)
      banAU.clear()
      
class basa_basi():
  try:os.mkdir('outputNdyZz')
  except:pass
  try:os.system('clear')
  except:pass
  cetak(panel(f" [bold white][+] Hallo Cuy Gw [bold red]NdyZ [bold white]Dan Gw harap anda tidak recode sc ini \n [+] Dan Semua Pengguna Termux. Semoga Kalian makin pro wkwkwk \n [+] Beribu-Ribu Kali Mohon Maaf jika ingin recode silahkan izin sama author, oke..?\n [+] Jangan Lupa Juga Cuy [bold red]donasi[bold white] Untuk Gw Yakan Awokawok \n [bold white][+][bold green] Dana : [bold red]085346923840 \n [bold white][+][bold green] Pulsa : [bold red]085346923840 \n [bold white][+] Thanks To All",width=100,padding=(0,2),title=f"[bold cyan]Basa-Basi",style=f"bold purple"))
  login()
  time.sleep(1)
  main()
  
if __name__=='__main__':
  basa_basi()
