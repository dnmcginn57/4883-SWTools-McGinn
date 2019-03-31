# Image Mosaic
## 4-1-19
## David McGinn

## Files
  * `mosaic.py` - creates a mosaic image
  * `dominant.py` - creates a JSON with image paths associated with their dominant RGB __MUST BE RUN FIRST__
  
## Instructions

Before `mosaic.py` can be run, `dominant.py` MUST run to create a JSON for `mosaic.py` to use.<br>
to run `dominant.py` use the command line with a command like `python3 dominant.py [path]` where `[path]` is a folder full of images.<br>
once `dominant.py` has successfully generated a json, `mosaic.py` is ready to go <br><br>

`mosaic.py` expects a command with arguments like this `python3 mosaic.py [input_file=] [output_folder=] [SubImagesSize=]` <br>
`output_folder=` field is optional, if it is left out the program will just rename the file and place it in `./`<br>
__Example__ `python3 mosaic.py input_file=./input_images/duck.jpeg output_folder=./output_images/duck_of_birds.png SubImageSize=16`
<br>this command will create a mosaic, with 16x16 images, of `duck.jpeg` and place it in `output_images` under a new name `duck_of_birds.png`

## Notes:

* `dominant.py` was necessary to cut down on processing time by making dominant color searches a one-time ordeal.

<br><br><br>
![](https://raw.githubusercontent.com/dnmcginn57/4883-SWTools-McGinn/master/Assignments/A08/output_images/JC_mosaic.png)
