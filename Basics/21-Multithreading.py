import threading

def print_numbers():
    for i in range(1, 6):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
print("Threat completed!")

#Python allows running multiple tasks at the same time using threads.

#It makes programs faster when dealing with I/O operations (e.g., file reading, network requests).