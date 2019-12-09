import logging

# 创建一个日志对象
logg = logging.getLogger("测试日志")
# 定义一个模板
FORMATTER = logging.Formatter("%(asctime)s - %(name)s - [%(lineno)d] - %(message)s")

# 创建一个屏幕流
p_stream = logging.StreamHandler()
# 创建一个文件流
f_stream = logging.FileHandler("log.log", mode="a", encoding="utf-8")

# 将流绑定到模板
p_stream.setFormatter(FORMATTER)
f_stream.setFormatter(FORMATTER)

# 将日志和流进行绑定
logg.addHandler(p_stream)
logg.addHandler(f_stream)

# 设置日志记录等级
logg.setLevel(logging.DEBUG)

# 打印日志信息
logg.debug("this is Debug")
logg.info("this is info")
logg.warning("this is warning")
logg.error("this is error")
logg.critical("this is critical")