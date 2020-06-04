### **Installation**
1. `sudo apt-get install direnv`
2. `echo 'eval "$(direnv hook bash)"' >> ~/.bashrc`
3. `cp .env.example .env`
4. ln -s \`pwd\`/.env \`pwd\`/.envrc
5. `mkvirtualenv -p /usr/bin/python3.6 <env-name>`(optional)
6. `pip install -r requirements.txt
7. `mkdir logs`