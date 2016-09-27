**contextlib模块**
---
说明：contextlib是为了加强with语句，提供上下文机制的模块，它是通过Generator实现的。通过定义类以及写__enter__和__exit__来进行上下文管理;
contextlib中有nested和closing，前者用于创建嵌套的上下文，后则用于帮你执行定义好的close函数
