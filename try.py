infos={"name":"Alice","age":30,"city":"New York"}
infos["email"]={"email":"email@example.com","phone":"123-456-7890"}
for value in infos.items():
    print(infos['email']['phone'])
