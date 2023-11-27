from collections import deque
import networkx as nx 
import matplotlib.pyplot as plt

graph = {
    'mit': ['bsd-simplified', 'bsd-new','bsd-original'],
    'zpl-2.0': ['apache-2.0'],
    'zlib': ['apache-2.0'],
    'ibpng': ['apache-2.0'],
    'bsd-simplified': ['bsd-new','bsd-original'],
    'bsd-new': ['epl-1.0','epl-2.0',"mpl-1.1","mpl-2.0",'mulanpsl-2.0','bsd-original'],
    'bsd-original': ['epl-1.0','epl-2.0',"mpl-1.1","mpl-2.0",'mulanpsl-2.0','bsd-new'],
    'mulanpsl-2.0': ['apache-2.0'],
    "apache-2.0":["lgpl-3.0","lgpl-3.0-plus"],
    "epl-1.0":[],
    "epl-2.0":[],
    "mpl-1.1":[],
    "mpl-2.0":["lgpl-2.1-plus"],
    "lgpl-2.1":["gpl-2.0"],
    "lgpl-2.1-plus":["lgpl-2.1","lgpl-3.0","lgpl-3.0-plus"],
    "lgpl-3.0":["gpl-3.0","gpl-3.0-plus","mulanpubl-2.0"],
    "lgpl-3.0-plus":["gpl-3.0","gpl-3.0-plus","mulanpubl-2.0"],
    "gpl-2.0":[],
    "gpl-2.1-plus":["gpl-3.0","gpl-3.0-plus"],
    "gpl-3.0":["agpl-3.0","agpl-3.0-plus"],
    "gpl-3.0-plus":["agpl-3.0","agpl-3.0-plus"],
    "mulanpubl-2.0":["agpl-3.0","agpl-3.0-plus"],
    "agpl-1.0-plus":["agpl-3.0","agpl-3.0-plus"],
    "agpl-3.0":[],
    "agpl-3.0-plus":[]
}


def find_path(graph, start, end, path=[]):
    path = path + [start]  # 路径，每一次递归调用时，把当前结点加入已经访问的集合中去
    # print("path:%s" % path)
    if start == end:
        return path
    if start not in graph:  # 仅存在此节点 不作为弧头出现，仅作为弧尾[数据结构唐朔飞]
        return "unknown"  # 递归结束的条件
    if end not in graph:  # 仅存在此节点 不作为弧头出现，仅作为弧尾[数据结构唐朔飞]
        return "unknown"  # 递归结束的条件
    # print("graph[{}]:{}".format(start, graph[start]))
    for node in graph[start]:  # 依次访问start的邻接顶点node
        if node not in path:  # 同一节点在返回的路径上不会出现多次
            # print("node:{}".format(node))
            newpath = find_path(graph, node, end, path)  # 递归调用时传入参数path
            # print("newpath:{}".format(newpath))
            # newpath=False
            if newpath:
                # print("if--newpath:{}".format(newpath))
                return newpath  # 找到一条路径便结束循环
    return None

def compatibility(license1, license2):
    tmp_graph = graph
    if license2 == "mpl-2.0":
        tmp_graph["apache-2.0"].append("mpl-2.0")
        tmp_graph["mpl-1.1"].append("mpl-2.0")
    elif license2 == "epl-2.0":
        tmp_graph["epl-1.0"].append("epl-2.0")
    
    return find_path(tmp_graph, license1, license2)

# 封装函数
# 参数 license_list，长度为n
# list中第一个元素是项目许可证key（字符串类型），后面n-1个元素是各个包的许可证key
# 返回值为长度为n-1的列表，代表这项目许可证和包许可证是否有冲突
# 返回值的元素若为None，说明【有冲突】
# 返回值元素作为"unknown"，说明许可证超出了图的范围，暂时无法检测
# 返回值是一个列表路径，代表兼容没问题
def project_compliance(project_license,license_list):
    if len(license_list)<=0:
        return None
    res = []
    for i in range(len(license_list)):
        tmp = compatibility(license_list[i], project_license)
        res.append(tmp)
    return res

if __name__ == '__main__':
    print(project_compliance("mpl-2.0",[ "gpl-2.0","apache-2.0","bsd-new","ok"]))
    print(compatibility("mit","gpl-2.0"))
    H = nx.DiGraph(graph) 
    nx.draw_circular(H, with_labels=True, font_weight='bold')
    plt.show()