import base64
from PIL import Image
from io import BytesIO


# 将base64进行灰度处理并返回base64
def base64_to_gray(base64_string):
    # 解码 base64 字符串为字节数据
    image_data = base64.b64decode(base64_string)

    # 创建 BytesIO 对象并读取图像数据
    image_buffer = BytesIO(image_data)
    image = Image.open(image_buffer)

    # 将图像转换为灰度模式
    gray_image = image.convert('L')

    # 将灰度图像保存为字节数据
    buffered = BytesIO()
    gray_image.save(buffered, format="PNG")
    encoded_string = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return encoded_string