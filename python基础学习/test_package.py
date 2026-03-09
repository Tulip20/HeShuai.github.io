# 外部直接导入wd_message包
import wd_message

# 调用包中的函数
wd_message.send()
wd_message.receive()

print("\n" + "=" * 40)
print("也可以用其他导入方式：")
print("=" * 40)

# 方式2：从包中导入特定函数
from wd_message import send, receive
send()
receive()

# 方式3：从包中的模块直接导入
from wd_message.send_message import send
from wd_message.receive_message import receive
send()
receive()
