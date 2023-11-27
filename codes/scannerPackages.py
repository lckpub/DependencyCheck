import re
import os
import buildDB

class Scanner:
    def __init__(self, filesPathList):
        self.filesPathList = filesPathList
        self.DBfilename = "standardDB.txt"
        # 加载数据库
        self.loadingStDB()
        
    def loadingStDB(self):
        if not os.path.exists(self.DBfilename):
            buildDB.crawler()
        with open(self.DBfilename, 'r') as f:
            content = f.read()
        self.DB = set(content.split('\n')) 
        
        for filepath in self.filesPathList:
            (direname, filename) = os.path.split(filepath)
            (file, suffix) = os.path.splitext(filename)
            self.DB.add(file)           
    
    def scanFiles(self):
        envFilePaths = []
        packageList = []
        
        for filePath in self.filesPathList:
            (dirname, filename) = os.path.split(filePath)
            (file, suffix) = os.path.splitext(filename)
            
            if suffix == '.py':
                moduleList = self.findPackage(filePath)
                packageList.extend(moduleList)
            elif 'requirements.txt' == filename or 'Pipfile.txt' == filename:
                envFilePaths.append(filePath)
        # 去重
        packageList = list(set(packageList))
        return (envFilePaths, packageList)

    def findPackage(self, filePath):
        moduleList = []
        moduleNameList = []
        
        with open(filePath, 'r', encoding="utf-8") as f:
            contents = f.readlines()
        
        annotate = False
        for line in contents:
            if "\"\"\"" in line:
                if not annotate:
                    annotate = True
                else:
                    annotate = False
                    continue
            elif "#" in line:
                continue
            if annotate:continue
            
            pattern_from = re.compile(r"(\s+from|^from)\s+(.+?)\s")
            pattern_import = re.compile(r"(\s+import|^import)\s+(.+?)[\n]")
            pattern_import_as = re.compile(r"(\s+import|^import)\s+(.+?)\sas")
            
            match_from = re.search(pattern_from, line)
            match_import = re.search(pattern_import, line)
            match_import_as = re.search(pattern_import_as, line)
            
            # print(match_from,match_import)
            if match_from != None:
                rex = match_from.group(2)
                rex = rex.replace(" ", '')
                moduleNameList.append(rex.split('.')[0])
                
            elif match_import_as != None:
                rex = match_import_as.group(2)
                rex = rex.replace(" ", '')
                moduleNameList.append(rex.split('.')[0])
                
            elif match_import != None:
                rex = match_import.group(2)
                rex = rex.replace(" ", '')
                temp = [s.split('.')[0] for s in rex.split(',')]
                moduleNameList.extend(temp)
        
        moduleNameList = set(moduleNameList)
        for moduleName in moduleNameList:
            if moduleName not in self.DB:
                moduleList.append(moduleName)
        return moduleList


if __name__ == "__main__":
    # 这里仅用于生成所有文件的地址进行测试
    files_path = []
    for filepath, dirnames, filenames in os.walk(r'D:\study_notebook\作品赛\SJTU'):
        for filename in filenames:
            path = os.path.join(filepath, filename)
            files_path.append(path)       
    # print(files_path)
    ###################################################################################
    
    # 该类的建立如下：
    # 给定所有文件的地址
    scanner = Scanner(files_path)
    # 返回的第一项是requirements.txt和pipfile.txt的地址
    # 第二项是所有的第三库
    (downloadEnvPath, moduleNameList) = scanner.scanFiles()
    print(moduleNameList)