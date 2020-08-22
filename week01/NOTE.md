学习笔记
1.折腾一下午终于搞清楚了获取文本的方式
 for atag_type in tags.find_all('span', attrs={'class':'hover-tag'}):
        film_hover.append(atag_type.next_element.next_element)
       