# 设施选址问题 Facility Location

## 目的和先决条件

在此示例中，我们将解决设施位置问题，即我们要建立仓库以供应一定数量的超级市场。我们将构建此问题的混合整数编程（MIP）模型，在Gurobi Python界面中实现此模型，并计算最佳解决方案。

该建模示例处于初级阶段，我们假设你了解 Python，并且具有一些有关构建数学优化模型的知识。

**注意：** 你可以通过单击 [此处](https://github.com/arvinxx/gurobi-and-mathematical-modeling/archive/master.zip) 下载包含此示例和其他示例的代码。为了正确运行此 Jupyter Notebook，您必须具有 Gurobi 许可证。如果您没有，则可以**商业用户身份**申请 [试用许可证](https://www.gurobi.com/downloads/request-an-evaluation-license/)，或以**学术用户身份**下载 [免费许可证](https://www.gurobi.com/academia/academic-program-and-licenses)。


## 动机

设施选址问题的研究（也称为位置分析）是运筹学和计算几何学的一个分支，与设施的最佳布置有关，以最大程度地降低运输成本，同时考虑避免在房屋附近放置危险材料以及竞争对手设施的位置等因素。

费马-韦伯问题（Fermat-Weber Problem）是17世纪提出的最早的设施选址问题之一。

费马-韦伯问题可以描述如下：

> 给定一个平面中的三个点，找到第四个点，使得其到三个给定点的距离之和最小。

该问题可以解释为设施位置问题的一种形式，其中假设所有目的地的每距离运输成本都相同。

设施选址问题在许多行业都有应用。对于供应链管理和物流，该问题可用于寻找商店、工厂、仓库等的最佳位置。其他应用范围包括公共政策（例如在城市中安置警察）、电信（例如网络中的蜂窝塔），甚至还有粒子物理学（例如，排斥电荷之间的分离距离）。设施选址问题的另一个应用是确定天然气输送设备的位置。最后，设施选址问题可应用于聚类分析。


## 问题描述

英国的一家大型连锁超市需要为其在英格兰北部开设的一系列超市建立仓库。超级市场的位置已经确定，但是仓库的位置尚未确定。

目前已经确定了若干仓库的备选地点，但必须就建立多少个仓库以及在哪些候选地点建立仓库作出决定。

建设多个仓库是有好处的，因为这将减少卡车从仓库到超市的平均行驶距离，从而降低运输成本。但是，建一个仓库有一定的固定成本。

在这个例子中，我们的目标是找到运输成本和建造新仓库成本之间的最佳权衡。


## 拟议的解决方案

设施选址问题的混合整数规划（MIP）模型。

## 查看网页版

本案例也包含了一个网页版本 如果你没有 Jupter Notebook  的话，可以直接查看网页版来学习。➡️ [传送门](https://arvinxx.github.io/gurobi-official-examples/facility-location)

## 协议

你可以通过单击 [此处](https://github.com/arvinxx/gurobi-and-mathematical-modeling/archive/master.zip) 下载包含此示例和其他示例的代码。为了正确运行此 Jupyter Notebook，你必须具有 Gurobi 许可证。如果你没有，则可以**商业用户身份**申请 [试用许可证](https://www.gurobi.com/downloads/request-an-evaluation-license/)，或以**学术用户身份**下载 [免费许可证](https://www.gurobi.com/academia/academic-program-and-licenses)。

Copyright © 2020 Gurobi Optimization, LLC

翻译 By Arvin Xu