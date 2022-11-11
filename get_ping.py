import ping3
import sys
ping3.EXCEPTIONS = True
host = sys.argv[1]
if len(sys.argv) > 2 :
    number = int(sys.argv[2])
else:
    number = 3
f = open("ping.txt", "a")
print("Started pinging address:", host)
f.write("Started pinging address: "+ host+"\n")
results = []
for i in range(number):
    try:
        result= int(ping3.ping(host, timeout=1, size= 56)*1000)
        result = (f"64 bytes from {host}: time={result}ms\n")
        print(result)
        results.append(result)
        f.write(result)
    except ping3.errors.Timeout as e:
        print(str(e))
    except Exception as e:
        print(str(e))
        exit()

loss = round((number - len(results))/number * 100, 2)
final_result= f"{len(results)} received and {number - len(results)} lost. packet loss: {loss}\n"
print(final_result)
f.write(final_result+"=================================================\n")

