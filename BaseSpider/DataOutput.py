#coding:utf-8
import codecs,chardet

class DataOutput(object):

    def __init__(self):
        self.datas=[]
    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout=codecs.open('baike2.html','w',encoding='utf-8')
        fout.write("<html>")
        fout.write("<head><meta charset='utf-8'/></head>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url'])
            # print(chardet.detect(data['url']))
            fout.write("<td>%s</td>"%data['title'])
            fout.write("<td>%s</td>"%data['summary'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
