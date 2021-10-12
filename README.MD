# Split PDF file to pages
# Convert first page of PDF file to PNG file
## Use command tool

``` python
	cmd='convert -density 192 ' + fname + ' -quality 100 -alpha remove ' + pngName
```

