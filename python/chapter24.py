# file = open('myprogram.exe','r')
# if __name__ == '__main__':
#     process_list = []
#     for i in range(20):
#         p = Process(target=print_process, args=(i,))
#         process_list.append(p)
#     for p in process_list:
#         p.start()
# file.close

import subprocess

# Replace 'myProgram.exe' with the actual path to your executable
program_path = "./myprogram.exe"

try:
    p = subprocess.Popen(program_path)
    # Get the output of the command
    output = p.communicate()[0]

    # Print the output
    print(output)

    print("Process started successfully.")
except Exception as e:
    print("Error:", e)
