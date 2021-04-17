require_relative "secuencia"

class Grafo

    def initialize(tamaño)
        @tamaño = tamaño
        @grafo = Array.new(tamaño) {Array.new}
    end

    def agregar(u,v)
        if u < 0 or u >= @tamaño or v < 0 or v >= @tamaño
            raise "Nodo fuera de los límites"
        else
            @grafo[u].append(v)
        end     
    end

    def vecinos(u)
        if u < 0 or u >= @tamaño
            raise "Nodo fuera de los límites"
        else
            @grafo[u]
        end  
    end
end

# Módulo secuencia para busqueda una clase abstracta
module Busqueda

    def initialize(tamaño)
        @grafo = Grafo.new tamaño
        @visitado = Array.new(tamaño)
    end

    def buscar(d, h)
        acum = 0                # Cuenta el número de nodos visitados
        @visitado.fill(false)
        @orden.agregar(d)
        encontrado = false
        while not @orden.vacio  # Orden será una pila o cola
            
            s = @orden.remover

            if @visitado[s]
                next
            else
                @visitado[s] = true
                acum += 1
            end

            if s == h
                encontrado = true
                # Limpiamos la estructura
                while not @orden.vacio
                    @orden.remover
                end
                break
            end
            
            @grafo.vecinos(s).each do |v|
                if not @visitado[v]
                    @orden.agregar(v)
                end
            end
        end
        encontrado ? acum : -1
    end

    def agregar(u,v)
        @grafo.agregar(u,v)
    end

end

class DFS

    include Busqueda
    
    def initialize(tamaño)
        super(tamaño)
        @orden = Pila.new
    end
end

class BFS
    
    include Busqueda

    def initialize(tamaño)
        super(tamaño)
        @orden = Cola.new
    end

end