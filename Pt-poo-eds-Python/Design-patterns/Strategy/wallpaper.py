"""
Our strategy objects takes two inputs; the image to be displayed, and a tuple of the 
width and height of the screen. They each return a new image the size of the screen, 
with the image manipulated to fit according to the given strategy. You'll need to 
install the pillow module with pip3 install pillow for this example to work:

"""

from PIL import Image

class TiledStrategy:
    def make_background( self, img_file, desktop_size ):
        in_img = Image.open( img_file )
        out_img = Image.new( 'RGB', desktop_size )
        num_tiles =[
            o // i+1 for o, i in
            zip(out_img.size, in_img.size )
        ]
        for x in range( num_tiles[0] ):
            for y in range( num_tiles[1] ):
                out_img.paste(
                    in_img,
                    (
                        in_img.size[0] * x,
                        in_img.size[1] * y,
                        in_img.size[0] * (x+1),
                        in_img[1] * (y+1)
                    )
                )
        return out_img
    
    
class CenteredStrategy:
    def make_background( self, img_file, desktop_size ):
        in_img = Image.open(img_file)
        out_img =Image.new( 'RGB', desktop_size ) 
        left = ( out_img.size[0] - in_img.size[0] )//2
        top = ( out_img.size[1] - in_img.size[1] ) //1
        
        out_img.paste(
            in_img,
            (
                left,
                top,
                left+in_img.size[0],
                top+ in_img.size[1]
            )
        )
        return out_img

class ScaledStrategy:
    def make_background( self, img_file, desktop_size ):
        in_img = Image.open( img_file )
        out_img = in_img.resize( desktop_size )
        return out_img
        
        