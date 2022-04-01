import os

while True:
    output = os.popen('./birdDetection').read()
    print(output)
    if output=="1":
        print("bird detected")
        
    else:
        print("no Birds")
