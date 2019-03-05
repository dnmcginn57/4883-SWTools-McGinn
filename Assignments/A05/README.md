# ASCII Image Converter
## David McGinn

### Files & Font:
* input_images - contains some input images for the program
* output_images - stores output images from the program
* ascii_image.py - run from the command line, converts an image into ASCII art
* [Sushi Sushi](https://www.dafont.com/sushi-sushi.font) - my chosen font for this project. I renamed it on my machine to SushiSushi so it would be command line friendly

### Operation instructions:
run ascii_image.py from the terminal, it requires 4 arguments besides the filename <br>
```python3 ascii_image.py [input path] [output path] [font name/path] [font size]``` 
<br>For Example:
```
python3 ascii_image.py ./input_images/sock_cat.jpg ./output_images/sock_cat_ascii.png SushiSushi 6
```
<br>will run the program, converting the image `sock_cat.jpg` into `sock_cat_ascii.png` using [Sushi Sushi](https://www.dafont.com/sushi-sushi.font) font with a size of 6pt.<br>
while a path, or name of font stored in your machines `usr/share/font` folder, to any font are technically supported, 
I have configured this program to work best with the [Sushi Sushi](https://www.dafont.com/sushi-sushi.font) font mentioned above

### Other notes

I have configured this program to allow characters to overlap a bit, but not so much as to render a perfect image.
The minor overlap creates a more 'legible' picture while maintaining the feel of ascii art
<br>
<br>

![](https://raw.githubusercontent.com/dnmcginn57/4883-SWTools-McGinn/master/Assignments/A05/output_images/JCASCII.png)

