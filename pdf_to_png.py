#!/usr/local/bin/python3

from PyPDF2 import PdfFileWriter, PdfFileReader
import AronLib as a

# KEY: split pdf to page, pdf page, split pdf file
# inputpdf = PdfFileReader(open("/tmp/b.pdf", "rb"))

tryx = '/Library/WebServer/Documents/xfido'
pdfpath = tryx + '/pdf'  # /Library/WebServer/Documents/xfido/pdf
fname = ".pdf"
ls = a.readDirRecurveList(pdfpath, fname);
a.pre (ls)
print ("len=" + a.toStr(len(ls)))




# NOTE: ONLY generate the first page "-0.png" from PDF file
# for fn in ls:
#     print('fn=' + fn);
#     xname = fn
#     inputpdf = PdfFileReader(open(xname, "rb"), strict=False)
#     name = a.dropExt(a.takeName (xname))
#     a.sleep(0)
#     for i in range(inputpdf.numPages):
#         output = PdfFileWriter()
#         output.addPage(inputpdf.getPage(i))
#         # output: /Library/WebServer/Documents/xfido/pdf/firstpage
# 
#         fpath = pdfpath + '/firstpage/' + name + "-0.png"
#         if a.fileExist(fpath) is False:
#             with open(pdfpath + '/firstpage/' + name + "-%s.pdf" % i, "wb") as outputStream:
#                 output.write(outputStream)
#         else:
#             a.pre('file Exist=' + fpath)
#         break   # ONLY the first page


def extractPage0PDF(pathPDF, randdir):
    fname = ".pdf"
    ls = a.readDirRecurveList(pathPDF, fname);
    ran = a.rand(1000, 100000)
    a.run('rm -rf ' + randdir)
    a.run('mkdir ' + randdir)
    if a.dirExist(randdir):
        for pdffile in ls:
            print('pdfile=' + pdffile);
            inputpdf = PdfFileReader(open(pdffile, "rb"), strict=False)
            name = a.dropExt(a.takeName (pdffile))
            a.sleep(0)
            for i in range(inputpdf.numPages):
                output = PdfFileWriter()
                output.addPage(inputpdf.getPage(i))

                fpath = pathPDF + '/' + name + "-0.png"
                a.pp('fpath=' + fpath)
                a.pp('randdir=' + randdir)
                if a.fileExist(fpath) is False:
                    with open(randdir + '/' + name + "-%s.pdf" % i, "wb") as outputStream:
                        output.write(outputStream)
                else:
                    a.pre('file Exist=' + fpath)
                break   # ONLY the first page

            
def replaceExt(fname, newExt):
    return a.dropExt(fname) + newExt

def pdfToPng(randdir):
    ls = a.lsDir(randdir, ".pdf")
    for fname in ls:
        pngName = replaceExt(fname, '.png')
        cmd='convert -density 192 ' + fname + ' -quality 100 -alpha remove ' + pngName
        a.run(cmd)
        print(fname + '=>' + pngName)
    return ls            

def copyPNGTo(randdir, wwwDir):
    cmd='cp -f ' + a.join(randdir, '*.png') + ' ' + wwwDir
    a.run(cmd)
    
pdfDir='/Users/aaa/try/dirxx1'
randdir = '/tmp/randomdirxx'

extractPage0PDF(pdfDir, randdir)

ls = pdfToPng(randdir)

copyPNGTo(randdir, '/Users/aaa/try/dirxx2')
