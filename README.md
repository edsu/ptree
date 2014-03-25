ptree
=====

[PairTree] [1] is an technique from the digital preservation community for 
safely mapping identifiers to file paths, and back again. It can be helpful 
when writing resources to disk so that they can be identified later on by 
merely looking at the filesystem layout.

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

ptree draws from Ben O'Steen's [PairTree Python module] [2], which provides a 
lot more functionality for storing bitstreams on disk. ptree intentionally
focuses soley on the identifier/filepath mapping, and leaves IO operations up 
to you. The unit tests were shamlessly stolen from John Kunze's 
[File::PairTree] [3]. 

License
-------

* CC0

[1]: https://confluence.ucop.edu/display/Curation/PairTree
[2]: http://pypi.python.org/pypi/Pairtree
[3]: http://search.cpan.org/dist/Pairtree/
