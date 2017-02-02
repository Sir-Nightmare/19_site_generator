# Encyclopedia

This script converts `*.md` files into html files and creates static site using Markdown converter + Jinja2 templates.
Index page with all links is generated.  
[Here](https://sir-nightmare.github.io/19_site_generator/) you can see generated site.

## Usage

- **Clone repository:** `git clone https://github.com/Sir-Nightmare/19_site_generator.git`  
- **Install necessary modules:** `pip3 install -r requirements.txt` 
- **Launch the script:** `python site_generator.py` 

By default script will generate `*.html` files from `*.md` files from `./articles/` folder using **config.json**.  
If you add new `*.md` files, you need to change **config.json** accordingly.  
All files will be stored in `./docs/` folder, which is used by GitHub Pages.  
You can change default paths in script global constants.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
