#1
import re
txt = "a ab abbb"
print(re.findall(r"ab*", txt))

#2
import re
txt = "a ab abbb"
print(re.findall(r"ab{2,3}", txt))

#3
import re
text = "hello_world test_case Hello_World"
x = r"[a-z]+_[a-z]+"
print(re.findall(x, text))

#4
import re
text = "Hello world Python Test"
x= r"[A-Z][a-z]+"
print(re.findall(x, text))

#5
import re
text = "a123b axxxb acb aXb"
x = r"a.*b"
print(re.findall(x, text))

#6
import re
text = "Hello, world. Python is fun"
x = re.sub(r"[ ,.]", ":", text)
print(x)

#7
import re
text = "hello_world_python"
result = re.sub(r"_([a-z])", lambda x: x.group(1).upper(), text)
print(result)

#8
import re
text = "HelloWorldPython"
result = re.split(r"(?=[A-Z])", text)
print(result)

#9
import re
text = "HelloWorldPython"
result = re.sub(r"([A-Z])", r" \1", text)
print(result.strip())

#10
import re
text = "helloWorldPython"
result = re.sub(r"([A-Z])", r"_\1", text).lower()
print(result)