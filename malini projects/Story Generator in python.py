import random

when = ['Yesterday', 'In the future', 'In a parallel universe', 'Last summer', 'On New Year\'s Eve']
who = ['a space explorer', 'a wizard', 'a robot', 'a mermaid', 'a superhero']
name = ['Zara', 'Orion', 'Quasar', 'Nixie', 'Blaze']
residence = ['Mars', 'Atlantis', 'Cyber City', 'Enchanted Forest', 'Sky Haven']
went = ['space station', 'magic academy', 'digital realm', 'enchanted garden', 'celestial observatory']
happened = ['discovered a new galaxy', 'cast a spell on a dragon', 'solved a digital puzzle', 'found a hidden treasure', 'saved the universe']

print(random.choice(when) + ', ' + random.choice(who) + ' named ' + random.choice(name) + ' that lived in ' +
      random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))

