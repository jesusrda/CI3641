# Módulo secuencia para simular una clase abstracta
module Secuencia
    def initialize
        @lista = Array.new
    end

    def agregar(x)
        raise NotImplementedError.new "Agregar no implementado"
    end

    def remover
        raise NotImplementedError.new "Remover no implementado"
    end

    def vacio
        raise NotImplementedError.new "Vacio no implementado"
    end
end

# Clase concreta pila
class Pila

    include Secuencia
    
    def agregar(x)
        @lista.append(x)    
    end

    def remover
        if @lista.empty?
            raise RuntimeError.new "La pila está vacía"
        else
            @lista.pop
        end
    end

    def vacio
        @lista.empty?
    end
end

# Clase concreta cola
class Cola

    include Secuencia

    def agregar(x)
        @lista.unshift(x)    
    end

    def remover
        if @lista.empty?
            raise RuntimeError.new "La cola está vacía"
        else
            @lista.pop
        end
    end

    def vacio
        @lista.empty?
    end
end