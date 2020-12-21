# 信号塔覆盖

等级：入门

## 目的和先决条件

在此示例中，我们将解决一个简单的覆盖问题：如何构建一个信号塔网络以提供信号覆盖给尽可能多的人。我们将构建业务问题的数学模型，然后实施 在Gurobi Python界面中进行建模，并计算最佳解决方案。

这个建模案例处在初学者级别，我们假设您了解 Python 并且您已经掌握一些知识关于建立数学优化模型。

## Motivation

Over the last ten years, smartphones have revolutionized our lives in ways that go well beyond how we communicate.
Besides calling, texting, and emailing, more than two billion people around the world now use these devices to navigate,
to book cab rides, to compare product reviews and prices, to follow the news, to watch movies, to listen to music, to
play video games,to take photographs, to participate in social media, and for numerous other applications.

A cellular network is a network of handheld smartphones in which each phone communicates with the telephone network by
radio waves through a local antenna at a cellular base station (cell tower). One important problem is the placement of
cell towers to provide signal coverage to the largest number of people.

## Problem Description

A telecom company needs to build a set of cell towers to provide signal coverage for the inhabitants of a given city. A
number of potential locations where the towers could be built have been identified. The towers have a fixed range, and
-due to budget constraints- only a limited number of them can be built. Given these restrictions, the company wishes to
provide coverage to the largest percentage of the population possible

## Proposed Solution

A mixed-integer programming (MIP) formulation for the Cell Tower Coverage Problem..

## Licensing

In order to run this Jupyter Notebook properly, you must have a valid Gurobi license. If you do not have one, you can
request
an [evaluation license](https://www.gurobi.com/downloads/request-an-evaluation-license/?utm_source=Github&utm_medium=website_JupyterME&utm_campaign=CommercialDataScience)
as a *commercial user*, or download
a [free license](https://www.gurobi.com/academia/academic-program-and-licenses/?utm_source=Github&utm_medium=website_JupyterME&utm_campaign=AcademicDataScience)
as an *academic user*.

## HTML Example URL

https://gurobi.github.io/modeling-examples/cell_tower_coverage/cell_tower.html

Copyright © 2020 Gurobi Optimization, LLC
