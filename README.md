# Transformations

run the main file 

args python mainfile [/path/of/folder/where/the/images/are] [/path/of/folder/where/new/data/to/be/stored]

example:
python mainfile.py /home/mo/vwfs_test/small/img/ /home/mo/vwfs_test/new_data/

This will save 3 versions of the original image.
1: Rotation with 3 degree of skewness
2: Random amplification of colors
3: Affine transformations (scaling, flipping, translations)

All images are resized to 256x256

The dimensions are taken from Jonathan's work "Learning Features and Parts for Fine-Grained Recognition"

