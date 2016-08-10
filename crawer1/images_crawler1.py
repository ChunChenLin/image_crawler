from __future__ import print_function


import lxml.html
import requests

a = raw_input("Please enter an URL of the sample images page:")

#a = 'http://www.photographyblog.com/reviews/canon_eos_7d_mark_ii_review/sample_images/'
b = requests.get(a)
assert b.status_code == 200
c = lxml.html.fromstring(b.content)
for d in c.xpath('//a[text() = "Download Original"]/@href'):
    print('Download:', d)
    e = requests.get(d, headers={'Referer': a})
    assert e.status_code == 200
    assert not d.endswith('/')
    f = d.rsplit('/')[-1]
    with open(f, 'wb') as g:
        print(g.write(e.content), 'bytes')