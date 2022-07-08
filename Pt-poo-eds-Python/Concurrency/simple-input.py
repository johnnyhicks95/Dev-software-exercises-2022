from threading import Thread

"""
This example runs two threads. Can you see them? Every program has one thread, 
called the main thread. The code that executes from the beginning is happening in 
this thread. The second thread, more obviously, exists as the InputReader class.

"""
class InputReader(Thread):
    def run(self):
        self.line_of_text = input()

print("Ënter some text and press enter: ")
thread = InputReader()
thread.start()

count = result = 1
while thread.is_alive():
    result = count * count
    count += 1

print("calculated squares up to {0}*{0}={1}".format(count, result))
print( "while you typed '{}'".format(thread.line_text) )


