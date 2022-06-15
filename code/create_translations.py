

# data = subprocess.run("translate-cli -t zh 'This is a pen.' -o", shell=True, check=True, stdout=True, stderr=True)

# p = subprocess.run("translate-cli -t zh 'This is a pen.' -o", capture_output=True, text=True, shell=True)

# output = subprocess.run("translate-cli -t zh 'This is a pen.' -o", shell=True)
# output = subprocess.check_output("translate-cli -t zh 'This is a pen.' -o", shell=True)
# output = output.decode("utf-8")
# print(output)


from subprocess import PIPE, Popen

text = "This will be translated"
title = "Hello World!"

data = {
    "title": title,
    "example": {
       "title": text,
       "ok": True
    }
}

languages = ['es', 'fr', 'sv', 'de']

string_to_translate = (title + "," + text)

for language in languages:
    command = "translate-cli -t {} '{}' -o".format(language, string_to_translate)
    with Popen(command, stdout = PIPE, stderr = None, shell = True) as process:
        output = process.communicate()[0].decode('latin1')
        print(output)