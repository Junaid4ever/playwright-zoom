!wget -O setup.py "https://www.dropbox.com/scl/fi/a6fzybdfet7bomw0h4tvg/setup.py?rlkey=uozdj43mq3bxtwzmm1qoi5nb8&st=lrvzq4n9&dl=0"
import sys

sys.path.append("setup")

from setup import install_dependencies

# Execute the function to install dependencies
install_dependencies()
