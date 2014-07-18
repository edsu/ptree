# -*- coding: utf-8 -*-

# Thanks to John Kunze of the California Digital Library for the unit tests
# in his CPAN module, which these were lifted from.
# http://search.cpan.org/~jak/File-Pairtree-0.28/

from unittest import TestCase

from ptree import id2ptree, ptree2id

class PairTreeTests(TestCase):

    i2ptree_tests = (
        ('abc', u'/ab/c/', 'basic 3-char case'),
        ('abcd', '/ab/cd/', 'basic 4-char case'),
        ('abcdefg', '/ab/cd/ef/g/', 'basic 7-char case'),
        ('abcde', '\\ab\\cd\\e\\', '5-char with \\ separator', '\\'),
        ('xy', '/xy/', '2-char edge case'),
        ('z', '/z/', '1-char edge case'),
        ('', '//', '0-char edge case'),
        ('abcdefg', '/ab/cd/ef/g/', '7-char, empty separator case', ''),
        ('12-986xy4', '/12/-9/86/xy/4/', 'hyphen'),
        ('13030_45xqv_793842495', '/13/03/0_/45/xq/v_/79/38/42/49/5/', 'long id with undescores'),
        ('ark:/13030/xt12t3', '/ar/k+/=1/30/30/=x/t1/2t/3/', 'colons and slashes'),
        ('/', '/=/', '1-separator-char edge case'),
        ('http://n2t.info/urn:nbn:se:kb:repos-1', '/ht/tp/+=/=n/2t/,i/nf/o=/ur/n+/nb/n+/se/+k/b+/re/po/s-/1/', 'a URL with colons, slashes, and periods'),
        ('what-the-*@?#!^!?', '/wh/at/-t/he/-^/2a/@^/3f/#!/^5/e!/^3/f/', 'weird chars from spec example'),
        ('\\"*+,<=>?^|', '/^5/c^/22/^2/a^/2b/^2/c^/3c/^3/d^/3e/^3/f^/5e/^7/c/', 'all weird visible chars'),
        ('Années de Pèlerinage', '/An/n^/c3/^a/9e/s^/20/de/^2/0P/^c/3^/a8/le/ri/na/ge/', 'UTF-8 chars'),
        ('2014SPIE.9158E..04Z', '20/14/SP/IE/,9/15/8E/,,/04/Z/', 'I want a relative path', None, True)
    )

    # TODO: ptree2id should support all these tests
    ptree2id_tests = (
        ('/ab/cd/', 'abcd', 'basic 4-char path'),
        ('/ab/cd/e/', 'abcde', 'basic 5-char path'),
        ('ab/cd/e', 'abcde', 'missing terminal separators'),
        ('/ab/cd/e/f/gh/', 'abcde', '1-char shorty ends ppath'),
        ('///ab///cd///e///////', 'abcde', 'lots of bunched separators'),
        ('  //ab///cd///e///  ', 'abcde', 'whitespace in front and in back'),
        ('pairtree_root/ab/cd/e/obj', 'abcde', 'junk before and after path'),
        ('pairtree_root/ab/c/d/ef', 'abc', 'junk after one-char component terminates ppath'),
        ('pairtree_root/a=/c+/e,/obj', 'a/c:e.', 'junk with weird chars'),
        ('/home/jak/pairtree_root/ab/cd/e/data/obj', 'abcde', 'bigger junk before and after path'),
        #('/home/jak/pairtree_root/ab/cd/e/data/obj/pairtree_root/gh/ij', 'ghij', 'ppath followed by a ppath picks last one'),
    )

    def test_id2ptree(self):
        for case in self.i2ptree_tests:
            if len(case) == 3:
                result = id2ptree(case[0])
            elif len(case) == 4: # uses custom separator
                result = id2ptree(case[0], sep=case[3])
            elif len(case) == 5: # uses abspath bool option
                result = id2ptree(case[0], relpath=case[4])
            msg = "%s: id2ptree(%s) = %s but got %s" % \
                    (case[2], case[0], case[1], result)
            self.assertEqual(result, case[1], msg=msg)

    def test_ptree2id(self):
        for case in self.ptree2id_tests:
            result = ptree2id(case[0])
            msg = "%s: ptree2id(%s) = %s but got %s" % \
                    (case[2], case[0], case[1], result)
            self.assertEqual(result, case[1], msg=msg)
