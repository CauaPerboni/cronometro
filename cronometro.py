import time
import os
import threading
import keyboard 

class Cronometro: 
    def __init__(self, segundos=0, minutos=0, horas=0):
        self.segundos = segundos
        self.minutos = minutos
        self.horas = horas
        self.executando = True
        self.pausado = False

    def __repr__(self):
        return f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}'

    def incremento(self):
        self.segundos += 1
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos >= 60:
            self.minutos = 0
            self.horas += 1

    def mostrar_comandos(self):
        print("Comandos disponíveis:")
        print("  p - Pausar o cronômetro")
        print("  r - Reiniciar o cronômetro")
        print("  d - Despausar o cronômetro")
        print("  q - Sair do cronômetro")

    def start(self):
        while self.executando:
            if not self.pausado:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.mostrar_comandos()
                print(self)
                self.incremento()
            time.sleep(1)

    def pausar(self):
        self.pausado = True

    def despausar(self):
        self.pausado = False

    def reiniciar(self):
        self.segundos = 0
        self.minutos = 0
        self.horas = 0

def monitorar_comandos(cronometro):
    while True:
        if keyboard.is_pressed('p'):
            cronometro.pausar()
            print("Cronômetro pausado. Pressione 'r' para reiniciar, 'd' para despausar ou 'q' para sair.")
            while cronometro.pausado:
                if keyboard.is_pressed('r'): 
                    cronometro.reiniciar()
                    cronometro.pausado = False 
                    print("Cronômetro reiniciado.")
                    break
                elif keyboard.is_pressed('d'):
                    cronometro.despausar()
                    print("Cronômetro despausado.")
                    break 
                elif keyboard.is_pressed('q'):
                    cronometro.executando = False 
                    print("Saindo do cronômetro...")
                    return
        elif keyboard.is_pressed('q'): 
            cronometro.executando = False 
            print("Saindo do cronômetro...")
            return

if __name__ == "__main__":
    cronometro1 = Cronometro()
    
    t1 = threading.Thread(target=cronometro1.start)
    t2 = threading.Thread(target=monitorar_comandos, args=(cronometro1,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
