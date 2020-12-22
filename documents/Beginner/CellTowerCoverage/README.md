# 信号塔覆盖

等级：入门

## 目的和先决条件

在此示例中，我们将解决一个简单的覆盖问题：如何构建一个信号塔网络以提供信号覆盖给尽可能多的人。我们将构建业务问题的数学模型，然后实施 在Gurobi Python界面中进行建模，并计算最佳解决方案。

这个建模案例处在初学者级别，我们假设您了解 Python 并且您已经掌握一些知识关于建立数学优化模型。

## 动机

在过去的十年里，智能手机彻底改变了我们的生活，远远超出了我们的沟通方式。除了打电话,发短信,发邮件,现在全世界有超过二十亿人使用这些设备导航到书出租车,比较产品评论和价格,遵循新闻,看电影,听音乐,玩游戏,拍照,参与社交媒体,和许多其他应用程序。

蜂窝网络是一种手持式智能手机网络，其中每部手机通过蜂窝基站(蜂窝基站)的本地天线通过无线电波与电话网络进行通信。一个重要的问题是如何安置手机信号塔，以便向最多的人提供信号覆盖。

## Problem Description

A telecom company needs to build a set of cell towers to provide signal coverage for the inhabitants of a given city. A
number of potential locations where the towers could be built have been identified. The towers have a fixed range, and
-due to budget constraints- only a limited number of them can be built. Given these restrictions, the company wishes to
provide coverage to the largest percentage of the population possible

## Proposed Solution

A mixed-integer programming (MIP) formulation for the Cell Tower Coverage Problem..



## 协议

你可以通过单击 [此处](https://github.com/arvinxx/gurobi-and-mathematical-modeling/archive/master.zip) 下载包含此示例和其他示例的代码。为了正确运行此 Jupyter Notebook，你必须具有 Gurobi 许可证。如果你没有，则可以**商业用户身份**申请 [试用许可证](https://www.gurobi.com/downloads/request-an-evaluation-license/)，或以**学术用户身份**下载 [免费许可证](https://www.gurobi.com/academia/academic-program-and-licenses)。
## 查看网页版

本案例也包含了一个网页版本 如果你没有 Jupter Notebook  的话，可以直接查看网页版来学习。➡️ [传送门](https://arvinxx.github.io/gurobi-official-examples/cell-tower-coverage)

Copyright © 2020 Gurobi Optimization, LLC

翻译 By Arvin Xu