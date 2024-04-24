import esprima


file = open("./mern-marketplace/server/server.js", 'r', encoding='utf8')
code = file.read()


ast = esprima.parseModule(code, {"jsx":True, "range":True})

print(ast.body[4].range[1])
