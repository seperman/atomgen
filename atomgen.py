import xml.etree.cElementTree as ET
import datetime
# import pdb  

class AtomGen(object):
    """
    Creates Atomfeed 1.2 from a list of dictionaries
    """

    def __init__(self, **kwargs):

        self.id = kwargs.pop('id', 'id')
        self.updated_key = kwargs.pop('updated', 'updated')
        self.published_key = kwargs.pop('published', 'published')
        self.end_date = kwargs.pop('end_date', 'end_date')
        self.summary = kwargs.pop('summary', 'summary')
        self.img_source = kwargs.pop('SOURCE', 'SOURCE')


    def run(self, infeed, update_time=datetime.datetime.utcnow()):

        # pdb.set_trace()   
        update_time_formatted = update_time.strftime('%Y-%m-%dT%H:%M:%SZ')

        feed = ET.Element('feed')
        feed.set("xmlns","http://www.w3.org/2005/Atom")
        feed.set("xmlns:news","http://itunes.apple.com/2011/Newsstand")
        updated = ET.SubElement(feed, 'updated')
        updated.text=update_time_formatted

        for item in infeed:
            entry = ET.SubElement(feed, 'entry')
            entry_id = ET.SubElement(entry, 'id')
            entry_id.text = str(item[self.id])

            if self.updated_key in item:
                entry_updated = ET.SubElement(entry, 'updated')
                entry_updated.text = item[self.updated_key].strftime('%Y-%m-%dT%H:%M:%SZ')

            if self.published_key in item:
                entry_published = ET.SubElement(entry, 'published')
                entry_published.text = item[self.published_key].strftime('%Y-%m-%dT%H:%M:%SZ')

            if self.end_date in item:
                entry_end_date = ET.SubElement(entry, 'news:end_date')
                entry_end_date.text = item[self.end_date].strftime('%Y-%m-%dT%H:%M:%SZ')

            if self.summary in item:
                entry_summary = ET.SubElement(entry, 'summary')
                entry_summary.text = str(item[self.summary])

            if self.img_source in item:
                icons = ET.SubElement(entry, 'news:cover_art_icons')
                icon_source = ET.SubElement(icons, 'news:cover_art_icon')
                icon_source.set("size","SOURCE")
                icon_source.set("src",item[self.img_source])


        print ET.tostring(feed, encoding="UTF-8", method="xml")



if __name__ == "__main__":
    import doctest
    doctest.testfile("doctest.txt")

