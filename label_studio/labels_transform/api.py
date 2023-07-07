import json
from django.http import HttpResponse, JsonResponse
from .functions import base64_to_gray


# 查询
def transform_list(request):
    return JsonResponse('查询')

# 保存
def transform_add(request):
    return HttpResponse('保存')

# 更新
def transform_update(request):
    return HttpResponse('更新')

# 删除
def transform_delete(request):
    return HttpResponse('删除')

# 直接返回灰度的base64
def transform_gray(request):
        if request.method == 'POST':
            body_data = request.body.decode('utf-8')
            try:
                # 取得传递的base64
                json_data = json.loads(body_data)
                data_url = json_data['dataURL']
                [img_type, b64_str] = data_url.split(',')
                # 转换base64
                b64_gray = base64_to_gray(b64_str)
                response = {
                    'data': img_type + ',' + b64_gray
                }
                return JsonResponse(response)

            except json.JSONDecodeError:
                # 处理解析错误...
                fail_data = {
                    'msg': '图片处理失败'
                }
                return JsonResponse(fail_data)


