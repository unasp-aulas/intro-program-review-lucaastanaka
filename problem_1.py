def main(Salario, Cargo):
    
    if Cargo == "Junior":
        Salario_novo = Salario * 1.15
        resultado = f"(Olá, seu cargo é {Cargo} e seu novo salario é de {Salario_novo})"
        return Salario_novo
    elif Cargo == "Pleno":
        Salario_novo = Salario * 1.26
        resultado = f"(Olá, seu cargo é {Cargo} e seu novo salário é de {Salario_novo})"
        return Salario_novo
    elif Cargo == "Senior":
        Salario_novo = Salario * 1.34
        resultado = f"(Olá, seu cargo é {Cargo} e seu novo salário é de {Salario_novo})"
        return Salario_novo
        print(resultado)
        
main(float(input("Entre o seu salario: ")), input("Entre o seu cargo: "))
        