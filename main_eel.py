import eel

# Set web files folder and optionally specify which file types to check for eel.expose()
#   *Default allowed_extensions are: ['.js', '.html', '.txt', '.htm', '.xhtml']
eel.init('frontend')


@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print(f'py - say_hello_py: {x}')


say_hello_py('Python World!')
eel.say_hello_js('Python World!')   # Call a Javascript function

# Start (this blocks and enters loop)
eel.start('main.html', mode='chrome', size=(450, 450))
