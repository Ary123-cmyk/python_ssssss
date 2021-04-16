import sys
import os
from colorama import Style, Fore, init
init(autoreset=True)
dis_rich = False
if len(sys.argv) == 1: print(Style.BRIGHT + Fore.CYAN +"Usage: {} <PATH_TO_FILE_A> <PATH_TO_FILE_B>".format(sys.argv[0]))
elif len(sys.argv) == 2: print(Style.BRIGHT + Fore.RED + "Missing one arugment: <PATH_TO_FILE_B>")
elif len(sys.argv) > 3: print(Style.BRIGHT + Fore.RED +"Too many arguements!")
else:
    file_a_pth = sys.argv[1]
    file_b_pth = sys.argv[2]
    if os.path.exists(file_a_pth) == False and os.path.exists(file_b_pth) == False:
        print(Style.BRIGHT + Fore.RED + "Could not open \"{}\" and \"{}\". This could be because they do not exist, or you do not have permissions to read and write to them.".format(file_a_pth,file_b_pth))
        raise SystemExit
    elif os.path.exists(file_a_pth) == False:
        print(Style.BRIGHT + Fore.RED + "Could not open \"{}\". This could be because it does not exist, or you do not have permissions to read and write to it.".format(file_a_pth))
        raise SystemExit
    elif os.path.exists(file_b_pth) == False:
        print(Style.BRIGHT + Fore.RED + "Could not open \"{}\". This could be because it does not exist, or you do not have permissions to read and write to it.".format(file_b_pth))
        raise SystemExit
    try:
        import rich
    except ModuleNotFoundError:
        print(Style.DIM + Fore.YELLOW+ "Module \"rich\" is not installed, text preview is disabled.")
        print(Style.DIM + Fore.YELLOW+ "Install it using \"python -m pip install rich\"")
        dis_rich = True
    file_a = open(file_a_pth, "r")
    file_b = open(file_b_pth, "r")
    a_cont = file_a.read()
    b_cont = file_b.read()
    if dis_rich == False:
        rich.inspect(a_cont, title="File A: {}".format(sys.argv[1]))
        rich.inspect(b_cont, title="File B: {}".format(sys.argv[2]))
    while True:
        conf = input("Continue? [y/n]: ")
        if conf == 'y' or conf == 'yes':
            break
        elif conf == 'n' or conf == 'no':
            print(Fore.CYAN + Style.BRIGHT + "okay, exiting!")
            raise SystemExit
        else:
            print(Style.BRIGHT + Fore.YELLOW + "Invalid option")
    file_a.close()
    file_b.close()
    file_a = open(file_a_pth, "w")
    file_b = open(file_b_pth, "w")
    file_a.write(b_cont)
    file_b.write(a_cont)
    file_a.close()
    file_b.close()
    print(Style.BRIGHT + Fore.GREEN + 'Done!')