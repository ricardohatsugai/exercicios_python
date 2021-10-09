def imc(peso, altura):
    imc = peso / altura**2
    return imc

def mensagem(imc):
    if imc < 16:
        texto = ' baixo peso muito grave!'
    if imc >= 16 and imc < 17:
        texto = ' baixo peso grave.'
    if imc >= 17 and imc < 18.5:
        texto = ' baixo peso.'
    if imc >= 18.5 and imc < 25:
        texto = ' peso normal.'
    if imc >= 25 and imc < 30:
        texto = ' sobrepeso.'
    if imc >= 30 and imc < 35:
        texto = ' obesidade grau I.'
    if imc >= 35 and imc < 40:
        texto = ' obesidade grau II.'
    if imc > 40:
        texto = ' obesidade grau III.'

    return texto
