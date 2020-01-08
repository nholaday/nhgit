navigation = {
    "Move left one character": 'h',
    "Move down one line": 'j',
    "Move up one line": 'k',
    "Move right one character": 'l',
    "Move to last line of screen": 'L',
    "Move to next word": "w",
    "Move to first line of screen": 'H',
    "Move to middle line of screen": 'M',
    "Move to beginning of line:": '0',
    "Move to end of line": '$',
    "Move to beginning of word": 'b',
    "Move to previous word": 'b',
    "Move to end of word": 'e',
    "Move to last line": "G",
    "Move to first line": "gg",
    "Page Up": "ctl-u",
    "Page Down": "ctl-d",
    "Next matching search pattern": "n",
    "Previous matching search pattern": "N",
    "til next 'X'": "tX",
    "change": "c",
    "inside": "i",
    "open file f": ":e f",
    "undo": "u",
    "redo": "ctl-r",
    "Indent": ">",
    "Set indent to 4 spaces": ":set shiftwidth=4",
    "Insert line above current line and edit": "O",
    "Insert line below current line and edit": "o",
    "Visual Block Mode": "ctl-v",
    "Goto line 77": "77G",
    "Jump to matching (, [, \"": "%",
    "Substitute 'old' with 'new', globally with confirm": ":%s/old/new/gc",
    "Run ls command": ":!ls",
}

terminal1 = {
    "resets the terminal display": "reset",
    "listing incl. hidden files": "ls -a",
    "opens hi.txt using the nano editor": "nano hi.txt",
    "run command with the security privileges of the superuser (super user do)": "sudo",
    "opens hi.txt using the vim editor": "vi hi.txt",
    "displays active processes": "top",
    "home directory": "cd ~",
    "long listing with human readable file sizes": "ls -lh",
    "list entire content of folder recursively": "ls -R",
    "change directory": "cd",
    "list storage": "ls",
    "long listing": "ls -l",
    "previous directory": "cd -",
    "clear screen": "clear",
    "change directory to root of drive": "cd /"
}

terminal2 = {
    "page through file with previous command's last arguement": "less !$", 
    "excecute previous command as super user": "sudo !!",
    "beginning of line": "ctl-a",
    "end of line": "ctl-e",
    "Find files in or under current directory that end with '.log'": "find . -name '*.log'",
    "Clear the page without using a command": "ctl-l",
    "Search file.log for all lines containing DEBUG": "grep DEBUG file.log",
    "Search hi.log for all lines matching regex '^VAV'": "grep -E '^VAV' hi.log",
    "Print all lines of hi.log NOT containing 'pizza'": "grep -v pizza hi.log",
    "Print how many lines in file hi.log": "wc -l hi.log",
    "Show processes": "top",
    "Show processes (human formatted)": "htop",
    "Print current processing statistics": "free",
    "Show input/ouput processes to hard disk": "iotop",
    "Operator to send output of one command as input for another": "|"
}

terminal3 = {
    "Search hi.log for all lines NOT ending in 'FCU'": "grep -vE 'FCU$' hi.log",
    "Print number of lines containing 'DEBUG' in hi.log": "grep DEBUG hi.log | wc -l",
    "List files (long, human readable) page-by-page and searchable": "ls -lh | less",
    "Print file for files ending in '.py'": "find . -name '*.py' | xargs cat",
    "Install htop on mac": "brew install htop",
    "Install htop on linux": "apt-get install htop",
    "Print file that shows what system wide cron jobs are running": "cat /etc/crontab",
    "Print cron table for your user": "crontab -l",
    "Edit your user's crontable": "crontab -e",
    "Run cat hi.log, if that fails run ls": "cat hi.log || ls",
    "Run cd -, if that succeeds also run ls": "cd - && ls",
    "Print file paths of excecutable commands": "echo $PATH",
    "Print the file path to the excecutable command 'python'": "which python",
    "Change permissions of script.sh to be executable": "chmod +x",
    "Change permissions of wb.py to be read/write/exec to all users": "chmod 777 wb.py",
    "Cut out everything but the 5th field delimited by ' '": "cut -d ' ' -f5",
    "Sort and and find uniques.  Count uniques": "sort | uniq -c"
}

terminal4 = {
    "Show how much free space on each disk (human readable)": "df -h",
    "Show what type of file hi.log is": "file hi.log",
    "Save the output of ls -lh to foo.txt": "ls -lh > foo.txt",
    "Append 'Fin' to the end of bar.txt": "echo Fin >> bar.txt",
    "Search and follow file.log for VAV": "tail -F file.log | grep VAV",
    "Look up running processes": "ps aux",
    "Look up running processes for user nic": "ps aux | grep nic",
    "Change directory to where all processes": "cd /proc",
    "Copy contents of bar.txt to clipboard": "cat bar.txt | pbcopy",
    "Run ls in 5 hours": "sleep 5h && ls",
    "Send 'select distinct' into smap query": "echo 'select distinct' | smap-query",
    "Print all exported environment variables": "printenv",
    "Change environment variable BACNET_IFACE to eth1": "export BACNET_IFACE=eth1",
    "Print current excecutable paths": "echo $PATH",
    "Backwards delete word": "ctl-w",
    "Delete from cursor to end of line": "ctl-k",
    "Kill to beginning of line": "ctl-u",
    "Paste killed text": "ctl-y",
    "Follow the a f.log using less": "less +F f.log",
    "Go to end of file using less": "shift-f",
    "Continue editing current shell line in an editor": "ctl-x-e",
    "cat argument from previous command": "cat !$",
}

tmux = {
    "Create new session named napkin": "tmux new -s napkin",
    "List tmux sessions": "tmux ls",
    "Attach to session named napkin": "tmux attach -t napkin",
    "Create new window": "ctl-b c",
    "Detatch from session": "ctl-b d",
    "Split window vertically": "ctl-b %",
    "Split window horizontally": "ctl-b \"",
    "Next pane": "ctl-b o",
    "Show pane numbers (and select)": "ctl-b q",
    "Kill current shell": "ctl-d",
    "Next window": "ctl-b n",
    "List windows": "ctl-b w"
}

contents = {
    'navigation': navigation, 
    'terminal1': terminal1,
    'terminal2': terminal2,
    'terminal3': terminal3,
    'terminal4': terminal4,
    'tmux': tmux
}
