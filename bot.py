from atproto import Client

p = open("pw.txt", "r")
pw = p.read()

def main():
  client = Client()
  client.login('puppypotion.bsky.social', pw)
  client.send_post(text='livetweeting my development; ambiguating the password so i can push the bot code to my git repo. if you\'re seeing this, i did it right.')
if __name__ == '__main__':
  main()