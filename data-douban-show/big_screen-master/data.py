#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site : 
# @Describe:

import json
import pandas as pd

class SourceDataDemo:


    def __init__(self):
        data = pd.read_csv(r"D:\大数据实验题目及数据\dashuju.csv")
        xx = {}
        yy = {}
        zz = {}
        for i in range(250):
            if data['score'][i] in xx:
                xx[data['score'][i]] = xx[data['score'][i]] + 1
            else:
                xx[data['score'][i]] = 1
            if data['year'][i] in yy:
                yy[data['year'][i]] = yy[data['year'][i]] + 1
            else:
                yy[data['year'][i]] = 1
            if data['year'][i] in zz:
                zz[data['year'][i]] = (zz[data['year'][i]] +float(data['score'][i]))/2
            else:
                zz[data['year'][i]] = float(data['score'][i])
        aaa = []
        ccc = []
        bbb = []
        eee = []
        ddd = []
        fff = []
        j = 0
        for i in xx:
            j = j + 1
            if j < 6:
                aaa.append({"name": i, "value": int(xx[i])})
            elif j < 11:
                ccc.append({"name":i,"value": int(xx[i])})
            else:
                bbb.append({"name":i,"value": int(xx[i])})
        print(zz,yy)
        for i in range(24):
            fff.append(str(1985+i))
            if str(1985+i) in zz:
                eee.append(yy[str(1985+i)])
                ddd.append(round(zz[str(1985+i)],1))
        self.title = '豆瓣top250大数据可视化'
        self.counter = {'name': '众望所归', 'value': 1997}
        self.counter2 = {'name': '肖申克的救赎', 'value': 9.7}
        self.echart1_data = {
            'title': '类型分布',
            'data': [
                {"name": "犯罪", "value": 17},
                {"name": "冒险", "value": 52},
                {"name": "剧情", "value": 190},
                {"name": "灾难", "value": 24},
                {"name": "战争", "value": 19},
                {"name": "悬疑", "value": 87},
                {"name": "爱情", "value": 112},
            ]
        }
        self.echart2_data = {
            'title': '地区分布',
            'data': [
                {"name": "中国", "value": 47},
                {"name": "德国", "value": 6},
                {"name": "法国", "value": 9},
                {"name": "英国", "value": 14},
                {"name": "中国香港", "value": 39},
                {"name": "日本", "value": 7},
                {"name": "美国", "value": 131},
            ]
        }
        self.echarts3_1_data = {
            'title': '高分占比',
            'data': ccc
        }
        self.echarts3_2_data = {
            'title': '中分占比',
            'data': bbb
        }
        self.echarts3_3_data = {
            'title': '低分占比',
            'data': aaa
        }
        self.echart4_data = {
            'title': '时间趋势',
            'data': [
                {"name": "年份", "value": ddd},
                {"name": "平均分", "value": eee},
            ],
            'xAxis': fff,
        }
        self.echart5_data = {
            'title': '地区占比',
            'data': [
                {"name": "中国", "value": 47},
                {"name": "德国", "value": 6},
                {"name": "法国", "value": 9},
                {"name": "英国", "value": 14},
                {"name": "中国香港", "value": 39},
                {"name": "日本", "value": 7},
                {"name": "美国", "value": 131},
            ]
        }
        self.echart6_data = {
            'title': '剧情占比',
            'data': [
                {"name": "爱情", "value": 80, "value2": 20, "color": "01", "radius": ['59%', '70%']},
                {"name": "剧情", "value": 70, "value2": 30, "color": "02", "radius": ['49%', '60%']},
                {"name": "悬疑", "value": 65, "value2": 35, "color": "03", "radius": ['39%', '50%']},
                {"name": "犯罪", "value": 60, "value2": 40, "color": "04", "radius": ['29%', '40%']},
                {"name": "灾难", "value": 50, "value2": 50, "color": "05", "radius": ['20%', '30%']},
            ]
        }
        self.map_1_data = {
            'symbolSize': 100,
            'data': [
                {'name': '巨人', 'value': 239},
                {'name': 'eva', 'value': 231},
                {'name': '钢炼', 'value': 203},
            ]
        }

    @property
    def echart1(self):
        data = self.echart1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echart2(self):
        data = self.echart2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_3(self):
        data = self.echarts3_3_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart4(self):
        data = self.echart4_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

    @property
    def echart5(self):
        data = self.echart5_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart6(self):
        data = self.echart6_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def map_1(self):
        data = self.map_1_data
        echart = {
            'symbolSize': data.get('symbolSize'),
            'data': data.get('data'),
        }
        return echart


class SourceData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        self.title = '豆瓣top250大数据可视化--长歌'

class CorpData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        with open('corp.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        self.title = data.get('title')
        self.counter = data.get('counter')
        self.counter2 = data.get('counter2')
        self.echart1_data = data.get('echart1_data')
        self.echart2_data = data.get('echart2_data')
        self.echarts3_1_data = data.get('echarts3_1_data')
        self.echarts3_2_data = data.get('echarts3_2_data')
        self.echarts3_3_data = data.get('echarts3_3_data')
        self.echart4_data = data.get('echart4_data')
        self.echart5_data = data.get('echart5_data')
        self.echart6_data = data.get('echart6_data')
        self.map_1_data = data.get('map_1_data')

class JobData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        with open('job.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        self.title = data.get('title')
        self.counter = data.get('counter')
        self.counter2 = data.get('counter2')
        self.echart1_data = data.get('echart1_data')
        self.echart2_data = data.get('echart2_data')
        self.echarts3_1_data = data.get('echarts3_1_data')
        self.echarts3_2_data = data.get('echarts3_2_data')
        self.echarts3_3_data = data.get('echarts3_3_data')
        self.echart4_data = data.get('echart4_data')
        self.echart5_data = data.get('echart5_data')
        self.echart6_data = data.get('echart6_data')
        self.map_1_data = data.get('map_1_data')