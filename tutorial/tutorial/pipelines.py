# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time


class TutorialPipeline(object):
    def open_spider(self, spider):
        self.file = open("douban.txt", "w",encoding='utf-8')
        self.num = 0

    def process_item(self, item, spider):
        self.num += 1
        # content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        titles = item['title']
        movieInfo = item['movieInfo']
        content = titles+':'+movieInfo +'\n'
        self.file.write(content)
        # with open('cnblog.txt', 'w', encoding='utf-8') as f:
        #     titles = item['title']
        #     movieInfo = item['movieInfo']
        #     for i, j in zip(titles, movieInfo):
        #         f.write(i + ':' + j + '\n')
        print(item["title"]+'--'+item['movieInfo']+'--'+item['star']+'--'+item['quote'])
        # time.sleep(3)
        return item

    def close_spider(self, spider):
        print('一共保存了' + str(self.num) + '条数据')
        # self.file.close()
