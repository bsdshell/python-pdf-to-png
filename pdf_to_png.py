#!/usr/local/bin/python3

from PyPDF2 import PdfFileWriter, PdfFileReader
import AronLib as a

# KEY: split pdf to page, pdf page, split pdf file, pdf to png
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
def extractPage0PDF(pathPDF, randdir, isOverridedPNG):
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
                
                if a.fileExist(fpath) is False or isOverridedPNG:
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


def getWWWPDFDir():
    www = a.getEnv('www')
    pdfPath = a.join(www, 'pdf')
    return pdfPath

def deleteTmpRandomDir(randdir):
    cmd = 'rm -rf ' + randdir
    a.run(cmd)

def extractPage0PDFCheck(pdfDir, randdir):
    isOverridedPNG = False
    overpng = input('Override old png (file-0.png) files Under:' + pdfDir + '\n ENTER: yes\n')
    if overpng == 'yes':
        isOverridedPNG = True
    else:
        print('NOT override png file:' + pdfDir + '\n')
    extractPage0PDF(pdfDir, randdir, isOverridedPNG)

# --------------------------------------------------------------------
# Main here
# Use following in live App.
# NOTE: pdfDir = getWWWPDFDir()
# Input pdf file
def Main():
    # pdfDir='/Users/aaa/try/dirxx1'
    pdfDir = getWWWPDFDir()
    print(pdfDir)
    a.pp("")
    input_pdfDir = input('\tWhere are your PDF files?\n\tCurrent location => Contain PDF files: ' + a.getPWD() + ' ENTER: yes\n' + '\tOtherwise Default: ' + pdfDir + '\n')
    a.pp("\t")
    
    if input_pdfDir == 'yes':
        pdfDir = a.getPWD()
    else:
        print('Use Default Location: ' + pdfDir)
    
    # Output png file
    randdir = '/tmp/randomdirxx'

    beg = a.nowSecond()
    extractPage0PDFCheck(pdfDir, randdir)

    # Use shell command: convert => convert pdf to png file
    # new png file: file.pdf => file-0.png
    ls = pdfToPng(randdir)

    # copy newly png file back to pdfDir
    copyPNGTo(randdir, pdfDir)

    end = a.nowSecond()

    print('Total Time =' + a.toStr(end - beg) + ' seconds')

    str = input('Delete ' + randdir + ' Enter: yes\n' )
    if str == 'yes':
        deleteTmpRandomDir(randdir)
        print('Delete ' + randdir)
    else:
        print('Do not delete ' + randdir + '\n')

    # mycmd='rm -rf /tmp/randomdirxx'
    # a.run(mycmd)

Main()
