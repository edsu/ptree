ptree
=====

[![Build Status](https://secure.travis-ci.org/edsu/ptree.png)](http://travis-ci.org/edsu/ptree)

[PairTree] is a technique from the digital preservation community for 
safely mapping identifiers to file paths, and back again. It can be helpful 
when writing resources to disk so that they can be identified later on by 
merely looking at the file system layout.

The ptree module has two functions to help you work with PairTree identifiers 
and file paths: `id2ptree` and `ptree2id`. 

```python
>>> import ptree
>>> ptree.id2ptree("info:lccn/12345678")
'/in/fo/+l/cc/n=/12/34/56/78/'
>>> ptree.ptree2id('/in/fo/+l/cc/n=/12/34/56/78/')
u'info:lccn/12345678'
```

Thanks
------

ptree draws from [Ben O'Steen's] PairTree Python module, which provides a 
lot more functionality for storing bitstreams on disk. For better or worse
ptree focuses solely on the identifier/path mapping, and leaves IO operations 
up to you. The unit tests were shamelessly stolen from John Kunze's 
[File::PairTree]. 

License
-------

* CC0

[PairTree]: https://confluence.ucop.edu/display/Curation/PairTree
[Ben O'Steen's]: http://pypi.python.org/pypi/Pairtree
[File::PairTree]: http://search.cpan.org/dist/File-Pairtree/lib/File/Pairtree.pm
