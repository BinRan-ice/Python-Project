# coding:utf-8
#xpath是在xml文档中搜索内容的一门语言
#html是xml的一个子集
from lxml import etree

xml="""
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷若</nick>
        <nick class="joy">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>惹了1</nick>
        </div>
        <span>
            <nick>惹了2</nick>
            <div>
            <nick>惹了3</nick>
            </div>
        </span>
    </author>

    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
"""
tree=etree.XML(xml)
#result=tree.xpath("/book") #/表示层级关系，第一个/是根节点
#result=tree.xpath("/book/name/text()")  #text()拿文本
result=tree.xpath("/book/author//nick/text()")  #所有符合条件的结点 后代结点
#result=tree.xpath("/book/author/*/nick/text()") #*通配符，任意的节点
#result=tree.xpath("/book//nick/text()")
print(result)