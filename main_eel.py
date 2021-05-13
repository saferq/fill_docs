import eel
import os
import random

# Set web files folder and optionally specify which file types to check for eel.expose()
#   *Default allowed_extensions are: ['.js', '.html', '.txt', '.htm', '.xhtml']
eel.init('frontend')


@eel.expose
def pick_file(folder):
    if os.path.isdir(folder):
        item = random.choice(os.listdir(folder))
        print(f'file: {item}')
        return item
    else:
        return 'Not valid folder'


# Start (this blocks and enters loop)
eel.start('main.html', mode='chrome', size=(450, 450))
