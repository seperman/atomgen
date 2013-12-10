##atomgen v 0.1.3
=======

Creates Apple Newsstand Atom Feed that is compatible with v1.2 of Atom Feed

*Author: Erasmose*
* [Github](https://github.com/erasmose)
* [Linkedin](http://www.linkedin.com/in/sepehr)


##Installation

Install from PyPi::

    pip install atomgen

##Example usage
    

    >>> import datetime
    >>> from atomgen import AtomGen
    >>> my_atom = AtomGen()
    >>> a=[{'id':'1','updated':datetime.datetime(2013, 12, 10, 1, 9, 53, 977342),'published':datetime.datetime(2013, 12, 10, 1, 10, 53, 977342),'summary':"This is the summary 1",'icon':"http://ccc.com/img.png"},{'id':2,'updated':datetime.datetime(2013, 12, 9, 1, 9, 53, 977342),'published':datetime.datetime(2013, 12, 10, 1, 7, 53, 977342),'summary':"This is the summary 2",'icon':"http://ccc2.com/img2.png"}]
    >>> print my_atom.run(a, update_time=datetime.datetime(2013, 12, 10, 1, 9, 53, 977342))
        <?xml version='1.0' encoding='UTF-8'?>
        <feed xmlns="http://www.w3.org/2005/Atom" xmlns:news="http://itunes.apple.com/2011/Newsstand"><updated>2013-12-10T01:09:53Z</updated><entry><id>1</id><updated>2013-12-10T01:09:53Z</updated><published>2013-12-10T01:10:53Z</published><summary>This is the summary 1</summary><news:cover_art_icons><news:cover_art_icon size="SOURCE" src="http://ccc.com/img.png" /></news:cover_art_icons></entry><entry><id>2</id><updated>2013-12-09T01:09:53Z</updated><published>2013-12-10T01:07:53Z</published><summary>This is the summary 2</summary><news:cover_art_icons><news:cover_art_icon size="SOURCE" src="http://ccc2.com/img2.png" /></news:cover_art_icons></entry></feed>

or by redefining some element names in the original dictionary:

    >>> b=[{'my_id':'1','when_updated':datetime.datetime(2013, 12, 10, 1, 9, 53, 977342),'when_published':datetime.datetime(2013, 12, 10, 1, 10, 53, 977342),'the_summary':"This is the summary 1",'myicon':"http://ccc.com/img.png"},{'my_id':2,'when_updated':datetime.datetime(2013, 12, 9, 1, 9, 53, 977342),'when_published':datetime.datetime(2013, 12, 10, 1, 7, 53, 977342),'the_summary':"This is the summary 2",'myicon':"http://ccc2.com/img2.png"}]
    >>> my_atom2 = AtomGen(id="my_id",published="when_published",updated="when_updated",summary="the_summary",icon="myicon")
    >>> print my_atom2.run(b, update_time=datetime.datetime(2013, 12, 10, 1, 9, 53, 977342))
    <?xml version='1.0' encoding='UTF-8'?>
    <feed xmlns="http://www.w3.org/2005/Atom" xmlns:news="http://itunes.apple.com/2011/Newsstand"><updated>2013-12-10T01:09:53Z</updated><entry><id>1</id><updated>2013-12-10T01:09:53Z</updated><published>2013-12-10T01:10:53Z</published><summary>This is the summary 1</summary><news:cover_art_icons><news:cover_art_icon size="SOURCE" src="http://ccc.com/img.png" /></news:cover_art_icons></entry><entry><id>2</id><updated>2013-12-09T01:09:53Z</updated><published>2013-12-10T01:07:53Z</published><summary>This is the summary 2</summary><news:cover_art_icons><news:cover_art_icon size="SOURCE" src="http://ccc2.com/img2.png" /></news:cover_art_icons></entry></feed>


          
This will generate exactly the same Atom feed. But it gives you the flexibility of modifying your own dictionary keys with the names you like.

##Documents

* [Documentations](http://atomgen.readthedocs.org/en/latest/)
