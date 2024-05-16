# ------------------------------------
# name:          RequestData
# Description:
# Author:        liuyong   Administrator
# Date:          2023/8/1 0001  6:59
# ------------------------------------
from django.http import HttpRequest
from bangyi.service.Untils.Tools import writelog

class RequestData:
    def __init__(self, request: HttpRequest):
        self.request = request

    def getRequestParam(self, paramName, default="{}"):
        paramVal = self.request.GET.get(paramName, None)
        if paramVal == None:
            paramVal = self.request.POST.get(paramName, None)
        if paramVal == None:
            paramVal = self.request.COOKIES.get(paramName, None)
        if paramVal == None:
            return default
        else:
            writelog(paramName + "=" + paramVal)
            return paramVal

    def getParams(self):
        return self.getRequestParam("params", "{}")

    def getGuid(self):
        return self.getRequestParam("guid", "")

    def getNose(self):
        return self.getRequestParam("nose", "")

    def getFile(self, fileName):
        return self.request.FILES.get(fileName, None)

    def getFull_Info(self):
        return self.request.get_full_path()

