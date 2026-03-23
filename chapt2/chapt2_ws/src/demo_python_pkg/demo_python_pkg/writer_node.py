import rclpy
from demo_python_pkg.person_node import PersonNode

class WriterNode(PersonNode):
    def __init__(self, node_name: str,name: str, age: int, book: str) -> None:
        super().__init__(node_name, name, age)
        print('WriterNode 的 __init__ 函数被调用了')
        self.book = book

def main():
    # Initialize ROS 2
    rclpy.init()

    node = WriterNode('writer_node','法外狂徒张三', 18, '论快速入狱')
    node.eat('鱼香肉丝')

     #Clean up
    node.destroy_node()
    rclpy.shutdown()
