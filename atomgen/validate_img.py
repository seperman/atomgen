from __future__ import print_function, division
import imghdr
import urllib2 as urllib
import io
from PIL import Image

validated_images = {}


class AtomIncompatibleImageType(Exception):
    """
    Exception raised when the Atom image is not PNG
    """
    pass



class AtomIncompatibleImageSize(Exception):
    """
    Exception raised when the Atom image is not the proper size or ratio
    """
    pass


class AtomImageHTTPError(Exception):
    """
    Exception raised when the Atom image can not be accessed 
    """
    pass


def check_img(img):
    """
    checks a local image for Apple Newsstand feed specifications v1.2
    """
    if imghdr.what(img) != "png":
        raise AtomIncompatibleImageType("image needs to be of PNG type")

    img_obj = Image.open(img)
    x,y = img_obj.size

    if max(x,y) < 1024:
        raise AtomIncompatibleImageSize("image's biggest side has to be at least 1024px")

    aspect_ratio = x/y

    if aspect_ratio > 2 or aspect_ratio < 0.5:
        raise AtomIncompatibleImageSize("image's aspect ratio has to be between .5 and 2 ")


    return True


def _fetch_img(img_url):
    try:
        fd = urllib.urlopen(img_url)
        return io.BytesIO(fd.read())
    except urllib.HTTPError:
        raise AtomImageHTTPError("%s can't be accessed" % img_url)
    return False


def validate_img_on_web(img_url):
    """
    checks a remote image for existance and Apple Newsstand feed specifications v1.2
    example:
    
    >>> from atomgen.validate_img import validate_img_on_web
    >>> validate_img_on_web("http://cdn.tennis.com/uploads/magazine/test_material/img_1200_500.png")
    """
    if img_url in validated_images:
        return
    else:
        img = _fetch_img(img_url)
        if img:
            if check_img(img):
                validated_images[img_url]=True
                print ("%s validated" % img_url)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
