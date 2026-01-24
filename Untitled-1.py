text = "Hello @user1, check out @project-update for details!"
mentions = [word.strip(",.!") for word in text.split() if word.startswith('@')]