# HOW TO USE
* Change follwoing inside `Main`

``` python
pdfDir='/path/to/pdffile'
		
# Output png file
randdir = '/tmp/randomdirxx'
```
* run your code

``` bash
	pdf-to-png
```

*
## Split PDF file to pages
## Convert first page of PDF file to PNG file
### Use command tool

``` python
	cmd='convert -density 192 ' + fname + ' -quality 100 -alpha remove ' + pngName
```

### Add code delete tmpdir
### Add flag to check whether to override png file

