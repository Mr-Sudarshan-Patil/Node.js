import os
from datetime import datetime, timedelta
from random import randint

if not os.path.exists('.git'):
    os.system('git init')

start_date = datetime(2024, 2, 12)
end_date = datetime(2024, 4, 14)

current_date = start_date
while current_date <= end_date:
    num_commits = randint(1, 10)
    for _ in range(num_commits):
        commit_date = current_date + timedelta(hours=randint(0, 23), minutes=randint(0, 59), seconds=randint(0, 59))
        commit_date_str = commit_date.strftime('%a %b %d %H:%M:%S %Y %z')
        with open('file.txt', 'a') as file:
            file.write(commit_date_str + '\n')
        os.system('git add .')
        os.system(f'git commit --date="{commit_date_str}" -m "commit"')
    current_date += timedelta(days=1)

if os.system('git remote -v') == 0:
    os.system('git push -u origin main')
