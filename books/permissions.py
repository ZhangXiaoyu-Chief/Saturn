from rest_framework import permissions


class CheckPermissionToAction(permissions.BasePermission):
    """
    自定义权限，需要重写has_permission或has_object_permission方法
    has_object_permission在has_permission通过之后手动通过调用
    self.check_object_permissions(self.request, book)触发
    """
    message = '你没有执行此操作的权限'  # 检查不通过是返回的消息字符串

    def has_object_permission(self, request, view, obj):
        """
        检查对象权限
        :param request: 
        :param view: 
        :param obj: 要检查的对象，也就是model的实例
        :return: 
        """
        print("object:", obj)
        return True

    def has_permission(self, request, view):
        """
        检查视图权限函数
        :param request: 
        :param view: 视图对象
        :return: 
        """
        print("view args:", view.args)
        print("view name:", view.get_view_name())
        return True
